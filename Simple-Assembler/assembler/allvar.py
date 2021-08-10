#all variables 



inst = []     #list of all user input instructions
code = []      #list of all code lines after removing var ig do't need it 

count1 = 0      #total instructions - total var = total code lines 

variables = {} 

labeld = {}   #labeld dictionary of defined label
labelc = {}    #labelc dictionary of called label

binlist = []       #binary representation
error = []      #errors


#flag
overflow = 0



#tuple of all valid opcode
validinst = ("add","sub","mov","ld","st","mul","div","rs","ls","xor","or","and","not","cmp","jmp","jlt","jgt","je","hlt")


#dictionary of all possible ISA inst  
isa = {"add":"00000","sub":"00001","movi":"00010","movr":"00011","ld":"00100","st":"00101","mul":"00110","div":"00111",
"rs":"01000","ls":"01001",
"xor":"01010","or":"01011","and":"01100","not":"01101","cmp":"01110"
,"jmp":"01111","jlt":"10000","jgt":"10001","je":"10010","hlt":"10011"}


#dictionary or registers
reg = {"R0":"000","R1":"001","R2":"010","R3":"011","R4":"100","R5":"101","R6":"110"}



