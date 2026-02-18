#I have neither given nor received unauthorized aid on this assignment

#parser functions
def parse_instructions(filename):
    instructions = []
    with open(filename, "r") as f: 
        for line in f: 
            line= line.strip()
            print(line)
            if line:
                line = line.strip("<>")
                parts = line.split(",")

                cleaned = []
                for p in parts:
                    cleaned.append(p.strip())

                instruction = tuple(cleaned)
                instructions.append(instruction)
    return instructions
def parse_registers(filename):
    registers = {} 
    #same as prev parse function but hashmap instead
    with open(filename, "r") as f:
        for line in f:
            line = line.strip()
            if line:
                line = line.strip("<>")
                parts = line.split(",")
                
                cleaned = []
                for p in parts:
                    cleaned.append(p.strip())
                print(cleaned)

                reg_name = cleaned[0]        
                reg_value = int(cleaned[1])
                registers[reg_name] = reg_value
    return registers
def parse_datamemory(filename):
    mem = {}
    with open(filename, "r") as f: 
        for line in f:
            line = line.strip()
            if line:
                line = line.strip("<>")
                parts = line.split(",")
                
                cleaned = []
                for p in parts:
                    cleaned.append(p.strip())

                value = int(cleaned[1])
                addr = int(cleaned[0])
                mem[addr] = value
    return mem 

def print_state(step, inm, inb, aib, lib, adb, reb, rgf, dam):
    #all in one formatter
    lines = []
    lines.append(f"STEP {step}:")

    #INM -----------------------
    inm_list = []
    for instruction in inm:
        parts = []
        for part in instruction:
            parts.append(str(part))
        
        inst_str = "<" + ",".join(parts) + ">"
        inm_list.append(inst_str)

    if inm_list:
        inm_str = ",".join(inm_list)
    else:
        inm_str = ""
    
    lines.append(f"INM:{inm_str}")

    #INB -----------------------
    inb_list = []
    for instruction in inb:
        parts = []
        for part in instruction:
            parts.append(str(part))

        inst_str = "<" + ",".join(parts) + ">"
        inb_list.append(inst_str)

    if inb_list:
        inb_str = ",".join(inb_list)
    else:
        inb_str = ""

    lines.append(f"INB:{inb_str}")

    #AIB -----------------------
    aib_list = []
    for instruction in aib:
        parts = []
        for part in instruction:
            parts.append(str(part))

        inst_str = "<" + ",".join(parts) + ">"
        aib_list.append(inst_str)

    if aib_list:
        aib_str = ",".join(aib_list)
    else:
        aib_str = ""

    lines.append(f"AIB:{aib_str}")

    #LIB -----------------------
    lib_list = []
    for instruction in lib:
        parts = []
        for part in instruction:
            parts.append(str(part))

        inst_str = "<" + ",".join(parts) + ">"
        lib_list.append(inst_str)

    if lib_list:
        lib_str = ",".join(lib_list)
    else:
        lib_str = ""

    lines.append(f"LIB:{lib_str}")

    #ADB -----------------------
    adb_list = []
    for instruction in adb:
        parts = []
        for part in instruction:
            parts.append(str(part))

        inst_str = "<" + ",".join(parts) + ">"
        adb_list.append(inst_str)

    if adb_list:
        adb_str = ",".join(adb_list)
    else:
        adb_str = ""

    lines.append(f"ADB:{adb_str}")

    #REB -----------------------
    reb_list = []
    for instruction in reb:
        parts = []
        for part in instruction:
            parts.append(str(part))

        inst_str = "<" + ",".join(parts) + ">"
        reb_list.append(inst_str)
        
    if reb_list:
        reb_str = ",".join(reb_list)
    else:
        reb_str = ""

    lines.append(f"REB:{reb_str}")

    #RGF -----------------------
    sorted_regs = sorted(rgf.keys())
    rgf_list = []

    for reg_name in sorted_regs:
        value = rgf[reg_name]
        reg_str = f"<{reg_name},{value}>"
        rgf_list.append(reg_str)

    rgf_str = ",".join(rgf_list)
    lines.append(f"RGF:{rgf_str}")

    #DAM -----------------------
    sorted_addrs = sorted(dam.keys())
    dam_list = []

    for addr in sorted_addrs:
        value = dam[addr]
        mem_str = f"<{addr},{value}>"
        dam_list.append(mem_str)

    dam_str = ",".join(dam_list)
    lines.append(f"DAM:{dam_str}")
    

    return "\n".join(lines)

