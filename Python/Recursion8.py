
def Add(No):
    Sum = 0
    while(No > 0):
        Sum = Sum + No
        No = No - 1
    
    return Sum

Ret = Add(4)

print("Result is : ",Ret)