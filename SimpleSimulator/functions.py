from variables import *

def initialize():       #mem.initialize
    while(True):
        st = input().strip()         #user input
        MEM.append(st)
        if(st == "1001100000000000"):
            break
            
def execute(instruction):          #ee.execute(INST)
    opcode=instruction[0:5]    #first 5 digits
    #find function using opcode
    isa[str(opcode)](instruction)
    
def dump():     #printing the list or dic          
    pass
def update():           #PC.update
    pass


def add(instruction):
    sum = RF[instruction[10:13]] + RF[instruction[13:16]]
    if(sum > 2 ^ 16):
        flag["V"] = 1
        RF[instruction[7:10]] = sum - 2 ^ 16
    else:
        RF[instruction[7:10]] = sum


def sub(instruction):
    sub = RF[instruction[10:13]]- RF[instruction[13:16]]
    if(sub < 0 ):
        flag["V"] = 1
        RF[instruction[7:10]] = 0
    else:
        RF[instruction[7:10]] = sub


def mul(instruction):
    mult = RF[instruction[10:13]]*RF[instruction[13:16]]
    if(mult > 2 ^ 16):
        flag["V"] = 1
        RF[instruction[7:10]] = mult % 2^16
    else:
        RF[instruction[7:10]] = mult


def div(instruction):
    quotient = int(RF[instruction[10:13]] / RF[instruction[13:16]])
    remainder = RF[instruction[10:13]] % RF[instruction[13:16]]
    RF["000"] = quotient
    RF["001"] = remainder


def xor(instruction):
    pass
    
def 
def movi(instruction):
    pass

def movr(instruction):
    pass

#-----------------------------------------------------TYPE A------------------------------------------------------------------------------

def add(r1,r2,r3):
    sum=RF[r2]+RF[r3]
    if(sum > 2 ^ 16):
        flag["V"] = 1
        RF[r1] = sum - 2 ^ 16
    else:
        RF[r1] = sum

def sub(r1,r2,r3):
    sub = RF[r2]- RF[r3]
    if(sub < 0 ):
        flag["V"] = 1
        RF[r1] = 0
    else:
        RF[r1] = sub

def mul(r1,r2,r3):
    mult = RF[r2]*RF[r3]
    if(mult > 2 ^ 16):
        flag["V"] = 1
        RF[r1] = mult % 2^16
    else:
        RF[r1] = mult

def xor(r1,r2,r3):
    pass

def Or(r1,r2,r3):
    pass
def And(r1,r2,r3):
    pass


#-----------------------------------------------------TYPE B------------------------------------------------------------------------------



def movi(r1,imm):
    pass
def rs(r1,imm):
    pass
def ls(r1,imm):
    pass
def movr(r1,r2):
    pass


#-----------------------------------------------------TYPE C------------------------------------------------------------------------------



def div(r1,r2):
    quotient = int(RF[r1] / RF[r2])
    remainder = RF[r1] % RF[r2]
    RF["000"] = quotient
    RF["001"] = remainder

def Not(r1,r2):
    pass
def cmp(r1,r2):
    pass


#-----------------------------------------------------TYPE D------------------------------------------------------------------------------



def ld(r1,mem_add):
    pass

def st(r1,mem_add):
    pass


#-----------------------------------------------------TYPE E------------------------------------------------------------------------------

def jmp(mem_add):
    pass

def jlt(mem_add):
    pass

def jgt(mem_add):
    pass
def je(mem_add):
    pass


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
        function(r1,r2,r3)


    elif(type=="B"):
        r1=instruction[5:8]
        imm=instruction[8:16]
        function(r1,imm)

    elif(type=="C"):
        r1=instruction[10:13]
        r2=instruction[13:16]
        function(r1,r2)
    
    elif(type=="D"):
        r1=instruction[5:8]
        mem_add=instruction[8:16]
        function(r1,mem_add)
    
    elif(type=="E"):
        mem_add=instruction[8:16]
        function(mem_add)
    
    else: hlt()
        
        
        
            
        
