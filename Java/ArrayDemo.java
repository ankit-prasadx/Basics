class ArrayDemo
{
    public static void main (String arr[])
    {
        // Ways of creating Single Dimensional Array

        // Explicit size is not allowed in java
        // int Arr2[4] = {10,20,30,40};

        // Allowed in java
        int Arr1[] = {10,20,30,40};

        // Dynamic Memory Allocation
        int Arr3[] = new int[4];
        // Member Initialiazation List
        Arr3[0] = 10;
        Arr3[1] = 20;
        Arr3[2] = 30;
        Arr3[3] = 40;

        // Dynamic memory allocation with Initialisation list
        int Arr4[4] = new int[4] {10,20,30,40};
    }
}