from allvar import *

global line
global dictionfun
dictionfun={"add":"A","sub":"A","mul":"A","div":"C" ,"hlt":"F","mov":("B","C"),"st":"D","ld":"D",
"rs":"B","ls":"B","xor":"A","or":"A","and": "A", "not": "C","cmp":"C","jmp":"E","jlt":"E","jgt":"E","je":"E"}


# check for validity of opcode
def isvalid(opcode):
    global validlist
    if opcode in validinst:
        return True
    else:
        return False



def getbin(i):           #inst is the ith element of inst list
    global line 
    global error
    line = i
    if(inst[line][0] == 'var'):        #if a var statment then return
        return
    if(inst[line][0][0:len(inst[i][0])-1]  in labeld.keys()):
        if(isvalid(inst[line][1]) == False):         #check if a valid opcode 
            error.append(["Invalid Opcode on line", i+1])       #if not append in error list and return
        else:
            callfunctions(inst[line][1::])
        return 
    if(isvalid(inst[line][0]) == False):         #check if a valid opcode 
        error.append(["Invalid Opcode on line", i+1])       #if not append in error list and return
        return 
    else:           #else call respective functions 
        callfunctions(inst[line])
        return


#checked for validity of opcode and label 
#now call respenctive functions and update binlist
def callfunctions(insilist):        #insilist list of instruction for ith iteration
    global binlist
    global dictionfun
    global line
    keyword=insilist[0]
    rema=""
    if(keyword in dictionfun.keys()):   #the first word is instruction
        if(len(insilist)==2):
            rema =convertBin(keyword,insilist[1])
        elif(len(insilist)==3):
            rema =convertBin(keyword,insilist[1],insilist[2])
        elif(len(insilist)==4):
            rema =convertBin(keyword,insilist[1],insilist[2],insilist[3])
        elif(len(insilist)==1):
            rema=convertBin(keyword)
        else:
            error.append(["Invalid Syntax",line+1])
    if(rema != ""):
        binlist.append(rema)
    return



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

def checkreg(r):
    if(r in ("R0","R1","R2","R3","R4","R5","R6","FLAGS")):
        return "R"
    elif(r[0] == "$"):
        return "I"
    else:
        error.append(["Invalid register name",line+1])      
        return "E"
 

#line 87 mov R3 FLAGS
def convertBin(keyword,var1=None,var2=None,var3=None):
    global isa
    global error
    global line
    if(keyword=="mov"):
        if(checkreg(var2)=="I"):
            keyword="movi"
            type="B"
        else:
            keyword="movr"
            type="C"
    else:
        type=dictionfun[keyword]
    if(type=="A" and checkValue(var1) == "R" and checkValue(var2) == "R"and checkValue(var3) == "R"):
        return isa[keyword]+"00"+reg[var1]+reg[var2]+reg[var3]  

    if(type=="B" and checkValue(var1) == "R" and checkValue(var2) == "I"):
        if(float(var2[1::]) != int(float(var2[1::]))):
            error.append(["A Imm must be a whole number <= 255 and >= 0",line+1])
            return ""
        if(int(var2[1::]) <= 0 or int(var2[1::])>= 255):
            error.append(["A Imm must be a whole number <= 255 and >= 0",line+1])
            return ""
        st = format(int(var2[1::]),"b")
        while(len(st) != 8):
            st = '0'+st
        return isa[keyword]+reg[var1]+st

    if(type=="C" and keyword == "movr" and checkValue(var1) == "R" and var2 == "FLAGS"):
        return isa[keyword]+"00000"+reg[var1]+reg[var2]

    if(type=="C" and checkValue(var1) == "R" and checkValue(var2) == "R"):
        return isa[keyword]+"00000"+reg[var1]+reg[var2]

    if(type=="D" and checkValue(var1)):
        if(var2 not in variables.keys()):
            error.append(["A mem_addr in load and store must be a variable",line+1])
            return ""
        return isa[keyword]+reg[var1]+variables[var2][1]

    if(type=="E"):              #branch
        if(var1 not in labeld.keys()):
            error.append(["A mem_addr in jump instructions must be a label",line+1])
            return ""
        return isa[keyword]+"000"+labeld[var1]

    if(type=="F"):
        return isa[keyword]+"00000000000"
    

#print at the end
def printbin():
    global error
    global binlist
    if(len(error)==0):          #no errors
        for i in range(0,len(binlist)):
            print(binlist[i])
    else:
       for i in range(0,len(error)):
            print(error[i][0]+", "+str(error[i][1]))
    return 0



