def CheckEven(No):
    if (No % 2 == 0):
        return True
    else:
        return False

def CheckEvenX(No):
    return (No % 2 == 0)    # == always returns True or False

Ret = CheckEvenX(12)

if (Ret == True):
    print("Its Even")
else:
    print("Its Odd")