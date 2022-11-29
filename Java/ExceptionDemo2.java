import java.util.*;

class ExceptionDemo2
{
    public static void main(String R[])
    {
        Scanner sobj = new Scanner(System.in);

        // int Arr[4] = {10,20,30,40};
        int Arr[] = {10,20,30,40};

        System.out.println("Enter the index of array");
        int iIndex = sobj.nextInt();

        System.out.println("Data at specified index is : "+Arr[iIndex]);

    }
}