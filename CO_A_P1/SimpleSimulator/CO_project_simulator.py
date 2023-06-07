Instructions=list()
MM=list()
Mem=list()
Errors=list()
labels=list()
variables=list()
Registers=list()
var_values=[]
program_counter=0
'''print("Give the assembly code as input(to end giving input type'hogya'):")
i=1
while True:
    print("Line",i,":",end=" ")
    a=input()
    a.strip()
    if a=='hogya':
        break
    else:
        Instructions.append(a)
        i+=1
for i in range(len(Instructions)):
    a=Instructions[i].split()
    Instructions[i]=[i+1]
    for j in range(len(a)):
        Instructions[i].append(a[j])'''




#Making all the Instructions locations get to a value zero.
for i in range(0,128):
        Mem.append(0)
for i in range(0,128):
        MM.append(0)
for i in range(0,8):
    Registers.append('0000000000000000')
for i in range(0,128):
        var_values.append(0)




#Functions definition
def todecimal(n,bit):
    va=0
    for i in range(0,bit):
        a=int(n[bit-1-i])
        va=va+a*(2**i)
    return va
def todecimalf(n,bit):
    va=0
    dp=bit
    for i in range(len(n)):
        if n[i]=='.':
            dp=i
            break
    for i in range(dp):
        va=va+int(n[dp-i-1])*(2**i)
    for i in range(dp+1,len(n)):
        va=va+int(n[i])*(2**(-1*(i-dp)))
    return va
def tobinary(n,bit):
    if n==0:
        return '0'*bit
    temp_lst=[]
    while n>0:
        q=n//2
        r=n%2
        temp_lst.append(r)
        n=q
    va=0
    for tt in range(0,len(temp_lst)):
        va=va+temp_lst[tt]*(10**(tt))
    x=bit-len(temp_lst)
    va=str(va)
    va='0'*x+va
    return va
def tobinaryf_(n):
    n0=int(n)
    n1=n-int(n)
    temp_lst=[]
    if n0==0:
        va='0'
    else:
        while n0>0:
            q=n0//2
            r=n0%2
            temp_lst.append(r)
            n0=q
        c=len(temp_lst)
        va=str(temp_lst[-1])
        for tt in range(1,c):
            va=va+str(temp_lst[c-tt-1])
    temp_lst=[]
    if n1==0:
        vb='0'
    else:
        while n1!=0:
            m=n1*2
            m0=int(m)
            m1=m-int(m)
            temp_lst.append(m0)
            n1=m1
        c=len(temp_lst)
        vb=str(temp_lst[0])
        for tt in range(1,c):
            vb=vb+str(temp_lst[tt])
    v=va+'.'+vb
    return v
def tobinary_f(n,bit):
    n0=int(n)
    n1=n-int(n)
    temp_lst=[]
    if n0==0:
        va='0'
    else:
        while n0>0:
            q=n0//2
            r=n0%2
            temp_lst.append(r)
            n0=q
        c=len(temp_lst)
        va=str(temp_lst[-1])
        for tt in range(1,c):
            va=va+str(temp_lst[c-tt-1])
    temp_lst=[]
    if n1==0:
        vb='0'
    else:
        while n1!=0:
            m=n1*2
            m0=int(m)
            m1=m-int(m)
            temp_lst.append(m0)
            n1=m1
        c=len(temp_lst)
        vb=str(temp_lst[0])
        for tt in range(1,c):
            vb=vb+str(temp_lst[tt])
    v=va+'.'+vb
    return '0'*(bit-len(v))+v
def reg_add(inpp):
    if inpp=='R0':
        return '000'
    elif inpp=='R1':
        return '001'
    elif inpp=='R2':
        return '010'
    elif inpp=='R3':
        return '011'
    elif inpp=='R4':
        return '100'
    elif inpp=='R5':
        return '101'
    elif inpp=='R6':
        return '110'
    elif inpp=='FLAGS':
        return '111'
def checkins(ins):
    lst=['add','sub','mov','ld','st','mul','div','rs','ls','xor','or','and','not','cmp','jmp','jlt','jgt','je','hlt','addf','subf','movf']
    if ins[1] in lst:
        return True
    else:
        return False
def checkregister(a):
    lst=['R0','R1','R2','R3','R4','R5','R6','FLAGS']
    if a in lst:
        return True
    else:
        return False
