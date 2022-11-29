def CheckEvenX(No):
    return (No % 2 == 0)    # == always returns True or False

Even = lambda No : No % 2 == 0

Ret = Even(13)

if (Ret == True):
    print("Its Even")
else:
    print("Its Odd")