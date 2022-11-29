
class Loops
{
    public static void main(String arg[])
    {
        int Arr1[] = {10,20,30,40};
        int iCnt = 0;

        System.out.println("Traversal of Array using for loop ");
        for (iCnt = 0; iCnt < Arr1.length; iCnt++)      // Same in C,C++,Java
        {
            System.out.println(Arr1[iCnt]);
        }

        System.out.println("Traversal of Array using While loop ");
        iCnt = 0;
        while (iCnt < Arr1.length)      // Same in C,C++,Java
        {
            System.out.println(Arr1[iCnt]);
            iCnt++;
        }

        System.out.println("Traversal of Array using do-While loop ");
        iCnt = 0;
        do      // Same in C,C++,Java
        {
            System.out.println(Arr1[iCnt]);
            iCnt++;
        }while (iCnt < Arr1.length);

        System.out.println("Traversal of Array using for-each loop ");
        for(int iNo : Arr1)     // Only in Java & Python
        {
            System.out.println(iNo);
        }

    }
}