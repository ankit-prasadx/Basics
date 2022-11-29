// abstract class is a class which contains 0 or more abstract method in it
abstract class Arithmetic
{
    public int Addition(int No1, int No2)
    {
        return No1 + No2;
    }
    public abstract int Substraction(int No1, int No2);
    // virtual int Substraction(int No1, int No2) = 0;
}

class Marvellous extends Arithmetic
{
    public int Substraction(int No1, int No2)
    {
        return No1 - No2;
    }
}


class AbstractDemo
{
    public static void main(String f[])
    {
        // Arithmetic aobj = new Arithmetic();  // NA
        Arithmetic aobj = new Marvellous();     // Allowed
        Marvellous mboj = new Marvellous();
        int iRet = 0;
        iRet = mboj.Addition(11,10);
        System.out.println("Addition is : "+iRet);
        iRet = mboj.Substraction(11,10);
        System.out.println("Substraction is : "+iRet);
    }
}