#main file 
# group members 
# Mohit Sharma - 2020086
# ujjwal Rastogi
# Yash - 2020551



from functions import *
from allvar import *



'''
inst list of instructions user input
count = 0     #instructions stored
variables = []  #variable list
label = []      #label list
binlist = []       #binary representation
error = []      #errors
labeld = []     #labeld list of defined label
labelc = []     #labelc list of called label

'''


def mainfun():
    
    global inst
    global overflow
    global count
    global variables
    global label
    global binlist
    global error
    global labeld
    binstr = ''

    while(True):
        try:
            st = input()          #user input 
            if(count > 256):
                overflow = 1
                break
            st = st.strip()
            st = st.split(' ')          #slpit instructions
        
            #delete these line
            if(st[0]== "EOF"):
                break
            #till here

            
            
                            
            inst.append(st)
        except EOFError:
            break

        count = count+1  
    
    for i in range(0,len(inst)):
        #variable check
        if(inst[i][0]== "var"):
            if(len(inst[i]) == 2):
                variables.append([inst[i][1],i])
            else:
                error.append(["Invalid instruction on line",i+1])

        #label called check
        if(inst[i][0] in ("jmp","jlt","jgt","je")):
            if(len(inst[i]) == 2):
                labelc.append(inst[i][1])
            else:
                error.append(["Invalid instruction on line",i+1])


    #while loop mei add kr de
    #label defined check
    for i in range(0,len(inst)):
        global labeld
        if(isvalid(inst[i][0])):
            labelc.append([inst[i][0],i])

    #check if both numbers match
    checklabelmatch()

    checklasthalt()

    #total instructions - total var
    global count1
    count1 = count - len(variables)

    variableaddress()
            

    for i in range(0,len(inst)):
        getbin(i)

    print(binlist)


mainfun()

