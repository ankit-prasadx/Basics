
class A
{
    public A()
    {
        System.out.println("inside A construcor");
    }
}

class B extends A
{
    public B()
    {
        System.out.println("inside B construcor");
    }
}

class C extends A
{
    public C()
    {
        System.out.println("inside C construcor");
    }
}


class Hierarchal
{
    public static void main(String p[])
    {
        B bobj = new B();
        C cobj = new C();
    }
}