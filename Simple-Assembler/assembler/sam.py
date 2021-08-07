# mohit
# my personal space to run some line of code for confirmation

variables = [["var1",1],["var2",4],["var3",5],["var4",6],["var98",254]]
addr = ''
count1 = 45
format(10, "b")
for i in range(0,len(variables)): 
    s = ''
    c = count1+1+i
    s = s+ format(c, "b")
    variables[i].append(s)
print(variables)
    
