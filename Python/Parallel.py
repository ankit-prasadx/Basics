import os
import multiprocessing

def Square(No):
    return (No*No)

def main():
    Data = [1,2,3,4,5,6]
    Result = []
    
    pool = multiprocessing.Pool()

    Result = pool.map(Square, Data)
    print("Result after Square operation is : ",Result)

if __name__ == "__main__":
    main()