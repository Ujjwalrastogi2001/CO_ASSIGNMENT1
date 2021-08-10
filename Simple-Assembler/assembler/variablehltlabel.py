from allvar import *

# check for validity of opcode
def isvalidopcode(opcode):
    global validlist
    if opcode in validinst:
        return True
    elif opcode=="var":
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
    global inst
    global variables
    global error
    last = -1
    flagb = True
    for i in range(0, len(inst)):
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
                    error.append(
                        ["Variable name Cannot be a register name", i+1])
                    flagb = False
                # is a valid instruction name
                if(isvalidopcode(inst[i][1]) == True):
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
def variableaddress(co):
    global variables
    global count
    count=co
    format(10, "b")
    for i in variables.keys():
        s = ''  # store address
        c = count+variables[i]
        s = s + format(c, "b")
        while(len(s) != 8):
            s = '0'+s
        variables[i] = [variables[i], s]  # append address in variables list
    # [item[1] for item in L] need it later ignore now



# check if all called label are defined label
# not necessary that all defined label is called
def checklabelmatch():
    label={}
    global labelc
    global labeld
    global error
    for i in labelc.keys():
        if(i+':' not in labeld.keys()):
            error.append(["Label is not defined", i[1]])
        else:
            label[i]=labelc[i]
    labelc=label

#error
def checklabel():
    global inst
    global error
    global labeld
    global labelc
    for i in range(0, len(inst)):
        # label called check
        if(inst[i][0] in ("jmp", "jlt", "jgt", "je")):  # if branch instructions
            if(len(inst[i]) == 2):  # length od instruction 2
                if(alphanum(inst[i][1][0:len(inst[i][1])-1]) == False):  # is not valid
                    error.append(["Invalid label name", i+1])
                    flagb = False
                labelc[inst[i][1]] = i
            else:
                error.append(["Invalid instruction on line", i+1])

        # label defined check
        if(isvalidopcode(inst[i][0]) == False):
            if(isvalidopcode(inst[i][0][0:len(inst[i][0])-1]) == False):
                if(inst[i][0][len(inst[i][0])-1] == ":"):
                    labeld[inst[i][0]] = i
                else:
                    error.append(["Invalid instruction on line", i+1])
            else:
                error.append(["Syntax error on line", i+1])




#add r1 r2 r3 error aa rha h
# check last statment is halt
def checklasthalt():
    flagb = False
    flagmul = False
    present = -1
    global inst
    global error
    if(inst[len(inst)-1][0] != "hlt"):  # last statment is not hlt
        error.append(["last statment is not halt ", len(inst)])
        flagb = False
    if(inst[len(inst)-1][0] == "hlt"):  # last statment is hlt
        if (len(inst[len(inst)-1]) != 1):  # len of instruction is not 2
            error.append(["Invalid instruction on line", len(inst)-1])
            #flagb = False
        # for i in range(0, len(inst)):  # lablel case label: hlt
        #     if(inst[i][0] in labeld.keys()):  # if 1st value is a label
        #         if(inst[i][1] == "hlt"):  # second is hlt
        #             if (len(inst[i]) != 2):  # len of instruction is not 2
        #                 error.append(["Invalid instruction on line", i+1])
        #             elif(flagb == True):  # multiple hlt case
        #                 error.append(["Multiple halt instructions", i+1])
        #                 flagmul = True
        #             else:  # if all cases fail then flagb = true
        #                 flagb = True
        #                 present = i
        # for i in range(0, len(inst)):  # lablel case label: hlt
        #     if(inst[i][0] == "hlt"):
        #         if (len(inst[i]) != 1):
        #             error.append(["Invalid instruction on line", i+1])
        #         elif(flagb == True):
        #             error.append(["Multiple halt instructions", i+1])
        #             flagmul = True
        #         else:
        #             flagb = True
        # if(flagb == True and flagmul == False):  # hlt is not last statment
        #     error.append(["last statment is not halt, hlt present at ", present+1])
        # if(flagb == True and flagmul == True): 
        #     error.append(["last statment is not halt, last hlt present at ", present+1])


