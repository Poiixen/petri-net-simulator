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
    pass
def parse_datamemory(filename):
    pass

# main
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