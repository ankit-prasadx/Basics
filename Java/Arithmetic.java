package Marvellous;

public class Arithmetic
{
    public int iValue1;
    public int iValue2;

    public Arithmetic (int A, int B)
    {
        iValue1 = A;
        iValue2 = B;
    }

    public int Addition()
    {
        return iValue1 + iValue2;
    }
    
    public int Substraction()
    {
        return iValue1 - iValue2;
    }
}