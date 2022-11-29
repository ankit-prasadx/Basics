def AcceptInput(iSIze,Value):
    pass

def main():
    print("Enter how many number of element you want to enter : ", end = " ")
    iSize = int(input())
    
    Data_Input = []
    print("Please enter the data ")

    for iCnt in range(0,iSize,1):
        Value = int(input())
        Data_Input.append(Value)
    
    print("Data is : ",Data_Input)

if __name__ == "__main__":
    main()