def main():
    inm = parse_instructions("sample/instructions.txt")
    rgf = parse_registers("sample/registers.txt")
    dam = parse_datamemory("sample/datamemory.txt")

    inb, aib, lib, adb, reb = [], [], [], [], []
    step = 0
    output = []
    order = {} 

    for i, instruction in enumerate(inm):
        order[instruction] = i
    next = len(inm)

    output.append(print_state(step, inm, inb, aib, lib, adb, reb, rgf, dam))

    while True:
        fired = False
        #try each transition, set fired = True if any fires

        #transition 1 and 2; read & decode  
        if len(inm) > 0: 
            opcode, destination, src, src1 = (
                inm[0][0],
                inm[0][1],
                inm[0][2],
                inm[0][3],
            )

            if (src in rgf) and (src1 in rgf):
                val, val1 = rgf[src], rgf[src1]           
                new = (opcode, destination, val, val1)
                
                inb.append(new)
                order[new] = order[inm[0]]
                del order[inm[0]]        

                inm.pop(0)
                fired = True

        #transition 3 and 4; issue1 & issue2
        if len(inb) > 0:
            for i in range(len(inb)):
                opcode = inb[i][0]
                if (opcode == "ADD") or (opcode == "SUB") or (opcode == "AND") or (opcode == "OR"):
                    aib.append(inb[i])
                    inb.pop(i)
                    fired = True
                    break
                elif (opcode == "LD"): #issue2
                    lib.append(inb[i])
                    inb.pop(i)
                    fired = True
                    break

        #transition 5; ALU 
        if len(aib) > 0:
            opcode, destination, val, val1 = (
                aib[0][0],
                aib[0][1],
                aib[0][2],
                aib[0][3],
            )
            if opcode == "ADD":
                res = (val + val1)
            elif opcode == "SUB":
                res = (val - val1)
            elif opcode == "AND":
                res = (val and val1)
            elif opcode == "OR":
                res = (val or val1)

            res_token = (destination, res)
            reb.append(res_token)

            order[res_token] = order[aib[0]]
            del order[aib[0]]
            aib.pop(0)
            fired = True

        #transition 6; addr
        if len(lib) > 0: 
            destination, val, val1 = (
                lib[0][1],
                lib[0][2],
                lib[0][3],
            )
            address = val + val1
            addr_token = (destination, address)
            adb.append(addr_token)

            order[addr_token] = order[lib[0]]
            del order[lib[0]]
            lib.pop(0)
            fired = True

        #transition 7; load
        if len(adb) > 0: 
            destination, address = (
                adb[0][0],
                adb[0][1]
            )
            
            val = dam[address]
            res_token = (destination, val)
            reb.append(res_token)

            order[res_token] = order[adb[0]]
            del order[adb[0]]
            adb.pop(0)
            fired = True

        #transition 8; write 
        if len(reb) > 0:
            index = -1
            min_order = None

            for i in range(len(reb)):
                token_order = order[reb[i]]

            if (min_order is None) or (token_order < min_order):
                min_order = token_order
                index = i

            destination = reb[index][0]
            val = reb[index][1]
            rgf[destination] = val

            del order[reb[index]]
            reb.pop(index)
            fired = True

        if not fired:
            break

        step += 1
        output.append(print_state(step, inm, inb, aib, lib, adb, reb, rgf, dam))
            
    with open("simulation.txt", "w") as f:
        f.write("\n\n".join(output))
        f.write("\n")

if __name__ == "__main__":
    main()