def checktype(ins):
    if len(ins)<2:
        return None
    lst=['add','sub','mul','xor','or','and','addf','subf']
    if ins[1] in lst:
        return 'A'
    lst=['ld','st']
    if ins[1] in lst:
        return 'D'
    lst=['jmp','jlt','jgt','je']
    if ins[1] in lst:
        return 'E'
    lst=['hlt']
    if ins[1] in lst:
        return 'F'
    lst=['rs','ls',]
    if ins[1] in lst:
        return 'B'
    lst=['movf']
    if ins[1] in lst:
        return 'B0'
    lst=['div','not','cmp']
    if ins[1] in lst:
        return 'C'
    if ins[1]=='mov':
        if checkregister(ins[3])==True:
            return 'C'
    if ins[1]=='mov':
        if checkregister(ins[3])==False:
            return 'B'
    return None
def islabel(a):
    if a[-1]==':' and a[-2]!=' ':
        return True
    else:
        return False



def takeout(n,m,o):
    if o-m == 1:
        return n[m]
    else:
        xx=n[m]
        for i in range(m+1,o):
            xx=xx+n[i]
        return xx
def typ(n):
    lst=['00000','00001','00110','01010','01011','01100']
    xx=takeout(n,0,5)
    if xx in lst:
        return 'A'
    lst=['00010','01000','01001']
    if xx in lst:
        return 'B'
    lst=['00011','00111','01101','01110']
    if xx in lst:
        return 'C'
    lst=['00100','00101']
    if xx in lst:
        return 'D'
    lst=['01111','11100','11101','11111']
    if xx in lst:
        return 'E'
    lst=['11010']
    if xx in lst:
        return 'F'
# handle=open("D:\Padhai Likhai\My codes\Python\sim.txt")
import sys
handle=sys.stdin.readlines()
i=0
for line in handle:
    line=str(line)
    Mem[i]=[]
    if typ(line)=='A':
        Mem[i].append(takeout(line,0,5))
        Mem[i].append('00')
        Mem[i].append(takeout(line,7,10))
        Mem[i].append(takeout(line,10,13))
        Mem[i].append(takeout(line,13,16))
    if typ(line)=='B':
        Mem[i].append(takeout(line,0,5))
        Mem[i].append('0')
        Mem[i].append(takeout(line,6,9))
        Mem[i].append(takeout(line,9,16))
    if typ(line)=='C':
        Mem[i].append(takeout(line,0,5))
        Mem[i].append('00000')
        Mem[i].append(takeout(line,10,13))
        Mem[i].append(takeout(line,13,16))
    if typ(line)=='D':
        Mem[i].append(takeout(line,0,5))
        Mem[i].append('0')
        Mem[i].append(takeout(line,6,9))
        Mem[i].append(takeout(line,9,16))
    if typ(line)=='E':
        Mem[i].append(takeout(line,0,5))
        Mem[i].append('0000')
        Mem[i].append(takeout(line,9,16))
    if typ(line)=='F':
        Mem[i].append(takeout(line,0,5))
        Mem[i].append('00000000000')
    i=i+1

        
        


#Working on Functions.
def repstr(a,n,tbr):
    va=a[0]
    for i in range(1,n):
        va=va+a[i]
    va=va+tbr
    for i in range(n+1,len(a)):
        va=va+a[i]
    return va

def add_(a,b,c):
    a=todecimal(a,3)
    b=todecimal(b,3)
    c=todecimal(c,3)
    b_val=todecimal(Registers[b],16)
    c_val=todecimal(Registers[c],16)
    v=b_val+c_val
    if todecimal(Registers[7],16)!=0:
        Registers[7]='0000000000000000'
    if v<0 or v>127:
        Registers[a]='0000000000000000'
        Registers[7]=repstr(Registers[7],12,'1')
        print("During execution of instruction in Mem[",program_counter,"] the value goes out of range.")
        quit()
    v=tobinary(v,16)
    Registers[a]=v

