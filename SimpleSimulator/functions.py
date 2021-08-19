from variables import *

def initialize():       #mem.initialize
    while(True):
        st = input().strip()         #user input
        MEM.append(st)
        if(st == "1001100000000000"):
            break
            
def execute(instruction):          #ee.execute(INST)
    opcode=instruction[0:5]        #first 5 digits
    #find function using opcode
    op(instruction)
    

def dump():     #printing the list or dic         
    print(inttobin(PC),end=" ")
    for i in RF.keys():
        print(inttobin(RF[i]),end=" ")
    print()


def reset():
    flag["V"] = flag["G"] =flag["E"] = flag["L"] = 0

def inttobin(val):
    return '{0:016b}'.format(val)
#-----------------------------------------------------TYPE A------------------------------------------------------------------------------

def add(r1,r2,r3):
    reset()
    sum=RF[r2]+RF[r3]
    if(sum >= 2 ^ 16):
        flag["V"] = 1
        RF[r1] = sum - 2 ^ 16
    else:
        RF[r1] = sum


def sub(r1,r2,r3):
    reset()
    sub = RF[r2]- RF[r3]
    if(sub < 0 ):
        flag["V"] = 1
        RF[r1] = 0
    else:
        RF[r1] = sub


def mul(r1,r2,r3):
    reset()
    mult = RF[r2]*RF[r3]
    if(mult >= 2 ^ 16):
        flag["V"] = 1
        RF[r1] = mult % 2^16
    else:
        RF[r1] = mult


def xor(r1,r2,r3):
    reset()
    bitxor = RF[r2]^RF[r3]
    RF[r1] = bitxor


def Or(r1,r2,r3):
    reset()
    bitor = RF[r2] | RF[r3]
    RF[r1] = bitor


def And(r1,r2,r3):
    reset()
    bitand = RF[r2] & RF[r3]
    RF[r1] = bitand

#-----------------------------------------------------TYPE B------------------------------------------------------------------------------



def movi(r1,imm):
    reset()
    RF[r1] = int(imm)

def rs(r1,imm):
    reset()
    RF[r1] >> int(imm)

def ls(r1,imm):
    reset()
    RF[r1] << int(imm)


#-----------------------------------------------------TYPE C------------------------------------------------------------------------------



def div(r1,r2):
    reset()
    quotient = int(RF[r1] / RF[r2])
    remainder = RF[r1] % RF[r2]
    RF["000"] = quotient
    RF["001"] = remainder

def Not(r1,r2):
    reset()
    n = ~RF[r2]           
    RF[r1] = n + 2**16

def cmp(r1,r2):
    reset()
    if(r1>r2):
        flag["G"]=1
    elif(r1<r2):
        flag["L"]=1
    else:
        flag["E"]=1

def movr(r1,r2):
    reset()
    RF[r1] = RF[r2]


#-----------------------------------------------------TYPE D------------------------------------------------------------------------------

def ld(r1,mem_add):
    reset()
    RF[r1] = int(MEM[int(mem_add)])

def st(r1,mem_add):
    reset()
    MEM[int(mem_add)] = inttobin(RF[r1])


#-----------------------------------------------------TYPE E------------------------------------------------------------------------------

def jmp(mem_add):
    reset()
    return int(mem_add)

def jlt(mem_add):
    if(flag("L") == 1):
        reset()
        return int(mem_add)
    else:
        reset()
        return PC+1

def jgt(mem_add):
    if(flag("G") == 1):
        reset()
        return int(mem_add)
    else:
        reset()
        return PC+1

def je(mem_add):
    if(flag("E") == 1):
        reset()
        return int(mem_add)
    else:
        reset()
        return PC+1


#-----------------------------------------------------TYPE F------------------------------------------------------------------------------


def hlt():
    pass


#------------------------------------------------------END---------------------------------------------------------------------------------

def op(instruction):
    global PC
    opcode=instruction[0:5]              #first 5 digits
    function=isa[opcode]                 
    type=dictionfun[function]
    if(type=="A"):
        r1=instruction[7:10]
        r2=instruction[10:13]
        r3=instruction[13:16]
        function(r1,r2,r3)
        PC+=1

    elif(type=="B"):
        r1=instruction[5:8]
        imm=instruction[8:16]
        function(r1,imm)
        PC+=1

    elif(type=="C"):
        r1=instruction[10:13]
        r2=instruction[13:16]
        function(r1,r2)
        PC+=1
    
    elif(type=="D"):
        r1=instruction[5:8]
        mem_add=instruction[8:16]
        function(r1,mem_add)
        PC+=1
    
    elif(type=="E"):
        mem_add=instruction[8:16]
        PC = function(mem_add)
    
    else: hlt()
        
        
        
            
        
