
class Maths
{
    public int iNo1;        // Characeristics
    public int iNo2;        // Characeristics

    public Maths()        // Default Constructor
    {
        System.out.println("Inside Default constructor");
    }
    public Maths(int a, int b)  // Parameterized Constructor
    {
        System.out.println("Inside parameterized constructor");
        iNo1 = a;
        iNo2 = b;
    }
    public int Addition()       // Behaviour
    {
        int iAns = 0;
        iAns = iNo1 + iNo2;
        return iAns;
    }
    public int Substraction()       // Behaviour
    {
        int iAns = 0;
        iAns = iNo1 - iNo2;
        return iAns;
    }

}   // End of Maths class

class Demo
{
    public static void main(String arg[])
    {
        System.out.println("Inside Main function");

        Maths mobj1 = new Maths();
        Maths mobj2 = new Maths(10,11);

        int iRet = 0;
        iRet = mobj1.Addition();
        System.out.println("Addition is :"+iRet);
        iRet = mobj2.Addition();
        System.out.println("Addition is :"+iRet);
    }
}