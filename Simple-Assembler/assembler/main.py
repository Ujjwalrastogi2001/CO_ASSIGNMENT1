#main file 
# group members 
# Mohit Sharma - 2020086
# ujjwal Rastogi - 2020546
# Yash - 2020551

"""
Command
to run a custom test case, without using automatedTesting:
path/to/Simple-Assembler/run < path/to/input/assembly/file >
path/to/output/binary/file
"""
#in mov we can use flag
from functions import *
from allvar import *
from variablehltlabel import *


def printerror():
    #check for error in hlt variable label if yes then stop     
    if(len(error) != 0):
        for i in range(0,len(error)):
            print(error[i][0]+", "+str(error[i][1]))
        return 0 if len(error) == 0 else 1

def mainfun():
    count = 0 # instructions stored
    count1 = 0  # total instructions - total var = total code lines

    #get all user input in list inst
    while(True):
        try:
            st = input()          #user input 
            if(count > 256):
                error.append(["Memory overflow",count+1])
                break
            st = st.strip()
            st = st.replace("\t"," ")
            st = st.split(' ')  #slpit instructions
            
        
            #delete these line
            if(st[0]== "EOF"):
                break
            #till here
            if(st != [""]):         
                inst.append(st)
                count = count+1 

        except EOFError:
            break
    
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

    #print bin
    printbin()
    return
    

#main function
mainfun()

