#main file 
# group members 
# Mohit Sharma - 2020086
# ujjwal Rastogi
# Yash - 2020551

"""
Command
to run a custom test case, without using automatedTesting:
path/to/Simple-Assembler/run < path/to/input/assembly/file >
path/to/output/binary/file


\automatedTesting\run
\Simple-Assembler\assembler\sample.txt
\Simple-Assembler\assembler\output.txt

"""




#variable name and label name are same not sure
#add sum calculate ku kr rhe h flag ka use toh simulator mei h 
#check multiple label with same name 
#dictionary of valid labels
#label name should not be a register
#label name should be alpha numberic
#A label name consists of alphanumeric characters and underscores.
#check at starting for valid opcode and halt then 
#if label then check at 1st index for opcode
#pass list to all arguments else define new functions for label  case don't want that


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
    """global inst
    global flag
    global count
    global variables
    global binlist
    global error
    global labeld
    global labelc"""
    count = 0
    

    #get all user input in list inst
    while(True):
        try:
            st = input()          #user input 
            if(count > 256):
                error.append(["Memory overflow",count+1])
                break
            st = st.strip()
            st = st.split(' ')          #slpit instructions
        
            #delete these line
            if(st[0]== "EOF"):
                break
            #till here
            if(st != [""]):         
                inst.append(st)
                count = count+1 

        except EOFError:
            break
     

    #check for validity of variables 
    checkvar()
    if(printerror() == 1):
        return

    #get all labels 
    checklabel()
    #check if both numbers match
    checklabelmatch()
    #check if last statment halt
    checklasthalt()
    
    if(printerror() == 1):
        return

    #total instructions - total var
    global count1
    count1 = count - len(variables)
    #assign adderss to variables
    variableaddress(count1)

    for i in range(0,len(inst)):
        getbin(i)

    #print bin
    printbin()
    return
    

#main function
mainfun()

