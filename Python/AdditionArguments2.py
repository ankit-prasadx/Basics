from AddModule1 import *
from sys import *

def main():
    print("Welcome to : ", argv[0])

    if(len(argv) == 2):

        if(argv[1] == "--U" or argv[1] == "--u"):
            print("Use the application as : ")
            print("python Name_Of_Application First_Number Second_Number")
            exit()
        
        if(argv[1] == "--H" or argv[1] == "--h"):
            print("Help : This is application is used to perform addition of 2 numbers")
            exit()

    if(len(argv) != 3):
        print("Invalid number of arguments")
        exit()
    Ret = Addition(int(argv[1]),int(argv[2]))
    print("Addition is : ",Ret)

if __name__ == "__main__":
    main()