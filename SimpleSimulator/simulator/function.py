from variables import *

def initialize():       #mem.initialize
    while(True):
        try:
            st = input().strip()         #user input
            #delete these line
            if(st == "EOF"):
                break
            #till here
            MEM.append(st)
        except EOFError:
            break
    for i in range(len(MEM),256):
            MEM.append("0000000000000000")

            
def execute(instruction):          #ee.execute(INST)
    opcode=instruction[0:5]        #first 5 digits
    #find function using opcode
    return op(instruction)
    

def dump(PC_new):     #printing the list or dic      
    global PC   
    print('{0:08b}'.format(PC),end=" ")
    for i in RF.keys():
        print(inttobin(RF[i]),end=" ")
    print()
    PC = PC_new

def MEM_dump():
    for i in MEM:
        print(i)
    for i in range(len(MEM),256):
        print("0000000000000000")
    print()


def reset():
    flag["V"] = flag["G"] =flag["E"] = flag["L"] = 0
    RF["111"] = 0


def inttobin(val):
    return '{0:016b}'.format(val)

def strtoint(st):
    intval = 0
    lenst = len(st)
    for i in range(0,lenst):
        if(st[i] == "1"):
            intval += 2**(lenst-i-1)
    return intval

#-----------------------------------------------------TYPE A------------------------------------------------------------------------------

def add(r1,r2,r3):
    sum=RF[r2]+RF[r3]
    if(sum >= 2 ^ 16):
        reset()
        flag["V"] = 1
        RF["111"] = 8
        RF[r1] = sum - 2 ^ 16
    else:
        RF[r1] = sum


def sub(r1,r2,r3):
    sub = RF[r2]- RF[r3]
    if(sub < 0 ):
        reset()
        flag["V"] = 1
        RF["111"] = 8
        RF[r1] = 0
    else:
        RF[r1] = sub


def mul(r1,r2,r3):
    mult = RF[r2]*RF[r3]
    if(mult >= 2 ^ 16):
        reset()
        flag["V"] = 1
        RF["111"] = 8
        RF[r1] = mult % 2^16
    else:
        RF[r1] = mult


def xor(r1,r2,r3):
    bitxor = RF[r2]^RF[r3]
    RF[r1] = bitxor
    reset()


def Or(r1,r2,r3):
    bitor = RF[r2] | RF[r3]
    RF[r1] = bitor
    reset()


def And(r1,r2,r3):
    bitand = RF[r2] & RF[r3]
    RF[r1] = bitand
    reset()

#-----------------------------------------------------TYPE B------------------------------------------------------------------------------



def movi(r1,imm):
    RF[r1] = strtoint(imm)
    reset()

def rs(r1,imm):
    RF[r1] >> strtoint(imm)
    reset()

def ls(r1,imm):
    RF[r1] << strtoint(imm)
    reset()


#-----------------------------------------------------TYPE C------------------------------------------------------------------------------



def div(r1,r2):
    quotient = int(RF[r1] / RF[r2])
    remainder = RF[r1] % RF[r2]
    RF["000"] = quotient
    RF["001"] = remainder
    reset()

def Not(r1,r2):
    n = ~RF[r2]           
    RF[r1] = n + 2**16
    reset()

def cmp(r1,r2):
    reset()
    if(RF[r1]>RF[r2]):
        flag["G"]=1
        RF["111"] = 2
    elif(RF[r1]<RF[r2]):
        flag["L"]=1
        RF["111"] = 4
    else:
        flag["E"]=1
        RF["111"] = 1
                     

def movr(r1,r2):
    RF[r1] = RF[r2]
    reset()


#-----------------------------------------------------TYPE D------------------------------------------------------------------------------

def ld(r1,mem_add):
    RF[r1] = int(MEM[strtoint(mem_add)])
    reset()

def st(r1,mem_add):
    MEM[strtoint(mem_add)] = inttobin(RF[r1])
    reset()


#-----------------------------------------------------TYPE E------------------------------------------------------------------------------

def jmp(mem_add):
    return strtoint(mem_add)
    reset()

def jlt(mem_add):
    if(flag["L"] == 1):
        reset()
        return strtoint(mem_add)
    else:
        reset()
        return PC+1

def jgt(mem_add):
    if(flag["G"] == 1):
        reset()
        return strtoint(mem_add)
    else:
        reset()
        return PC+1

def je(mem_add):
    if(flag["E"] == 1):
        reset()
        return strtoint(mem_add)
    else:
        reset()
        return PC+1


#-----------------------------------------------------TYPE F------------------------------------------------------------------------------


def hlt():
    pass


#------------------------------------------------------END---------------------------------------------------------------------------------

def op(instruction):
    opcode=instruction[0:5]              #first 5 digits
    function=isa[opcode]                 
    type=dictionfun[function]
    if(type=="A"):
        r1=instruction[7:10]
        r2=instruction[10:13]
        r3=instruction[13:16]
        fundictionary[opcode](r1,r2,r3)
        PC_new = PC + 1

    elif(type=="B"):
        r1=instruction[5:8]
        imm=instruction[8:16]
        fundictionary[opcode](r1,imm)
        PC_new = PC + 1

    elif(type=="C"):
        r1=instruction[10:13]
        r2=instruction[13:16]
        fundictionary[opcode](r1,r2)
        PC_new = PC + 1
    
    elif(type=="D"):
        r1=instruction[5:8]
        mem_add=instruction[8:16]
        fundictionary[opcode](r1,mem_add)
        PC_new = PC + 1
    
    elif(type=="E"):
        mem_add=instruction[8:16]
        PC_new = fundictionary[opcode](mem_add)
    
    else: hlt()

    return PC_new
        



fundictionary = {"00000":add, "00001":sub, "00010":movi, "00011":movr, "00100":ld, "00101":st
,"00110":mul, "00111":div, "01000":rs, "01001":ls, "01010":xor, "01011":Or, "01100":And,
"01101":Not,"01110":cmp,"01111":jmp,"10000":jlt,"10001":jgt,"10010":je,"10011":hlt}


        
            
        
