
def Add(No):
    if(No <= 0):
        return 0
    else:
        return (No + Add(No-1))

Ret = Add(4)

print("Result is : ",Ret)