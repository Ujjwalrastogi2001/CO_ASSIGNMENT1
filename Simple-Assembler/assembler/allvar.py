#all variables 



inst = []     #list of all user input instructions
code = []      #list of all code lines after removing var ig do't need it 
count = 0     #instructions stored
count1 = 0      #total instructions - total var = total code lines 

variables = []  #variable list

labeld = []     #labeld list of defined label
labelc = []     #labelc list of called label

binlist = []       #binary representation
error = []      #errors


#flag
overflow = 0



#tuple of all valid opcode
validinst = ("add","sub","mov","ld","st","mul","div","rs","ls","xor","or","and","not","cmp","jmp","jlt","jgt","je","hlt")


#dictionary of all possible ISA inst
isa = {"add":("00000","","")
,"sub":(1,"00001","",""),"mov":(3,"00000","",""),"ld":(0,"00000","",""),"st":(0,"00000","",""),"mul":(0,"00000","",""),"div":(0,"00000","",""),
"rs":(0,"00000","",""),"ls":(0,"00000","",""),
"xor":(0,"00000","",""),"or":(0,"00000","",""),"and":(0,"00000","",""),"not":(0,"00000","",""),"cmp":(0,"00000","","")
,"jmp":(0,"00000","",""),"jlt":(0,"00000","",""),"jgt":(0,"00000","",""),"je":(0,"00000","",""),"hlt":(0,"00000","","")}

