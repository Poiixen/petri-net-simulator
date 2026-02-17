# I have neither given nor received unauthorized aid on this assignment

# parse functions
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
    # all in one formatter
    lines = []
    lines.append(f"STEP {step}:")

    # INM -----------------------
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
    
    lines.append(f"INM: {inm_str}")

    # INB -----------------------
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

    # AIB -----------------------
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

    # LIB -----------------------
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

    # ADB -----------------------
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

    # REB -----------------------
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

    # RGF -----------------------
    sorted_regs = sorted(rgf.keys())
    rgf_list = []

    for reg_name in sorted_regs:
        value = rgf[reg_name]
        reg_str = f"<{reg_name},{value}>"
        rgf_list.append(reg_str)

    rgf_str = ",".join(rgf_list)
    lines.append(f"RGF:{rgf_str}")

    # DAM -----------------------
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

    output = []
    step = 0
    #output.append(print_state(step, inm, inb, aib, lib, adb, reb, rgf, dam))

    while True:
        fired = False
        # try each transition, set fired = True if any fires

        if not fired:
            break
        step += 1
        output.append(print_state(step, inm, inb, aib, lib, adb, reb, rgf, dam))

    with open("simulation.txt", "w") as f:
        f.write("\n".join(output))

if __name__ == "__main__":
    main()