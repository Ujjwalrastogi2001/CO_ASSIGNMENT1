MEM = []          #  Stores input
PC = 0            #  Program Counter 
RF = {"000":0,"001":0,"010":0,"011":0,"100":0,"101":0,"110":0,"111":0}  #KEY= (register name) VALUE= (int)

isa = {"00000":"add", "00001":"sub", "00010":"movi", "00011":"movr", "00100":"ld", "00101":"st"
,"00110":"mul", "00111":"div", "01000":"rs", "01001":"ls", "01010":"xor", "01011":"Or", "01100":"And",
"01101":"Not","01110":"cmp","01111":"jmp","10000":"jlt","10001":"jgt","10010":"je","10011":"hlt"}

flag = {"V":0,"L":0,"G":0,"E":0}


dictionfun={"add":"A","sub":"A","mul":"A","div":"C" ,"hlt":"F","movi":"B","movr":"C","st":"D","ld":"D",
"rs":"B","ls":"B","xor":"A","Or":"A","And": "A", "Not": "C","cmp":"C","jmp":"E","jlt":"E","jgt":"E","je":"E"}