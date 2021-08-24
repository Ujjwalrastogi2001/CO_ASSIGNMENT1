from allvar import *

# check for validity of opcode
def isvalidopcode(opcode):
    global validlist
    if opcode in validinst:
        return True
    else:
        return False


# check if name is alphanumercal
def alphanum(s):
    flagb = True
    for i in s:
        if(not((i >= chr(65) and i <= chr(90)) or
               (i >= chr(97) and i <= chr(122)) or (i >= chr(48) and i <= chr(57)) or i == "_")):
            flagb = False
            return flagb
    return flagb



# check for validity of variables
# variable not at starting, repeating, invalid, a regisgter name used, a valid opcode used are handled
def checkvar():
    last = -1
    flagb = True
    for i in range(0, len(inst)):
        flagb = True
        # variable check
        if(inst[i][0] == "var"):
            if(len(inst[i]) == 2):
                if(last+1 != i):  # last instruction was not variable
                    error.append(
                        ["All Variable not defined at the starting line", i+1])
                    flagb = False
                if(alphanum(inst[i][1]) == False):  # is not in valid list
                    error.append(["Invalid Variable name", i+1])
                    flagb = False
                if(inst[i][1] in variables.keys()):  # is already defined
                    error.append(["Variable name repeated", i+1])
                    flagb = False
                if(inst[i][1] in ("R0", "R1", "R2", "R3", "R4", "R5", "R6")):  # is a register name
                    error.append(["Variable name Cannot be a register name", i+1])
                    flagb = False
                if(isvalidopcode(inst[i][1]) == True):# is a valid instruction name
                    error.append(["Syntax error", i+1])
                    flagb = False
                if(flagb == True):  # if all conditions fails then is a valid variable
                    variables[inst[i][1]] = i
            else:  # length is not 2
                error.append(["Invalid instruction on line", i+1])
            last = i
    return



# find the address of variable
# append at the third position of the inner list
def variableaddress(count1):       
    for i in variables.keys():
        c = count1+variables[i]
        s = s = '{0:08b}'.format(c) 
        variables[i] = [variables[i], s]  # append address in variables list
    return



#multiple halt statment possible check it
def checklasthalt():
    if(inst[len(inst)-1][0] != "hlt"):  # last statment is not hlt
        if(inst[len(inst)-1][0][0:len(inst[len(inst)-1][0])-1] in labeld.keys()):
            if(inst[len(inst)-1][1] == "hlt"):  # last statment is hlt
                if (len(inst[len(inst)-1]) != 2):  # len of instruction is not 2 label + hlt
                    error.append(["Invalid instruction on line", len(inst)-1])
                    return
        else:
            error.append(["last statment is not halt ", len(inst)])
            return
    if(inst[len(inst)-1][0] == "hlt"):  # last statment is hlt
        if (len(inst[len(inst)-1]) != 1):  # len of instruction is not 1
            error.append(["Invalid instruction on line", len(inst)-1])
            return
    
    for i in range(0,len(inst)-1):
        if(inst[i][0] != "hlt"):  
            if(inst[i][0][0:len(inst[i][0])-1] in labeld.keys()):
                if(inst[i][1] == "hlt"):
                    error.append(["hlt is not at last statment present at ", i+1])
                    return
        if(inst[i][0] == "hlt"):  # last statment is hlt
             error.append(["hlt is not at last statment present at", i+1])



# check if all called label are defined label
# not necessary that all defined label is called
def checklabelmatch():
    global labelc
    global labeld
    label = {}
    global error
    for i in labelc.keys():
        if(i not in labeld.keys()):
            error.append(["Label is not defined at line ",labelc[i] ])
        else:
            label[i] = labelc[i]
    labelc = label
    


def labeladdress():
    for i in labeld.keys():
        s = '{0:08b}'.format(labeld[i])  # store address
        labeld[i] =  s



#check multiple label with same name 
def checklabel(count2):
    for i in range(count2, len(inst)):
        flagb = True
        # label called check
        if(inst[i][0] in ("jmp", "jlt", "jgt", "je")):  # if branch instructions
            if(len(inst[i]) == 2):  # length of instruction 2
                if(inst[i][1] in labelc.keys()): 
                    labelc[inst[i][1]].append(i+1)
                    continue
                if(alphanum(inst[i][1]) == False):  # is not valid
                    error.append(["Invalid label name", i+1])
                    flagb = False
                if(inst[i][1] in variables.keys() or inst[i][1] == "var" ):  # is a vaild variable name
                    error.append(["Variable and Label name cannot be same", i+1])
                    flagb = False
                if(inst[i][1] in ("R0", "R1", "R2", "R3", "R4", "R5", "R6")):  # is a register name
                    error.append(["Label name Cannot be a register name", i+1])
                    flagb = False
                if(isvalidopcode(inst[i][1]) == True):# is a valid instruction name
                        error.append(["Syntax error", i+1])
                        flagb = False
                if(flagb == True):
                    labelc[inst[i][1]] = [i+1]
            else:
                error.append(["Invalid instruction on line", i+1])

    for i in range(count2, len(inst)):
        flagb = True
        if(isvalidopcode(inst[i][0]) == False):# is not valid instruction name
            if(len(inst[i]) <= 5 and len(inst[i])>=2):  # length of instruction > 5
                if(inst[i][0][len(inst[i][0])-1] != ":"):           #last element is not :
                    error.append(["Invalid instruction on line", i+1])
                    flagb = False
                if(alphanum(inst[i][0][0:len(inst[i][0])-1]) == False):  # is not valid
                    error.append(["Invalid label name", i+1])
                    flagb = False
                if(inst[i][0][0:len(inst[i][0])-1] in variables.keys()):  # is a vaild variable name
                    error.append(["Variable and Label name cannot be same", i+1])
                    flagb = False
                if(inst[i][0][0:len(inst[i][0])-1] in ("R0", "R1", "R2", "R3", "R4", "R5", "R6")):  # is a register name
                    error.append(["Label name Cannot be a register name", i+1])
                    flagb = False
                if(inst[i][0][0:len(inst[i][0])-1] in labeld.keys()):  # is already defined
                    error.append(["Label name cannot be same", i+1])
                    flagb = False
                if(isvalidopcode(inst[i][0][0:len(inst[i][0])-1]) == True  or inst[i][1][0:len(inst[i][0])-2] == "var" ):# is a valid instruction name
                    error.append(["Syntax error", i+1])
                    flagb = False
                if(flagb == True):
                    labeld[inst[i][0][0:len(inst[i][0])-1]] = i-count2
            else:
                error.append(["Invalid instruction on line", i+1])