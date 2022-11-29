
class Value:
    def __init__(self,Data):
        self.No = Data
    def SumFactors(self):
        Sum = 0

        for i in range(1,(int(self.No/2) + 1)):
            if(self.No % i == 0):
                Sum = Sum + i
        
        return Sum

    def CheckPerfect(self):
        Ans = self.SumFactors()

        if(self.No == Ans):
            return True
        else:
            return False
    
    def CheckPrime(self):
        i = 0
        flag = False
        for i in range(2,int(self.No/2)+1):
            if(self.No % i == 0):
                flag = True
                break
        if(flag == True):
            return False
        else:
            return True

def main():
    print("Please enter number")
    A = int(input())

    obj = Value(A)
    bRet = obj.CheckPrime()
    if(bRet == True):
        print("{} is a prime number".format(A))
    else:
        print("{} is not a prime number".format(A))

if __name__ == "__main__":
    main()