def addf_(a,b,c):
    a=todecimal(a,3)
    b=todecimal(b,3)
    c=todecimal(c,3)
    b_val=todecimalf(Registers[b],16)
    c_val=todecimalf(Registers[c],16)
    v=b_val+c_val
    if todecimal(Registers[7],16)!=0:
        Registers[7]='0000000000000000'
    if v<0 or v>127:
        Registers[a]='0000000000000000'
        Registers[7]=repstr(Registers[7],12,'1')
        print("During execution of instruction in Mem[",program_counter,"] the value goes out of range.")
        quit()
    v=tobinary_f(v,16)
    Registers[a]=v

def sub_(a,b,c):
    a=todecimal(a,3)
    b=todecimal(b,3)
    c=todecimal(c,3)
    b_val=todecimal(Registers[b],16)
    c_val=todecimal(Registers[c],16)
    v=b_val-c_val
    if todecimal(Registers[7],16)!=0:
        Registers[7]='0000000000000000'
    if v<0 or v>127:
        Registers[a]='0000000000000000'
        Registers[7]=repstr(Registers[7],12,'1')
        print("During execution of instruction in Mem[",program_counter,"] the value goes out of range.")
        quit()
    v=tobinary(v,16)
    Registers[a]=v

def subf_(a,b,c):
    a=todecimal(a,3)
    b=todecimal(b,3)
    c=todecimal(c,3)
    b_val=todecimalf(Registers[b],16)
    c_val=todecimalf(Registers[c],16)
    v=b_val-c_val
    if todecimal(Registers[7],16)!=0:
        Registers[7]='0000000000000000'
    if v<0 or v>127:
        Registers[a]='0000000000000000'
        Registers[7]=repstr(Registers[7],12,'1')
        print("During execution of instruction in Mem[",program_counter,"] the value goes out of range.")
        quit()
    v=tobinary_f(v,16)
    Registers[a]=v

def mul_(a,b,c):
    a=todecimal(a,3)
    b=todecimal(b,3)
    c=todecimal(c,3)
    b_val=todecimal(Registers[b],16)
    c_val=todecimal(Registers[c],16)
    v=b_val*c_val
    if todecimal(Registers[7],16)!=0:
        Registers[7]='0000000000000000'
    if v<0 or v>127:
        Registers[a]='0000000000000000'
        Registers[7]=repstr(Registers[7],12,'1')
        print("During execution of instruction in Mem[",program_counter,"] the value goes out of range.")
        quit()
    v=tobinary(v,16)
    Registers[a]=v

def xor_2b(a,b):
    if a=='0' and b=='0':
        return '0'
    if a=='1' and b=='1':
        return '0'
    if a=='1' and b=='0':
        return '1'
    if a=='0' and b=='1':
        return '1'
def xor_(a,b,c):
    a=todecimal(a,3)
    b=todecimal(b,3)
    c=todecimal(c,3)
    b_v=Registers[b]
    c_v=Registers[c]
    va=xor_2b(b_v[0],c_v[0])
    for i in range(1,16):
        va=va+xor_2b(b_v[i],c_v[i])
    Registers[a]=va
    if todecimal(Registers[7],16)!=0:
        Registers[7]='0000000000000000'

def or_2b(a,b):
    if a=='0' and b=='0':
        return '0'
    if a=='1' and b=='1':
        return '1'
    if a=='1' and b=='0':
        return '1'
    if a=='0' and b=='1':
        return '1'
def or_(a,b,c):
    a=todecimal(a,3)
    b=todecimal(b,3)
    c=todecimal(c,3)
    b_v=Registers[b]
    c_v=Registers[c]
    va=or_2b(b_v[0],c_v[0])
    for i in range(1,16):
        va=va+or_2b(b_v[i],c_v[i])
    Registers[a]=va
    if todecimal(Registers[7],16)!=0:
        Registers[7]='0000000000000000'

def and_2b(a,b):
    if a=='0' and b=='0':
        return '0'
    if a=='1' and b=='1':
        return '1'
    if a=='1' and b=='0':
        return '0'
    if a=='0' and b=='1':
        return '0'
def and_(a,b,c):
    a=todecimal(a,3)
    b=todecimal(b,3)
    c=todecimal(c,3)
    b_v=Registers[b]
    c_v=Registers[c]
    va=and_2b(b_v[0],c_v[0])
    for i in range(1,16):
        va=va+and_2b(b_v[i],c_v[i])
    Registers[a]=va
    if todecimal(Registers[7],16)!=0:
        Registers[7]='0000000000000000'

