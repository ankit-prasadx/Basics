
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

class C extends B
{
    public C()
    {
        System.out.println("inside C construcor");
    }
}


class Multilevel
{
    public static void main(String p[])
    {
        C cobj = new C();
    }
}