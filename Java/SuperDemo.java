
class Base
{
    public int A,B;
    // public Base()
    // {
    //     this.A = 0;
    //     this.B = 0;
    // }
    public Base(int No1, int No2)
    {
        this.A = No1;
        this.B = No2;
    }
    public void Fun()
    {
        System.out.println("Inside Base Fun");
        System.out.println("Value of A from fun method is :"+this.A);

    }
}

class Derived extends Base
{
    public int X,Y;
    public Derived(int i, int j, int k, int l)
    {
        super(k,l);     // 1st use case
        this.X = i;
        this.Y = j;
    }
    public void gun()
    {
        System.out.println("Value of A from Gun method is :"+super.A);      // 2nd Usecase
        super.Fun();        // 3rd Usecase
    }
}

class SuperDemo
{
    public static void main(String q[])
    {
        Derived dobj = new Derived(11,21,51,101);
        dobj.gun();
    }
}