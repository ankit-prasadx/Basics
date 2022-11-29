# Accept 2 numbers and perform addition and substraction on it

# Kay karaycha ahe?       -> Behaviours (Functions)
# Addition and Substraction

# Te karayala kay lagnar ahe?       -> Characteristics (Data)
# 2 numbers

# Class  = Characteristics + Behaviour
# Class  = Data + Functions

class Arithmetic:
    def __init__(self,A,B):
        self.No1 = A
        self.No2 = B

    def Add(self):
        return self.No1+self.No2

    def Sub(self):
        return self.No1-self.No2


def main():
    print("Enter first number")
    Value1 = int(input())

    print("Enter second number")
    Value2 = int(input())

    obj = Arithmetic(Value1,Value2)

    Ans = obj.Add()
    print("Addition is :",Ans)

    Ans = obj.Sub()
    print("SubstractionS is :",Ans)



if __name__ == "__main__":
    main()