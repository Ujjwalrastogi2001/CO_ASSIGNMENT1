#main file 
# group members 
# Mohit Sharma - 2020086
# ujjwal Rastogi
# Yash - 2020551

#all variable must be defined at the statting 
"""
<<<<<<< HEAD
Command
to run a custom test case, without using automatedTesting:
path/to/Simple-Assembler/run < path/to/input/assembly/file >
path/to/output/binary/file


\automatedTesting\run
\Simple-Assembler\assembler\sample.txt
\Simple-Assembler\assembler\output.txt



"""


=======
add: add R1 R2 R3
hlt
EOF

1st line error repeating
"""
>>>>>>> a53297d76b019ed3fb7945758fea4a7b962dd5e2

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
    global labelc
    binstr = ''

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
                       
            inst.append(st)
        except EOFError:
            break

        count = count+1  
    
    for i in range(0,len(inst)):
        #variable check
        if(inst[i][0]== "var"):
            if(len(inst[i]) == 2):
                variables[inst[i][1]]=i
            else:
                error.append(["Invalid instruction on line",i+1])

        #label called check
        if(inst[i][0] in ("jmp","jlt","jgt","je")):
            if(len(inst[i]) == 2):
                labelc[inst[i][1]]=i
            else:
                error.append(["Invalid instruction on line",i+1])
        
        #label defined check
        if(isvalid(inst[i][0]) == False):
            if(isvalid(inst[i][0][0:len(inst[i][0])-1]) == False):              
                if(inst[i][0][len(inst[i][0])-1] == ":"):
                    labelc[inst[i][1]]=i
                else:
                    error.append(["Invalid instruction on line",i+1])
            else:
                error.append(["Syntax error on line",i+1])


            

    #check if both numbers match
    checklabelmatch()

    checklasthalt()

    #total instructions - total var
    global count1
    count1 = count - len(variables)

    variableaddress()
            

    for i in range(0,len(inst)):
        getbin(i)

    printbin()


mainfun()

