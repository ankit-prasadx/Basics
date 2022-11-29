

def main():
    try:
        print("Enter first number")
        No1 = int(input())

        print("Enter second number")
        No2 = int(input())

    
        Ans = No1/No2
        print("Division is : ",Ans)
    
    except ZeroDivisionError:
        print("inside Zero division error")

    except ValueError:
        print("inside value error")

    except Exception:
        print("inside general except block")

    finally:
        print("Inside finally block")

if __name__ == "__main__":
    main()