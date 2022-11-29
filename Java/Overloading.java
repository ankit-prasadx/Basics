import java.lang.*;

class Demo
{
    public void fun()
    {
        System.out.println("Fun without parameters");
    }
    public void fun(int i)
    {
        System.out.println("Fun with one integer parameters");
    }
    public void fun(int i, int j)
    {
        System.out.println("Fun with two integer parameters");
    }
    public void fun(double d)
    {
        System.out.println("Fun one double parameters");
    }
}

class Overloading
{
    public static void main(String Arr[])
    {
        Demo dobj = new Demo();
        dobj.fun();
        dobj.fun(11);
        dobj.fun(11,21);
        dobj.fun(11.21);

    }
}