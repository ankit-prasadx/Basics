

def main():
    print("Enter Number : ")
    No = int(input())
    i = 1
    print("Factors are :")
    # for i in range(1,int(No/2)+1,1):
    while (i <= int(No/2)):
        if ((No % i) == 0):
            print(i)
        i = i + 1



if __name__ == "__main__":
    main()