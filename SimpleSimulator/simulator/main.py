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

from function import *
from variables import *

def mainfun():
    global PC
    initialize() # Load memory from stdin
    PC = 0 # Start from the first instruction
    while(True):
        Instruction = MEM[PC] # Get current instruction
        if(Instruction == "1001100000000000"):
            dump(PC_new)
            break
        PC_new = execute(Instruction)
        #halted, new_PC = execute(Instruction); # Update RF compute new_PC
        dump(PC_new) # Print PC and RF state
        PC = PC_new
    MEM_dump() # Print memory state



mainfun()

