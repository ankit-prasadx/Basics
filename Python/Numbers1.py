
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


def main():
    obj = Numbers()
    obj.Accept()
    obj.Display()

if __name__ == "__main__":
    main()