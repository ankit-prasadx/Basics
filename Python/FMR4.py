
def CheckEven(No):
    return (No % 2 == 0)

def MultiplyByTwo(No):
    return No*2

def filterX(Helper_Function, Data):
    Result = []
    for no in Data:
        if(Helper_Function(no) == True):
            Result.append(no)
    
    return Result

def mapX(Helper_Function,Data):
    Result = []
    for No in Data:
        Value = Helper_Function(No)
        Result.append(Value)
    
    return Result


def main():
    print("Enter how many number of element you want to enter : ", end = " ")
    iSize = int(input())
    
    Data_Input = []
    print("Please enter the data ")

    for iCnt in range(0,iSize,1):
        Value = int(input())
        Data_Input.append(Value)
    
    print("Data is : ",Data_Input)

    Data_Filter = filterX(CheckEven, Data_Input)
    print("Data after filter : ",Data_Filter)

    Data_Map = mapX(MultiplyByTwo, Data_Filter)
    print("Data after map : ",Data_Map)

if __name__ == "__main__":
    main()