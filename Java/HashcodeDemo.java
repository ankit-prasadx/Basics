
class Demo
{
    public int No1;
    public int No2;

    public Demo(int a, int b)
    {
        No1 = a;
        No2 = b;
    }
}

class HashcodeDemo
{
    public static void main (String Q[])
    {
        Demo obj = new Demo(10,11);

        System.out.println("Hashcode of the obj is : "+obj.hashCode());
    }
}