def mov_B(a,b):
    a=todecimal(a,3)
    va='0'*9+b
    Registers[a]=va
    if todecimal(Registers[7],16)!=0:
        Registers[7]='0000000000000000'

def movf_(a,b):
    a=todecimal(a,3)
    va='0'*8+b
    Registers[a]=va
    if todecimal(Registers[7],16)!=0:
        Registers[7]='0000000000000000'

def rs_(a,b):
    a=todecimal(a,3)
    a_v=Registers[a]
    b=todecimal(b,7)
    va='0'*b
    for i in range(0,16-b):
        va=va+a_v[i]
    Registers[a]=va
    if todecimal(Registers[7],16)!=0:
        Registers[7]='0000000000000000'

def ls_(a,b):
    a=todecimal(a,3)
    a_v=Registers[a]
    b=todecimal(b,7)
    va=a_v[b]
    for i in range(b+1,16):
        va=va+a_v[i]
    va='0'*b
    Registers[a]=va
    if todecimal(Registers[7],16)!=0:
        Registers[7]='0000000000000000'

def mov_C(a,b):
    a=todecimal(a,3)
    b=todecimal(b,3)
    Registers[a]=Registers[b]
    if todecimal(Registers[7],16)!=0:
        Registers[7]='0000000000000000'

def div_(a,b):
    a=todecimal(a,3)
    b=todecimal(b,3)
    a_v=todecimal(Registers[a],16)
    b_v=todecimal(Registers[b],16)
    if todecimal(Registers[7],16)!=0:
        Registers[7]='0000000000000000'
    if b_v==0:
        Registers[7]=repstr(Registers[7],12,'1')
        Registers[0]='0000000000000000'
        Registers[1]='0000000000000000'
    else:
        Registers[0]=tobinary(a_v//b_v,16)
        Registers[1]=tobinary(a_v%b_v,16)

def not_b(a):
    if a=='0':
        return '1'
    if a=='1':
        return '0'
def not_(a,b):
    a=todecimal(a,3)
    b=todecimal(b,3)
    b_v=Registers[b]
    va=not_b(b_v[0])
    for i in range(1,16):
        va=va+not_b(b_v[i])
    Registers[a]=va
    if todecimal(Registers[7],16)!=0:
        Registers[7]='0000000000000000'

def cmp_(a,b):
    a=todecimal(a,3)
    b=todecimal(b,3)
    a_v=Registers[a]
    b_v=Registers[b]
    if todecimal(a_v,16)==todecimal(b_v,16):
        Registers[7]=repstr(Registers[7],15,'1')
        Registers[7]=repstr(Registers[7],13,'0')
        Registers[7]=repstr(Registers[7],14,'0')
    elif todecimal(a_v,16)<todecimal(b_v,16):
        Registers[7]=repstr(Registers[7],13,'1')
        Registers[7]=repstr(Registers[7],15,'0')
        Registers[7]=repstr(Registers[7],14,'0')
    elif todecimal(a_v,16)>todecimal(b_v,16):
        Registers[7]=repstr(Registers[7],14,'1')
        Registers[7]=repstr(Registers[7],15,'0')
        Registers[7]=repstr(Registers[7],13,'0')

def st_(a,b):
    a=todecimal(a,3)
    Mem[todecimal(b,7)]=Registers[a]
    if todecimal(Registers[7],16)!=0:
        Registers[7]='0000000000000000'
    if todecimal(Registers[7],16)!=0:
        Registers[7]='0000000000000000'
    return 1
    

def ld_(a,b):
    a=todecimal(a,3)
    Registers[a]=tobinary(Mem[todecimal(b,7)],16)
    if todecimal(Registers[7],16)!=0:
        Registers[7]='0000000000000000'
    return 1
    

def jmp_(a):
    try:
        Registers[7]='0000000000000000'
        return todecimal(a,7)
    except:
        return -1

def jlt_(a):
    try:
        if Registers[7][13]=='1':
            Registers[7]='0000000000000000'
            return todecimal(a,7)
        else:
            if todecimal(Registers[7],16)!=0:
                Registers[7]='0000000000000000'
            return -1
    except:
        return -1

def jgt_(a):
    try:
        if Registers[7][14]=='1':
            Registers[7]='0000000000000000'
            return todecimal(a,7)
        else:
            if todecimal(Registers[7],16)!=0:
                Registers[7]='0000000000000000'
            return -1
    except:
        return -1

def je_(a):
    try:
        if Registers[7][15]=='1':
            Registers[7]='0000000000000000'
            return todecimal(a,7)
        else:
            if todecimal(Registers[7],16)!=0:
                Registers[7]='0000000000000000'
            return -1
    except:
        return -1

#print("variables",variables)
#print("Mem",Mem)

#Execution
def exct(inss,pc):
    if inss[0]=='00000':
        add_(inss[2],inss[3],inss[4])
        return pc+1
    elif inss[0]=='10000':
        addf_(inss[2],inss[3],inss[4])
        return pc+1
    elif inss[0]=='10001':
        subf_(inss[2],inss[3],inss[4])
        return pc+1
    elif inss[0]=='00001':
        sub_(inss[2],inss[3],inss[4])
        return pc+1
    elif inss[0]=='00010':
        mov_B(inss[2],inss[3])
        return pc+1
    elif inss[0]=='10010':
        movf_(inss[1],inss[2])
        return pc+1
    elif inss[0]=='00011':
        mov_C(inss[2],inss[3])
        return pc+1
    elif inss[0]=='00100':
        if ld_(inss[2],inss[3])==1:
            return pc+1
    elif inss[0]=='00101':
        if st_(inss[2],inss[3])==1:
            return pc+1
    elif inss[0]=='00110':
        mul_(inss[2],inss[3],inss[4])
        return pc+1
    elif inss[0]=='00111':
        div_(inss[2],inss[3])
        return pc+1
    elif inss[0]=='01000':
        rs_(inss[2],inss[3])
        return pc+1
    elif inss[0]=='01001':
        ls_(inss[2],inss[3])
        return pc+1
    elif inss[0]=='01010':
        xor_(inss[2],inss[3],inss[4])
        return pc+1
    elif inss[0]=='01011':
        or_(inss[2],inss[3],inss[4])
        return pc+1
    elif inss[0]=='01100':
        and_(inss[2],inss[3],inss[4])
        return pc+1
    elif inss[0]=='01101':
        not_(inss[2],inss[3])
        return pc+1
    elif inss[0]=='01110':
        cmp_(inss[2],inss[3])
        return pc+1
    elif inss[0]=='01111':
        v=jmp_(inss[2])
        if v!=-1:
            return v
        else:
            return pc+1
    elif inss[0]=='11100':
        v=jlt_(inss[2])
        if v!=-1:
            return v
        else:
            return pc+1
    elif inss[0]=='11101':
        v=jgt_(inss[2])
        if v!=-1:
            return v
        else:
            return pc+1
    elif inss[0]=='11111':
        v=je_(inss[2])
        if v!=-1:
            return v
        else:
            return pc+1
if len(Errors)==0:
    #print("Initially:")
    #print("RF-",Registers)
    #print("PC-",program_counter)
    #print("")
    #print("SIMULATOR:")
    while Mem[program_counter][0]!='11010':
        if islabel(Mem[program_counter])==True:
            program_counter=program_counter+1
        print(tobinary(program_counter,7),end="        ")
        if islabel(Mem[program_counter])==False:
            program_counter=exct(Mem[program_counter],program_counter)
        '''print("RF-",Registers)
        print("PC-",program_counter)
        print("")'''
        for km in range(0,8):
            print(Registers[km],end=" ")
        print("")

    print(tobinary(program_counter,7),end="        ")
    for km in range(0,8):
        print(Registers[km],end=" ")
    print("")
    for k in range(len(Mem)):
        if Mem[k]==0:
            MM[k]=Mem[k]
        elif islabel(Mem[k]):
            MM[k]=Mem[k]
        elif type(Mem[k])==str:
            MM[k]=Mem[k]
        else:
            nn=Mem[k][0]
            for l in range(1,len(Mem[k])):
                nn=nn+Mem[k][l]
            MM[k]=nn
    for km in range(len(MM)):
        if MM[km]==0:
            print(tobinary(MM[km],16))
        else:
            print(MM[km])
else:
    for i in range(len(Errors)):
        print("Error! ",Errors[i])
