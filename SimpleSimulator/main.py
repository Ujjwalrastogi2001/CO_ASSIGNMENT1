
def add(l):
    """global binlist
    global reg
    global line
    global flag"""
    if(len(l) != 4):
        error.append(["Inviaid Syntax", line+1])
        return " "
    if(validregister(l[1]) == True and validregister(l[2]) == True and validregister(l[3]) == True):
        """sum = reg[l[3]][0]+reg[l[2]][0]

        if(sum > 2 ^ 16):
            flag["V"] = 1
            reg[l[1]][0] = sum - 2 ^ 16
        else:
            reg[l[1]][0] = sum"""
        
        
    


def sub(l):
    """global binlist
    global reg
    global line
    global flag"""
    if(len(l) != 4):
        error.append(["Inviaid Syntax", line+1])
        return " "
    if(validregister(l[1]) == True and validregister(l[2]) == True and validregister(l[3]) == True):
        """subt = reg[l[2]][0]+reg[l[3]][0]
        if(subt < 0):
            flag["V"] = 1
            reg[l[1]][0] = 0
        else:
            reg[l][0] = subt"""
        return "00"+reg[l[1]][1]+reg[l[2]][1]+reg[l[3]][1]


def mul(l):
    """global binlist
    global reg
    global line
    global flag"""
    if(len(l) != 4):
        error.append(["Inviaid Syntax", line+1])
        return " "
    if(validregister(l[1]) == True and validregister(l[2]) == True and validregister(l[3]) == True):
        """mult = reg[l[3]][0]*reg[l[2]][0]
        if(mult > 2 ^ 16):
            flag["V"] = 1
            reg[l[1]][0] = mul % 2 ^ 10
        else:
            reg[l[1]][0] = mul"""
        return "00"+reg[l[1]][1]+reg[l[2]][1]+reg[l[3]][1]
    return ""


def div(l):
    global binlist
    global reg
    global line
    global flag
    if(len(l) != 3):
        error.append(["Inviaid Syntax", line+1])
        return " "
    if(validregister(l[1]) == True and validregister(l[2]) == True):
        """quotient = reg[l[2]][0] % reg[l[3]][0]
        remainder = reg[l][0]+reg[l[3]][0] - reg[l[2]][0]
        reg["R0"][0] = quotient
        reg["R1"][0] = remainder"""
        return "00000"+reg[l[1]][1]+reg[l[2]][1]
    return ""


def store():
    pass


def hlt(l):
    return "00000000000"

def mov():
    pass