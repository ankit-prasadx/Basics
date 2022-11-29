import os

def main():
    print("PID of current provess is : ",os.getpid())
    print("PID of parent provess is : ",os.getppid())

if __name__ == "__main__":
    main()