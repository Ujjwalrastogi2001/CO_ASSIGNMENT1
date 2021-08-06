import functions as f


#change from yash
def mainfun():
    code = []     
    overflow = False 
    count = 0     #instructions stored
    while(True):
        try:
            st = input()    
            count = count+1        #user input 
            if(count > 256):
                overflow = True

            st = st.split(' ')      # add R1 R2
            string = ''                # binary
            code.append(st)
        except EOFError:
            break
    
    n = 0
    while(len(code) != n):
        #label check 
        #var
        #halt
        #total instruc < 256
        pass

    while(len(code) != n):
        
        #function 
        op = f.getopcode(st[1])
        string = string + f.getopcode(st[0])   #opcode
        string = string + f.getregcode()
        if( op == 00000):
            add(st[1],st[2])

        
 

mainfun()


