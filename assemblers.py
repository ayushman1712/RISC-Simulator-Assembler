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

errors_dict = {}
for i in range(len(lines1)+2):
    errors_dict[i] = []

#dealing with var declaration lines
variables=[]
lines2=[]
for i in lines1:
    if i.split()[0]=='var':
        variables.append((i.split())[1])
    else:
        lines2.append(i)

index_of_vars = len(variables)
while index_of_vars < len(lines1):
    if lines1[index_of_vars].strip()[:3] == 'var':
        errors_dict[index_of_vars+1].append("ERROR : variables not declared at the beginning")
        break
    else:
        index_of_vars += 1

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
    "R0" :"000", "R1" :"001", "R2" :"010", "R3" :"011", "R4" :"100", "R5" :"101","R6" :"110","FLAGS":"111", "" : "kuch bhi"
}

def immediate(stri, line_num):
    copy = float(stri[1:])
    if len(stri) > 7 or float(int(copy)) != copy or copy < 0:
        errors_dict[line_num].append("ERROR : Illegal Immediate value")
        stri = ""
    else:
        stri=bin(int(stri[1:]))[2:]
        stri=('0'*(7-len(stri)))+stri
    return stri


print(labels)
print(variables)
binary_output=[]
def opcodeGenerator(instructions_list):
    line_num = 0
    for instruction in instructions_list:
        machine_code=''
        if ":" in instruction:
            j=((instruction.split(":"))[1].strip()).split()
            instruction=(instruction.split(":"))[1].strip()
        else:
            pass
        i=instruction.split()

        if i[0]=='add':
            flag = 1
            line_num += 1
            if len(i) != 4:
                errors_dict[line_num].append("ERROR : Incorrect number of arguments")
                machine_code = "ERROR"
                flag = 0
            else:
                try:
                    register1 = i[1]
                except:
                    register1 = ""
                try:
                    register2 = i[2]
                except:
                    register2 = ""
                try:
                    register3 = i[3]
                except:
                    register3 = ""
                if register1 not in registers or register2 not in registers or register3 not in registers:
                    errors_dict[line_num].append("ERROR : Undefined register")
                    flag = 0
                elif "FLAGS" in [register1, register2, register3]:
                    errors_dict[line_num].append("ERROR : Illegal use of FLAGS register")
                    flag = 0
            if flag:
                machine_code=machine_code+opcodes["add"]+"00"+registers[i[1]]+registers[i[2]]+registers[i[3]]
        elif i[0]=='sub':
            flag = 1
            line_num += 1
            if len(i) != 4:
                errors_dict[line_num].append("ERROR : Incorrect number of arguments")
                machine_code = "ERROR"
                flag = 0
            else:
                try:
                    register1 = i[1]
                except:
                    register1 = ""
                try:
                    register2 = i[2]
                except:
                    register2 = ""
                try:
                    register3 = i[3]
                except:
                    register3 = ""
                if register1 not in registers and register2 not in registers and register3 not in registers:
                    errors_dict[line_num].append("ERROR : Undefined register")
                    flag = 0
                elif "FLAGS" in [register1, register2, register3]:
                    errors_dict[line_num].append("ERROR : Illegal use of FLAGS register")
                    flag = 0
            if flag:
                machine_code=machine_code+opcodes["sub"]+"00"+registers[i[1]]+registers[i[2]]+registers[i[3]]
        elif i[0]=='mul':
            flag = 1
            line_num += 1
            if len(i) != 4:
                errors_dict[line_num].append("ERROR : Incorrect number of arguments")
                machine_code = "ERROR"
                flag = 0
            else:
                try:
                    register1 = i[1]
                except:
                    register1 = ""
                try:
                    register2 = i[2]
                except:
                    register2 = ""
                try:
                    register3 = i[3]
                except:
                    register3 = ""
                if register1 not in registers and register2 not in registers and register3 not in registers:
                    errors_dict[line_num].append("ERROR : Undefined register")
                    flag = 0
                elif "FLAGS" in [register1, register2, register3]:
                    errors_dict[line_num].append("ERROR : Illegal use of FLAGS register")
                    flag = 0
            if flag:
                machine_code=machine_code+opcodes["mul"]+"00"+registers[i[1]]+registers[i[2]]+registers[i[3]]
        elif i[0]=='xor':
            flag = 1
            line_num += 1
            if len(i) != 4:
                errors_dict[line_num].append("ERROR : Incorrect number of arguments")
                machine_code = "ERROR"
                flag = 0
            else:
                try:
                    register1 = i[1]
                except:
                    register1 = ""
                try:
                    register2 = i[2]
                except:
                    register2 = ""
                try:
                    register3 = i[3]
                except:
                    register3 = ""
                if register1 not in registers and register2 not in registers and register3 not in registers:
                    errors_dict[line_num].append("ERROR : Undefined register")
                    flag = 0
                elif "FLAGS" in [register1, register2, register3]:
                    errors_dict[line_num].append("ERROR : Illegal use of FLAGS register")
                    flag = 0
            if flag:
                machine_code=machine_code+opcodes["xor"]+"00"+registers[i[1]]+registers[i[2]]+registers[i[3]]
        elif i[0]=='or':
            flag = 1
            line_num += 1
            if len(i) != 4:
                errors_dict[line_num].append("ERROR : Incorrect number of arguments")
                machine_code = "ERROR"
                flag = 0
            else:
                try:
                    register1 = i[1]
                except:
                    register1 = ""
                try:
                    register2 = i[2]
                except:
                    register2 = ""
                try:
                    register3 = i[3]
                except:
                    register3 = ""
                if register1 not in registers and register2 not in registers and register3 not in registers:
                    errors_dict[line_num].append("ERROR : Undefined register")
                    flag = 0
                elif "FLAGS" in [register1, register2, register3]:
                    errors_dict[line_num].append("ERROR : Illegal use of FLAGS register")
                    flag = 0
            if flag:
                machine_code=machine_code+opcodes["or"]+"00"+registers[i[1]]+registers[i[2]]+registers[i[3]]
        elif i[0]=='and':
            flag = 1
            line_num += 1
            if len(i) != 4:
                errors_dict[line_num].append("ERROR : Incorrect number of arguments")
                machine_code = "ERROR"
                flag = 0
            else:
                try:
                    register1 = i[1]
                except:
                    register1 = ""
                try:
                    register2 = i[2]
                except:
                    register2 = ""
                try:
                    register3 = i[3]
                except:
                    register3 = ""
                if register1 not in registers and register2 not in registers and register3 not in registers:
                    errors_dict[line_num].append("ERROR : Undefined register")
                    flag = 0
                elif "FLAGS" in [register1, register2, register3]:
                    errors_dict[line_num].append("ERROR : Illegal use of FLAGS register")
                    flag = 0
            if flag:
                machine_code=machine_code+opcodes["and"]+"00"+registers[i[1]]+registers[i[2]]+registers[i[3]]
        elif i[0]=='mov' and i[2][0]=='$':
            flag = 1
            line_num += 1
            if len(i) != 3:
                errors_dict[line_num].append("ERROR : Incorrect number of arguments")
                machine_code = "ERROR"
                flag = 0
            else:
                try:
                    register1 = i[1]
                except:
                    register1 = ""
                if register1 not in registers:
                    errors_dict[line_num].append("ERROR : Undefined register")
                    flag = 0
                elif "FLAGS" in [register1]:
                    errors_dict[line_num].append("ERROR : Illegal use of FLAGS register")
                    flag = 0
            if immediate(i[2], line_num) == "":
                flag = 0
            if flag:
                machine_code=machine_code+opcodes["movI"]+"0"+registers[i[1]]+immediate(i[2], line_num)
        elif i[0]=='rs':
            flag = 1
            line_num += 1
            if len(i) != 3:
                errors_dict[line_num].append("ERROR : Incorrect number of arguments")
                machine_code = "ERROR"
                flag = 0
            else:
                try:
                    register1 = i[1]
                except:
                    register1 = ""
                if register1 not in registers:
                    errors_dict[line_num].append("ERROR : Undefined register")
                    flag = 0
                elif "FLAGS" in [register1]:
                    errors_dict[line_num].append("ERROR : Illegal use of FLAGS register")
                    flag = 0
            if immediate(i[2], line_num) == "":
                flag = 0
            if flag:            
                machine_code=machine_code+opcodes["rs"]+"0"+registers[i[1]]+immediate(i[2], line_num)
        elif i[0]=='ls':
            flag = 1
            line_num += 1
            if len(i) != 3:
                errors_dict[line_num].append("ERROR : Incorrect number of arguments")
                machine_code = "ERROR"
                flag = 0
            else:
                try:
                    register1 = i[1]
                except:
                    register1 = ""
                if register1 not in registers:
                    errors_dict[line_num].append("ERROR : Undefined register")
                    flag = 0
                elif "FLAGS" in [register1]:
                    errors_dict[line_num].append("ERROR : Illegal use of FLAGS register")
                    flag = 0
            if immediate(i[2], line_num) == "":
                flag = 0
            if flag:            
                machine_code=machine_code+opcodes["ls"]+"0"+registers[i[1]]+immediate(i[2], line_num)
        elif i[0]=='mov': #add flags here
            flag = 1
            line_num += 1
            if len(i) != 3:
                errors_dict[line_num].append("ERROR : Incorrect number of arguments")
                machine_code = "ERROR"
                flag = 0
            else:
                try:
                    register1 = i[1]
                except:
                    register1 = ""
                if register1 not in registers:
                    errors_dict[line_num].append("ERROR : Undefined register")
                    flag = 0
            if flag:
                machine_code=machine_code+opcodes["movR"]+"00000"+registers[i[1]]+registers[i[2]]
        elif i[0]=='div':
            flag = 1
            line_num += 1
            if len(i) != 3:
                errors_dict[line_num].append("ERROR : Incorrect number of arguments")
                machine_code = "ERROR"
                flag = 0
            else:
                try:
                    register1 = i[1]
                except:
                    register1 = ""                
                try:
                    register2 = i[2]
                except:
                    register2 = ""
                if register1 not in registers and register2 not in registers:
                    errors_dict[line_num].append("ERROR : Undefined register")
                    flag = 0
                elif "FLAGS" in [register1, register2]:
                    errors_dict[line_num].append("ERROR : Illegal use of FLAGS register")
                    flag = 0
            if flag:
                machine_code=machine_code+opcodes["div"]+"00000"+registers[i[1]]+registers[i[2]]
        elif i[0]=='not':
            flag = 1
            line_num += 1
            if len(i) != 3:
                errors_dict[line_num].append("ERROR : Incorrect number of arguments")
                machine_code = "ERROR"
                flag = 0
            else:
                try:
                    register1 = i[1]
                except:
                    register1 = ""                
                try:
                    register2 = i[2]
                except:
                    register2 = ""
                if register1 not in registers and register2 not in registers:
                    errors_dict[line_num].append("ERROR : Undefined register")
                    flag = 0
                elif "FLAGS" in [register1, register2]:
                    errors_dict[line_num].append("ERROR : Illegal use of FLAGS register")
                    flag = 0
            if flag:
                machine_code=machine_code+opcodes["not"]+"00000"+registers[i[1]]+registers[i[2]]
        elif i[0]=='cmp':
            line_num += 1
            flag = 1
            if len(i) != 3:
                errors_dict[line_num].append("ERROR : Incorrect number of arguments")
                machine_code = "ERROR"
                flag = 0
            else:
                try:
                    register1 = i[1]
                except:
                    register1 = ""                
                try:
                    register2 = i[2]
                except:
                    register2 = ""
                if register1 not in registers and register2 not in registers:
                    errors_dict[line_num].append("ERROR : Undefined register")
                    flag = 0
                elif "FLAGS" in [register1, register2]:
                    errors_dict[line_num].append("ERROR : Illegal use of FLAGS register")
                    flag = 0
            if flag:
                machine_code=machine_code+opcodes["cmp"]+"00000"+registers[i[1]]+registers[i[2]]
        elif i[0]=='ld':
            line_num += 1
            flag = 1
            if len(i) != 3:
                errors_dict[line_num].append("ERROR : Incorrect number of aguments")
                machine_code = "ERROR"
                flag = 0
            else:
                try:
                    register1 = i[1]
                except:
                    register1 = ""
                if register1 not in registers:
                    errors_dict[line_num].append("ERROR : Undefined register")
                    flag = 0
                elif "FLAGS" in [register1]:
                    errors_dict[line_num].append("ERROR : Illegal use of FLAGS register")
                    flag = 0
                mem_addr = i[2]
                if mem_addr not in variables:
                    if mem_addr in labels:
                        errors_dict[line_num].append("ERROR : Misuse of label as variable")
                    else:
                        errors_dict[line_num].append("ERROR : Undefined variable used")
                    flag = 0
            if flag:
                machine_code=machine_code+opcodes["ld"]+"0"+registers[i[1]]+memory[i[2]]
        elif i[0]=='st':
            line_num += 1
            flag = 1
            if len(i) != 3:
                errors_dict[line_num].append("ERROR : Incorrect number of arguments")
                machine_code = "ERROR"
                flag = 0
            else:
                try:
                    register1 = i[1]
                except:
                    register1 = ""
                if register1 not in registers:
                    errors_dict[line_num].append("ERROR : Undefined register")
                    flag = 0
                elif "FLAGS" in [register1]:
                    errors_dict[line_num].append("ERROR : Illegal use of FLAGS register")
                    flag = 0
                mem_addr = i[2]
                if mem_addr not in variables:
                    if mem_addr in labels:
                        errors_dict[line_num].append("ERROR : Misuse of label as variable")
                    else:
                        errors_dict[line_num].append("ERROR : Undefined variable used")
                    flag = 0
            if flag:
                machine_code=machine_code+opcodes["st"]+"0"+registers[i[1]]+memory[i[2]]
        elif i[0]=='jmp':
            line_num += 1
            flag = 1
            if len(i) !=2:
                errors_dict[line_num].append("ERROR : Incorrect number of arguments")
                machine_code = "ERROR"
                flag = 0
            else:
                try:
                    register1 = i[1]
                except:
                    register1 = ""
                if register1 not in register:
                    errors_dict[line_num].append("ERROR : Undefined register")
                    flag = 0
                elif "FLAGS" in [register1]:
                    errors_dict[line_num].append("ERROR : Illegal use of FLAGS register")
                    flag = 0
                mem_addr = i[2]
                if mem_addr not in labels:
                    if mem_addr in variables:
                        errors_dict[line_num].append("ERROR : Misuse of variable as label")
                    else:
                        errors_dict[line_num].append("ERROR : Undefined label used")
                    flag = 0 
            if flag:           
                machine_code=machine_code+opcodes["jmp"]+"0000"+memory[i[1]]
        elif i[0]=='jlt':
            line_num += 1
            flag = 1
            if len(i) != 2:
                errors_dict[line_num].append("ERROR : Incorrect number of arguments")
                machine_code = "ERROR"
                flag = 0
            else:
                try:
                    register1 = i[1]
                except:
                    register1 = ""
                if register1 not in register:
                    errors_dict[line_num].append("ERROR : Undefined register")
                    flag = 0
                elif "FLAGS" in [register1]:
                    errors_dict[line_num].append("ERROR : Illegal use of FLAGS register")
                    flag = 0
                mem_addr = i[2]
                if mem_addr not in labels:
                    if mem_addr in variables:
                        errors_dict[line_num].append("ERROR : Misuse of variable as label")
                    else:
                        errors_dict[line_num].append("ERROR : Undefined label used")
                    flag = 0 
            if flag:
                machine_code=machine_code+opcodes["jlt"]+"0000"+memory[i[1]]
        elif i[0]=='jgt':
            line_num += 1
            flag = 1
            if len(i) != 2:
                errors_dict[line_num].append("ERROR : Incorrect number of arguments")
                machine_code = "ERROR"
                flag = 0
            else:
                try:
                    register1 = i[1]
                except:
                    register1 = ""
                    if register1 not in registers:
                        errors_dict[line_num].append("ERROR : Undefined register")
                        flag = 0
                    elif "FLAGS" in [register1]:
                        errors_dict[line_num].append("ERROR : Illegal use of FLAGS register")
                        flag = 0
                    mem_addr = i[2]
                    if mem_addr not in labels:
                        if mem_addr in variables:
                            errors_dict[line_num].append("ERROR : Misuse of variable as label")
                        else:
                            errors_dict[line_num].append("ERROR : Undefined label used")
                        flag = 0 
            if flag:
                machine_code=machine_code+opcodes["jgt"]+"0000"+memory[i[1]]
        elif i[0]=='je':
            line_num += 1
            flag = 1
            if len(i) != 2:
                errors_dict[line_num].append("ERROR : Incorrect number of arguments")
                machine_code = "ERROR"
                flag = 0
            else:
                try:
                    register1 = i[1]
                except:
                    register1 = ""
                    if register1 not in registers:
                        errors_dict[line_num].append("ERROR : Undefined register")
                        flag = 0
                    elif "FLAGS" in [register1]:
                        errors_dict[line_num].append("ERROR : Illegal use of FLAGS register")
                        flag = 0
                    mem_addr = i[2]
                    if mem_addr not in labels:
                        if mem_addr in variables:
                            errors_dict[line_num].append("ERROR : Misuse of variable as label")
                        else:
                            errors_dict[line_num].append("ERROR : Undefined label used")
                        flag = 0 
            if flag:
                machine_code=machine_code+opcodes["je"]+"0000"+memory[i[1]]
        elif i[0]=='hlt':
            line_num += 1
            machine_code=machine_code+opcodes["hlt"]+"00000"+"00000"+"0"
        else:
            line_num += 1
            errors_dict[line_num].append("ERROR : Type in instruction name")
        binary_output.append(machine_code)
    return binary_output

f.close()
###############################################################################################
if 'hlt' not in instructions_list and 'hlt\n' not in instructions_list:
    errors_dict[len(lines1)+1].append("ERROR : missing hlt instruction")
elif instructions_list[-1] not in ['hlt', 'hlt\n']:
    index = 0
    for i in lines1:
        i = i.strip()
        index += 1
        if i == 'hlt' or i == 'hlt\n':
            break
    if index != len(lines1):
        errors_dict[index].append("ERROR : hlt not last instruction")
###############################################################################################
g=open("output.txt","w")
for i in opcodeGenerator(instructions_list):
    g.write(f"{i}\n")
g.close()
print(errors_dict)
