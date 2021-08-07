from allvar import *

global line

#handle overflow case 
#what to do of overflow
#what to store in overflow case

def validregister(r):
    global error
    global line
    i = line
    if(r in ("R0","R1","R2","R3","R4","R5","R6")):
        return True
    elif( r == "FALGS"):
        error.append(["Invalid use of FLAGS register",i+1])
        return False
    else:
        error.append(["Invalid register name",i+1])
        return False
        

def add():
    global inst
    global binlist
    global reg
    global line
    global overflow
    global reg
    i = line
    if(len(inst[i]) != 4):
        error.append(["Inviaid Syntax",i+1])
        return " "
    if(validregister(inst[i][1])== True and validregister(inst[i][2]) == True and validregister(inst[i][3]) == True):
        sum = reg[inst[i][3]][0]+reg[inst[i][2]][0]
        
        if(sum > 2^16):
            overflow = 1
        else:
            reg[inst[i][1]][0] = sum
    return "00"+reg[inst[i][1]][1]+reg[inst[i][2]][1]+reg[inst[i][3]][1]



def sub():
    global inst
    global binlist
    global reg
    global line
    global overflow
    global reg
    i = line
    if(len(inst[i]) != 4):
        error.append(["Inviaid Syntax",i+1])
        return " "
    if(validregister(inst[i][1])== True and validregister(inst[i][2]) == True and validregister(inst[i][3]) == True):
        subt = reg[inst[i][2]][0]-reg[inst[i][3]][0]
        if(subt < 0):
            overflow = 1
        else:
            reg[inst[i][1]][0] = subt
    return "00"+reg[inst[i][1]][1]+reg[inst[i][2]][1]+reg[inst[i][3]][1]


def mul():
    global inst
    global binlist
    global reg
    global line
    global overflow
    global reg
    i = line
    if(len(inst[i]) != 4):
        error.append(["Inviaid Syntax",i+1])
        return " "
    if(validregister(inst[i][1])== True and validregister(inst[i][2]) == True and validregister(inst[i][3]) == True):
        mult = reg[inst[i][3]][0]*reg[inst[i][2]][0]
        if(mult > 2^16):
            overflow = 1
        else:
            reg[inst[i][1]][0] = sum
    return "00"+reg[inst[i][1]][1]+reg[inst[i][2]][1]+reg[inst[i][3]][1]


def div():
    global inst
    global binlist
    global reg
    global line
    global overflow
    global reg
    i = line
    if(len(inst[i]) != 3):
        error.append(["Inviaid Syntax",i+1])
        return " "
    if(validregister(inst[i][1])== True and validregister(inst[i][2]) == True):
        quotient = reg[inst[i][2]][0]%reg[inst[i][3]][0]
        remainder = reg[inst[i][2]][0]+reg[inst[i][3]][0] - reg[inst[i][2]][0]
        reg["R0"][0] = quotient 
        reg["R1"][0] = remainder
    return "00"+reg[inst[i][1]][1]+reg[inst[i][2]][1]+reg[inst[i][3]][1]


def store():
    pass


def hlt():
    return "00000000000"

dictionfun={"00000":add,"00001":sub,"00110":mul,"00111":div ,"10011":hlt}

'''
inst list of user input  
overflow = False 
count = 0     #instructions stored
variables = []  #variable list
label = []      #label list
binlist = []       #binary representation
error = []      #errors
labeld = []     #labeld list of defined label
labelc = []     #labelc list of called label

'''

#find the address of variable
#append at the third position of the inner list
def variableaddress():
    global variables
    global count1
    format(10, "b")
    for i in range(0,len(variables)): 
        s = ''                                  #store address
        c = count1+1+i
        s = s+ format(c, "b")
        variables[i].append(s)      #append address in variables list

    # [item[1] for item in L] need it later ignore now



def getbin(i):           #inst is the ith element of inst list
    global line 
    line = i
    global error
    flagvalid = isvalid(inst[i][0])         #isvalid
    if(inst[i][0] == 'var'):        #if a var statment then return
        return
    if(flagvalid == False):         #check if a valid opcode 
        error.append(["Invalid Opcode on line", i+1])       #if not append in error list and return
        return 
    else:           #else call respective functions 
        callfunctions()
        return








#checked for validity of opcode and label 
#now call respenctive functions and update binlist
def callfunctions():
    global inst
    global binlist
    global dictionfun 
    global line 
    i = line
    bin  = ' '
    op = getopcode(inst[i][0])
    bin = bin+op
    #assign numbers to them

    rema = dictionfun[op]()
    print(bin)
    print(rema)
    print(bin)
    
    if(rema != ""):
        bin = bin + rema
        binlist.append(bin)



    


#check last statment is halt
def checklasthalt():
    flag = True
    global inst
    global error
    if(inst[len(inst)-1][0] != "hlt"):
        flag = False
    if(inst[len(inst)-1][0] == "hlt"):
        if (len(inst[len(inst)-1]) != 1):
            flag =  False
    if(flag == False):
        error.append(["last statment is not halt",len(inst)-1])








def getregcode():
    pass





#get opcode from dictionary ISA 
def getopcode(opcode):
    global isa
    return isa[opcode]



# check for validity of opcode
def isvalid(opcode):
    global validlist
    if opcode in validinst:
        return True
    else:
        return False
        

#error not sure 
#check if all called label are defined label 
#not necessary that all defined label is called
def checklabelmatch():
    global labelc
    global labeld
    global error
    for i in labelc:
        if( i[0]+':' not in labeld):
            error.append(["Label is not defined",i[1]])
    




