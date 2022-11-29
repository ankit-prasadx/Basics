from functools import reduce

CheckEven = lambda No: (No % 2 == 0)

MultiplyByTwo = lambda No: No*2

Sum = lambda A,B: A + B

def main():
    print("Enter how many number of element you want to enter : ", end = " ")
    iSize = int(input())
    
    Data_Input = []
    print("Please enter the data ")

    for iCnt in range(0,iSize,1):
        Value = int(input())
        Data_Input.append(Value)

    print("Data is : ",Data_Input)

    Data_Filter = list(filter(CheckEven, Data_Input))
    print("Data after filter : ",Data_Filter)

    Data_Map = list(map(MultiplyByTwo, Data_Filter))
    print("Data after map : ",Data_Map)

    Data_Result = reduce(Sum, Data_Map)
    print("Data after reduce : ",Data_Result)

if __name__ == "__main__":
    main()