
def AreaOfCircle(Radius, PI = 3.14):
    Result = PI * Radius * Radius
    return Result

def main():
    RValue = 10.5
    PIValue = 3.14

    # Positional
    Ans = AreaOfCircle(RValue,PIValue)      # Ans = Area(10.5,3.14)
    print("Area of Circle is : ",Ans)

    # Keyword Argument
    Ans = AreaOfCircle(PI = PIValue,Radius = RValue)      # Ans = Area(10.5,3.14)
    print("Area of Circle is : ",Ans)
    
    # Positional Argument and Second is default
    Ans = AreaOfCircle(10.5)      # Ans = Area(10.5)
    print("Area of Circle is : ",Ans)

    # Keyword Argument and Second is default
    Ans = AreaOfCircle(Radius = 10.5)      # Ans = Area(10.5)
    print("Area of Circle is : ",Ans)

    # Keyword Argument
    Ans = AreaOfCircle(PI = 7.10, Radius = 10.5)      # Ans = Area(10.5)
    print("Area of Circle is : ",Ans)

if __name__ == "__main__":
    main()