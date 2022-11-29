from AddModule1 import *
from sys import *

def main():
    if(len(argv) != 3):
        print("Invalid number of arguments")
        exit()
    Ret = Addition(int(argv[1]),int(argv[2]))
    print("Addition is : ",Ret)

if __name__ == "__main__":
    main()