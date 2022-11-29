
class Base
{
    public int A,B;
    public Base()
    {
        System.out.println("Base Constructor");
        this.A = 10;
        this.B = 20;
    }
    public void fun()
    {
        System.out.println("Inside Base Fun");
    }
    public void gun()
    {
        System.out.println("Inside Base Gun");
    }
    public void fun(int No)
    {
        System.out.println("Inside Base fun with integer");
    }

}

class Derived extends Base      // class Derived : public Base
{
    public int X,Y;
    public Derived()
    {
        System.out.println("Derived Constructor");
        this.X = 30;
        this.Y = 40;
    }
    public void sun()
    {
        System.out.println("Inside Derived Sun");
    }
    public void gun()
    {
        System.out.println("Inside Derived gun");
    }

}
class Single
{
    public static void main(String Arr[])
    {
        // Base bobj1 = new Base();
        // Derived dobj1 = new Derived();
        Base bobj2 = new Derived();
        // Derived dobj2 = new Base();
    
    // dobj1.fun();
    // dobj1.fun(11);
    // dobj1.gun();
    // dobj1.sun();

    bobj2.fun();
    bobj2.fun(11);
    bobj2.gun();
    // bobj2.sun();

    }
}