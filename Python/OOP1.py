
class Arithmetic:

    def __init__(self,A,B):
        print("Inside init method")
        self.No1 = A
        self.No2 = B

    def Addition(self):
        Ans = self.No1 + self.No2
        return Ans

    def Substraction(self):
        Ans = self.No1 - self.No2
        return Ans

def main():
    print("Inside main method")

    obj = Arithmetic(11,10)
    
    Ret = obj.Addition()
    print("Addition is : {}".format(Ret))

    Ret = obj.Substraction()
    print("Substraction is : {}".format(Ret))

    objX = Arithmetic(21,20)

if __name__ == "__main__":
    print("Inside Starter")
    main()