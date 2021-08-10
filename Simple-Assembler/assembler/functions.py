from allvar import *

global line


#inst list of user input  
overflow = False 

label = []      #label list
binlist = []       #binary representation

global dictionfun
dictionfun={"add":"A","sub":"A","mul":"A","div":"C" ,"hlt":"F","mov":("B","C"),"st":"D","ld":"D","rs":"B","ls":"B","xor":"A","or":"A","and": "A", "not": "C","cmp":"C","jmp":"E","jlt":"E","jgt":"E","je":"E"}






#handle overflow case 
#what to do of overflow
#what to store in overflow case
def checkValue(r):
    global error
    global line
    if(r in ("R0","R1","R2","R3","R4","R5","R6")):
        return "R"
    elif( r == "FLAGS"):
        error.append(["Invalid use of FLAGS register",line+1])
        return "E"
    # check overflow error in immediate >255
    elif(r[0] == "$"):
        return "I"
    else:
        error.append(["Invalid register name",line+1])      
        return "E"
        


def convertBin(keyword,var1=None,var2=None,var3=None):
    global isa
    type=dictionfun[keyword]
    if(keyword=="mov"):
        if(checkValue(var2)=="I"):
            keyword="movi"
            type="B"
        else:
            keyword="movr"
            type="C"

    #check for valid registers
    #if(var1!=None): checkValue(var1)
    if(type=="A" and checkValue(var1) == "R" and checkValue(var2) == "R"and checkValue(var3) == "R"):
        return isa[keyword]+"00"+reg[var1]+reg[var2]+reg[var3]  
    if(type=="B" and checkValue(var1) == "R" and checkValue(var2) == "I"):
        st = format(int(var2[1::]),"b")
        while(len(st) != 8):
            st = '0'+st
        return isa[keyword]+reg[var1]+st
    if(type=="C" and checkValue(var1) == "R" and checkValue(var2) == "R"):
        return isa[keyword]+"00000"+reg[var1]+reg[var2]
    if(type=="D" and checkValue(var1)):
        return isa[keyword]+reg[var1]+variables[var2][1]
    if(type=="E"):
        return isa[keyword]+"000"+variables[var1][1]
    if(type=="F"):
        return isa[keyword]+"00000000000"
    


    


def add():
    global inst
    global binlist
    global reg
    global line
    global overflow
    global reg
    if(len(inst[line]) != 4):
        error.append(["Inviaid Syntax",line+1])
        return " "
    if(checkValue(inst[line][1])== "R" and checkValue(inst[line][2]) == "R" and checkValue(inst[line][3]) == "R"):
        sum = reg[inst[line][3]][0]+reg[inst[line][2]][0]
        
        if(sum > 2^16):   
            overflow = 1
            reg[inst[line][1]][0] = sum - 2^16
        else:
            reg[inst[line][1]][0] = sum
    return "0000000"+reg[inst[line][1]][1]+reg[inst[line][2]][1]+reg[inst[line][3]][1]



def sub():
    global inst
    global binlist
    global reg
    global line
    global overflow
    global reg
    if(len(inst[line]) != 4):
        error.append(["Inviaid Syntax",line+1])
        return " "
    if(checkValue(inst[line][1])== "R" and checkValue(inst[line][2]) == "R" and checkValue(inst[line][3]) == "R"):
        subt = reg[inst[line][2]][0]-reg[inst[line][3]][0]
        if(subt < 0):
            overflow = 1
            reg[inst[line][1]][0] = 0
        else:
            reg[inst[line][1]][0] = subt
    return "0000100"+reg[inst[line][1]][1]+reg[inst[line][2]][1]+reg[inst[line][3]][1]


def mul():
    global inst
    global binlist
    global reg
    global line
    global overflow
    global reg
    if(len(inst[line]) != 4):
        error.append(["Inviaid Syntax",line+1])
        return " "
    if(checkValue(inst[line][1])== "R" and checkValue(inst[line][2]) == "R" and checkValue(inst[line][3]) == "R"):
        mult = reg[inst[line][3]][0]*reg[inst[line][2]][0]
        if(mult > 2^16):
            overflow = 1
            reg[inst[line][1]][0] = mul%2^10
        else:
            reg[inst[line][1]][0] = mul
    return "0011000"+reg[inst[line][1]][1]+reg[inst[line][2]][1]+reg[inst[line][3]][1]


def div():
    global inst
    global binlist
    global reg
    global line
    global overflow
    global reg
    if(len(inst[line]) != 3):
        error.append(["Inviaid Syntax",line+1])
        return " "
    if(checkValue(inst[line][1])== "R" and checkValue(inst[line][2]) == "R"):
        quotient = reg[inst[line][2]][0]%reg[inst[line][3]][0]
        remainder = reg[inst[line][2]][0]+reg[inst[line][3]][0] - reg[inst[line][2]][0]
        reg["R0"][0] = quotient 
        reg["R1"][0] = remainder
    return "0011100"+reg[inst[line][1]][1]+reg[inst[line][2]][1]+reg[inst[line][3]][1]


def store():
    pass


def hlt():
    return "00000000000"

def mov():
    global inst
    global binlist
    global reg
    global line
    global overflow
    global reg
    cr=inst[line]
    #check if the second register contains a value or not (if not can 0 be stored)
    if(len(cr!=3)):
        error.append(["Invalid Syntax",line+1])
        return " "
    if(checkValue(cr[1])== "R" and checkValue(cr[2]) == "R"):  #both are registers
        reg[cr[1]][0]=reg[cr[2]][0]
        return "0001100000"+reg[cr[1]][1]+reg[cr[2]][1]
    elif(checkValue(cr[1])== "R" and checkValue(cr[2]) == "I"):        #one value is immediate
        reg[cr[1]][0]=cr[2]
        return "00010000"+toBinary(cr[2])





#find the address of variable
#append at the third position of the inner list
# def variableaddress():
#     global variables
#     global count
#     format(10, "b")
#     for i in range(0,len(variables)): 
#         s = ''                                  #store address
#         c = count+1+varia
#         s = s+ format(c, "b")
#         variables[line].append(s)      #append address in variables list

    # [item[1] for item in L] need it later ignore now



def getbin(i):           #inst is the ith element of inst list
    global line 
    global error
    line = i
    flagvalid = isvalid(inst[line][0])         #isvalid
    if(inst[line][0] == 'var'):        #if a var statment then return
        return
    if(inst[line][0] in labeld.keys()):
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
    #bin  = ''
    # op = getopcode(inst[line][0])
    # bin = bin+op
    keyword=inst[line][0]
    rema=""
    if(keyword in dictionfun.keys()):   #the first word is instruction
        if(len(inst[line])==2):
            rema =convertBin(keyword,inst[line][1])
        elif(len(inst[line])==3):
            rema =convertBin(keyword,inst[line][1],inst[line][2])
        elif(len(inst[line])==4):
            rema =convertBin(keyword,inst[line][1],inst[line][2],inst[line][3])
        elif(len(inst[line])==1):
            rema=convertBin(keyword)
        else:
            error.append(["Invalid Syntax",line+1])
    
    #print(rema)
    if(rema != ""):
        binlist.append(rema)
    return


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
        

#print at the end
def printbin():
    global error
    global binlist
    l = 256 - len(binlist)      #  total 256 
    if(len(error)==0):          #no errors
        for i in range(0,len(binlist)):
            print(binlist[i])
    else:
       for i in range(0,len(error)):
            print(error[i][0]+", "+str(error[i][1]))
    return 0
