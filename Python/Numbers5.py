
class Numbers:
    def __init__(self):
        self.Size = 0
        self.Arr = list()

    def Accept(self):
        print("Enter How many elements you want : ", end = " ")
        self.Size = int(input())

        print("Enter the Elements :")
        Value = 0
        for i in range(0,self.Size):
            Value = int(input())
            self.Arr.append(Value)

    def Display(self):
        print("Elements in list are : ")
        for i in range(0,self.Size):
            print(self.Arr[i])

    def Summation(self):
        Sum = 0
        for i in range(0,self.Size):
            Sum = Sum + self.Arr[i]
        
        return Sum

    def Average(self):
        Sum = 0
        for i in range(0,self.Size):
            Sum = Sum + self.Arr[i]
        
        return (Sum/self.Size)
    
    def Maximum(self):
        Max = self.Arr[0]
        for i in range(0,self.Size):
            if(Max < self.Arr[i]):
                Max = self.Arr[i]
        
        return (Max)
    
    def Minimum(self):
        Min = self.Arr[0]
        for i in range(0,self.Size):
            if(Min > self.Arr[i]):
                Min = self.Arr[i]
        
        return (Min)


def main():
    obj = Numbers()
    obj.Accept()
    obj.Display()

    Output = obj.Summation()
    print("Summation of all elements is : {}".format(Output))

    Output = obj.Average()
    print("Average of all elements is : {}".format(Output))
    
    Output = obj.Maximum()
    print("Maximum of all elements is : {}".format(Output))
    
    Output = obj.Minimum()
    print("Minimum of all elements is : {}".format(Output))

if __name__ == "__main__":
    main()