
def Fact(No):
    if(No <= 0):
        return 1
    else:
        return (No * Fact(No-1))

Ret = Fact(4)

print("Result is : ",Ret)