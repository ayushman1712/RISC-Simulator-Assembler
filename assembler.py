f=open("test.txt")
lines=f.readlines()

#removing '\n' from all the lines
for i in range(len(lines)):
    if lines[i][-1]=="\n":
        lines[i]=lines[i][:len(lines[i])-1]

#removing  blank lines
lines1=[]
for i in lines:
    if i.strip()=="":
        pass
    else:
        lines1.append(i)

#dealing with var declaration lines
variables=[]
lines2=[]
for i in lines1:
    if i.split()[0]=='var':
        variables.append((i.split())[1])
    else:
        lines2.append(i)

#dealing with labels
labels={}
for i in range(len(lines2)):
    if ":" in lines2[i]:
        labels[lines2[i].split(":")[0]]=(lines2[i].split(":")[1]).strip()

#memory address allocation to all instructions
memory={}
for i in range(len(lines2)):
    if ":" not in lines2[i]:
        n=((7-len(bin(i)[2:]))*'0')+(bin(i)[2:])
        memory[lines2[i]]=str(n)
    else:
        n=((7-len(bin(i)[2:]))*'0')+(bin(i)[2:])
        memory[(lines2[i].split(":"))[0]]=str(n)

#memory address allocation to all variables
for i in range(len(lines2),len(lines2)+len(variables)):
    n=((7-len(bin(i)[2:]))*'0')+(bin(i)[2:])
    memory[variables[i-len(lines2)]]=str(n)

instructions_list=lines2
no_of_instructions=len(instructions_list)

opcodes = {
    "add"  :"00000", "sub"  :"00001", "movI" :"00010", "movR" :"00011",
    "ld"   :"00100", "st"   :"00101", "mul"  :"00110", "div"  :"00111",
    "rs"   :"01000", "ls"   :"01001", "xor"  :"01010", "or"   :"01011",
    "and"  :"01100", "not"  :"01101", "cmp"  :"01110", "jmp"  :"01111",
    "jlt"  :"11100", "jgt"  :"11101", "je"   :"11111", "hlt"  :"11010"
}

registers = {
    "R0" :"000", "R1" :"001", "R2" :"010", "R3" :"011", "R4" :"100", "R5" :"101","R6" :"110","FLAGS":"111"
}

def immediate(str):
    str=bin(int(str[1:]))[2:]
    str=('0'*(7-len(str)))+str
    return str

binary_output=[]
def opcodeGenerator(instructions_list):
    for instruction in instructions_list:
        machine_code=''
        if ":" in instruction:
            j=((instruction.split(":"))[1].strip()).split()
            instruction=(instruction.split(":"))[1].strip()
        else:
            pass
        i=instruction.split()

        if i[0]=='add':
            machine_code=machine_code+opcodes["add"]+"00"+registers[i[1]]+registers[i[2]]+registers[i[3]]
        elif i[0]=='sub':
            machine_code=machine_code+opcodes["sub"]+"00"+registers[i[1]]+registers[i[2]]+registers[i[3]]
        elif i[0]=='mul':
            machine_code=machine_code+opcodes["mul"]+"00"+registers[i[1]]+registers[i[2]]+registers[i[3]]
        elif i[0]=='xor':
            machine_code=machine_code+opcodes["xor"]+"00"+registers[i[1]]+registers[i[2]]+registers[i[3]]
        elif i[0]=='or':
            machine_code=machine_code+opcodes["or"]+"00"+registers[i[1]]+registers[i[2]]+registers[i[3]]
        elif i[0]=='and':
            machine_code=machine_code+opcodes["and"]+"00"+registers[i[1]]+registers[i[2]]+registers[i[3]]
        elif i[0]=='mov' and i[2][0]=='$':
            machine_code=machine_code+opcodes["movI"]+"0"+registers[i[1]]+immediate(i[2])
        elif i[0]=='rs':
            machine_code=machine_code+opcodes["rs"]+"0"+registers[i[1]]+immediate(i[2])
        elif i[0]=='ls':
            machine_code=machine_code+opcodes["ls"]+"0"+registers[i[1]]+immediate(i[2])
        elif i[0]=='mov':
            machine_code=machine_code+opcodes["movR"]+"00000"+registers[i[1]]+registers[i[2]]
        elif i[0]=='div':
            machine_code=machine_code+opcodes["div"]+"00000"+registers[i[1]]+registers[i[2]]
        elif i[0]=='not':
            machine_code=machine_code+opcodes["not"]+"00000"+registers[i[1]]+registers[i[2]]
        elif i[0]=='cmp':
            machine_code=machine_code+opcodes["cmp"]+"00000"+registers[i[1]]+registers[i[2]]
        elif i[0]=='ld':
            machine_code=machine_code+opcodes["ld"]+"0"+registers[i[1]]+memory[i[2]]
        elif i[0]=='st':
            machine_code=machine_code+opcodes["st"]+"0"+registers[i[1]]+memory[i[2]]
        elif i[0]=='jmp':
            machine_code=machine_code+opcodes["jmp"]+"0000"+memory[i[1]]
        elif i[0]=='jlt':
            machine_code=machine_code+opcodes["jlt"]+"0000"+memory[i[1]]
        elif i[0]=='jgt':
            machine_code=machine_code+opcodes["jgt"]+"0000"+memory[i[1]]
        elif i[0]=='je':
            machine_code=machine_code+opcodes["je"]+"0000"+memory[i[1]]
        elif i[0]=='hlt':
            machine_code=machine_code+opcodes["hlt"]+"00000"+"00000"+"0"
        binary_output.append(machine_code)
    return binary_output
f.close()
g=open("output.txt","w")
for i in opcodeGenerator(instructions_list):
   g.write(f"{i}\n")
g.close()