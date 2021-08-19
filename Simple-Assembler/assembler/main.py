"""
-----------------------------------------------
main file assembler
-----------------------------------------------
group members
Mohit Sharma - 2020086 - mohit20086@iiitd.ac.in
ujjwal Rastogi - 2020546 - ujjwal20546@iiitd.ac.in
Yash Agarwal - 2020551 - yash20551@iiitd.ac.in
------------------------------------------------
"""


from functions import *
from allvar import *
from variablehltlabel import *


#main function
def mainfun():
    count = 0 # number of instructions stored
    count1 = 0  # total number instructions - total variable = total code lines

    #get all user input in list inst
    while(True):
        try:
            st = input()          #user input 
            if(count > 256):
                error.append(["Memory overflow",count+1])
                break
            st = st.strip()
            st = st.split()  #slpit instructions

            # #delete these line
            # if(st[0]== "EOF"):
            #     break
            # #till here
            if(st != [""]):    #if not a not a empty istruction then append in inst and increment count
                inst.append(st)
                count = count+1 
        except EOFError:
            break
    
    if(len(inst)== 0):            #empty file 
        return
    checkvar()    #check for validity of variables 
    if(printerror() == 1):
        return

     #total instructions - total var
    count1 = count - len(variables)

    checklabel(len(variables))    #get all labels
    checklabelmatch()    #check if both numbers match
    checklasthalt()    #check if last statment halt
    if(printerror() == 1):
        return

    variableaddress(count1)    #assign adderss to variables
    labeladdress()    #assign adderss to label
    for i in range(0,len(inst)):
        getbin(i)

    printbin()    #print binary output if no error
    return


#main function
mainfun()