from allvar import *


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
    global error
    flagvalid = isvalid(inst[i][0])         #isvalid
    if(inst[i][0] == 'var'):        #if a var statment then return
        return
    if(flagvalid == False):         #check if a valid opcode 
        error.append(["Invalid Opcode on line", i+1])       #if not append in error list and return
        return 
    else:           #else call respective functions 
        callfunctions(i)
        return




# check for validity of opcode
def isvalid(opcode):
    global validlist
    if opcode in validinst:
        return True
    else:
        return False




#checked for validity of opcode and label 
#now call respenctive functions and update binlist
def callfunctions(i):
    global inst
    global binlist
    bin  = ''
    op = getopcode(inst[i][0])
    bin.append(op)
    #assign numbers to them
    #if else opcode
    #dict function call 
    if(op == "00000"):
        add()

    


#check last statment is halt
def checklasthalt():
    flag = True
    global inst
    global error
    if(inst[len(inst)-1][1] != "hlt"):
        flag = False
    if(inst[len(inst)-1][1] == "hlt"):
        if (len(inst[len(inst)-1]) != 1):
            flag =  False
    if(flag == False):
        error.append(["last statment is not halt",len(inst)-1])





#get opcode from dictionary ISA 
def getopcode(opcode):
    global isa
    return isa[opcode][0]


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
    

def getregcode():
    pass

def add():
    pass

def sub():
    pass


def store():
    pass


