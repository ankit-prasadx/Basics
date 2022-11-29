

def main():
    print("Enter Number : ")
    No = int(input())

    print("Factors are :")
    for i in range(1,No,1):
        if No % i == 0:
            print(i)
        # i = i + 1



if __name__ == "__main__":
    main()