class StaticDemo
{
    
    public StaticDemo()
    {
        System.out.println("Inside constructor of StaticDemo");
    }
    public static void main(String arr[])
    {
        System.out.println("Inside main");

/////////////////////////////////////As per C++//// Demo::No3
        System.out.println("Value of static No3 : "+Demo.No3);
/////////////////////////////////////As per C++//// Demo::No4
        System.out.println("Value of static No4 : "+Demo.No4);
        Demo.gun();

        Demo obj1 = new Demo();
        Demo obj2 = new Demo();
        obj1.Fun();
    }
    static
    {
        System.out.println("Inside static block of StaticDemo class which contains main");
    }
}

class Demo
{
    public int No1;             // non static characteristics
    public int No2;             // non static characteristics
    public static int No3;      // static characteristics
    public static int No4;      // static characteristics

    static                      // static block
    {
        System.out.println("Inside static block of Demo class");
        No3 = 51;
        No4 = 101;
    }

    public Demo()               // Constructor
    {
        System.out.println("Inside constructor");
        No1 = 11;
        No2 = 21;
    }
//As per C++ -- Fun() can access all characteristics
    public void Fun()           // Non static method
    {
        System.out.println("Inside non static method fun");
        System.out.println("Value of No1 : "+this.No1);
        System.out.println("Value of No2 : "+this.No2);
        System.out.println("Value of No3 : "+this.No3);
        System.out.println("Value of No4 : "+this.No4);
    }

//As per C++ -- gun() can access static characteristics (No3,No4)
    public static void gun()    // Static method
    {
        System.out.println("Inside static method gun");
        // System.out.println("Value of No1 : "+No1);
        // System.out.println("Value of No2 : "+No2);
        System.out.println("Value of No3 : "+No3);
        System.out.println("Value of No4 : "+No4);
    }
}