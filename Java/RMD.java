
class Base
{
    public void fun()
    {
        System.out.println("Base Fun");
    }
    public void gun()
    {
        System.out.println("Base gun");
    }
    public void sun()
    {
        System.out.println("Base sun");
    }
}

class Derived extends Base
{
    public void fun()
    {
        System.out.println("Derived Fun");
    }
    public void gun()
    {
        System.out.println("Derived gun");
    }
}

class RMD
{
    public static void main(String Arr[])
    {
        Base bobj = new Derived();      // Upcasting
        
        bobj.fun();
        bobj.gun();
        bobj.sun();
        // bobj.run();
    }
}


/*
Base obj = new Base();      // Upcasting

Derived obj = new Derived();      // Upcasting

Base obj = new Derived();      // Upcasting

Derived obj = new Base();      // Upcasting
*/