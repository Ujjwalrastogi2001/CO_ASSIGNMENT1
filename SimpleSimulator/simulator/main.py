"""
-----------------------------------------------
main file simulator
-----------------------------------------------
group members
Mohit Sharma - 2020086 - mohit20086@iiitd.ac.in
ujjwal Rastogi - 2020546 - ujjwal20546@iiitd.ac.in
Yash Agarwal - 2020551 - yash20551@iiitd.ac.in
------------------------------------------------
"""

import numpy as np
from function import *
from variables import *
import matplotlib.pyplot as plt

# PC= mem_add
def mainfun():
    cycle=0
    cycList=[]
    global PC
    initialize() # Load memory from stdin
    PC = 0 # Start from the first instruction
    while(True):
        Instruction = MEM[PC] # Get current instruction
        cycle=cycle+1   # Increase cycle count by 1
        cycList.append(cycle)
        if(Instruction == "1001100000000000"):
            memList.append(PC)
            dump(PC_new)
            break
        PC_new = execute(Instruction)
        dump(PC_new) # Print PC and RF state
        PC = PC_new
    MEM_dump() # Print memory state
    
    for xe, ye in zip(cycList, memList):
        if(type(ye) is list):
            plt.scatter([xe] * len(ye), ye,s = 5, color="black")
        else:
            plt.scatter([xe], ye,s = 5,color="black")
    plt.show()
    plt.savefig('foo.png')
    



mainfun()

