
def Outer():
    print("Inside Outer")

    def Inner():
        print("Inside Inner")
    
    return Inner

Ret = Outer()
print(Ret)
print(type(Ret))
Ret()
