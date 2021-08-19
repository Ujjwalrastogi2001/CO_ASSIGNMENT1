"""
-----------------------------------------------
Main File Simulator
-----------------------------------------------
Group Members
Mohit Sharma - 2020086 - mohit20086@iiitd.ac.in
Ujjwal Rastogi - 2020546 - ujjwal20546@iiitd.ac.in
Yash Agarwal - 2020551 - yash20551@iiitd.ac.in
------------------------------------------------
"""

from variables import *
from functions import *
def mainfun():
    initialize() # Load memory from stdin
    PC = 0 # Start from the first instruction
    while(True):
        Instruction = MEM[PC] # Get current instruction
        if(Instruction == "1001100000000000"):
            break
        execute(Instruction)
        #halted, new_PC = execute(Instruction); # Update RF compute new_PC
        dump() # Print PC and RF state
    
    MEM.dump() # Print memory state



mainfun()
