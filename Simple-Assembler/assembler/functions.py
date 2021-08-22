from allvar import *

# check for validity of opcode
def isvalid(opcode):
    global validlist
    if opcode in validinst:
        return True
    else:
        return False



def getbin(i):           #inst is the ith element of inst list
    global error
    line = i
    if(inst[line][0] == 'var'):        #if a var statment then return
        return
    if(inst[line][0][0:len(inst[i][0])-1]  in labeld.keys()):
        if(len(inst[line][0])>=2):
            if(isvalid(inst[line][1]) == False):         #check if a valid opcode 
                error.append(["Invalid Opcode on line", i+1])       #if not append in error list and return
            else:
                callfunctions(inst[line][1::],line)   
        else:
            error.append(["Invalid syntax on line", line+1])   
        return 
    if(isvalid(inst[line][0]) == False):         #check if a valid opcode 
        error.append(["Invalid Opcode on line", i+1])       #if not append in error list and return
        return 
    else:           #else call respective functions 
        callfunctions(inst[line],line)
        return



#checked for validity of opcode and label 
#now call respenctive functions and update binlist
def callfunctions(insilist,line):        #insilist list of instruction for ith iteration
    global binlist
    global dictionfun
    keyword=insilist[0]
    rema=""
    type=dictionfun[keyword]
    if(keyword in dictionfun.keys()):   #the first element of list insilist is instruction
        if(len(insilist)==2 and type=="E" ):
            rema =convertBin(line, keyword,insilist[1])
        elif(len(insilist)==3 and (type=="C" or type=="B" or type=="D" or type == ('B','C'))):
            rema =convertBin(line, keyword,insilist[1],insilist[2])
        elif(len(insilist)==4 and type=="A"):
            rema =convertBin(line, keyword,insilist[1],insilist[2],insilist[3] )
        elif(len(insilist)==1 and type=="F" ):
            rema=convertBin(line, keyword)
        else:
            error.append(["Invalid Syntax",line+1])
    if(rema != ""):
        binlist.append(rema)
    return



#can delete last few linws
def checkValue(r,line):
    global error
    if(r in ("R0","R1","R2","R3","R4","R5","R6")):
        return "R"
    elif( r == "FLAGS"):
        error.append(["Invalid use of FLAGS register",line+1])
        return "E"
    elif(r[0] == "$"):
        return "I"
    else:
        error.append(["Invalid register name",line+1])      
        return "E"



# to check seconf register in mov 
def checkreg(r,line):
    if(r in ("R0","R1","R2","R3","R4","R5","R6","FLAGS")):
        return "R"
    elif(r[0] == "$"):
        return "I"
    else:
        error.append(["Invalid register name",line+1])      
        return "E"
 
 

#convert to binary output line by line 
def convertBin(line, keyword,var1=None,var2=None,var3=None):
    global isa
    global error
    if(keyword=="mov"):
        if(checkreg(var2,line)=="I"):
            keyword="movi"
            type="B"
        else:
            keyword="movr"
            type="C"
    else:
        type=dictionfun[keyword]
    if(type=="A" and checkValue(var1,line) == "R" and checkValue(var2,line) == "R"and checkValue(var3,line) == "R"):
        return isa[keyword]+"00"+reg[var1]+reg[var2]+reg[var3]  

    if(type=="B" and checkValue(var1,line) == "R" and checkValue(var2,line) == "I"):
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

    if(type=="C" and keyword == "movr" and checkValue(var1,line) == "R" and var2 == "FLAGS"):
        return isa[keyword]+"00000"+reg[var1]+reg[var2]

    if(type=="C" and checkValue(var1,line) == "R" and checkValue(var2,line) == "R"):
        return isa[keyword]+"00000"+reg[var1]+reg[var2]

    if(type=="D" and checkValue(var1,line)):
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
       printerror()
    return


#print error if any
def printerror():    
    if(len(error) != 0):
        for i in range(0,len(error)):
            print(error[i][0]+", "+str(error[i][1]))
    return 0 if len(error) == 0 else 1
