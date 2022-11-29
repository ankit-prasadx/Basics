// SAME as constant characteristics of class from C++

class Demo
{
    public int No1;
    public final int No2 = 11;      // const int No2 = 11;
    public final int No3;           // const int No3;

    public Demo()       // Demo () : No2(11), No2(21)
    {
        No1 = 0;
        No3 = 23;       // NA in C++
    }
}

class Final1
{
    public static void main(String q[])
    {
        final int = 51;     // const int i = 51;
        Demo obj = new Demo();
        obj.No1++;
        // obj.No2++;
        // obj.No3++;
    }
}