import time

def DisplayEven(No):
    # for i in range(No+1)
    for i in range(1,No+1,1):
        if(i % 2 == 0):
            print("Even number : ",i)


def DisplayOdd(No):
    # for i in range(No+1)
    for i in range(1,No+1,1):
        if(i % 2 != 0):
            print("Odd number : ",i)

def main():
    print("Demonstration of Serial Programming")
    DisplayEven(2000)
    DisplayOdd(2000)

if __name__ == "__main__":
    start_time1 = time.time()
    start_time = time.process_time()
    main()
    end_time1 = time.time()
    end_time = time.process_time()
    print("Execution time of Process is : ",end_time - start_time)
    print("Execution time of Application is : ",end_time1 - start_time1)