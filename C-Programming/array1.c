#include<stdio.h>

int main()
{

    // First way to initialise the array
    int arr [5] = {1,2,3,4,5};

    // Seccond way to initialize the array
    int brr [] = {1,2,3,4,5,6,7,8,9};

    // Third way to initialize the array
    int crr[4];
    crr[0] = 1;
    crr[1] = 2;
    crr[2] = 3;
    crr[3] = 4;

    printf("Size of array is :%d\n", sizeof(arr));
    printf("Size of array is :%d\n", sizeof(brr));
    printf("Size of array is :%d\n", sizeof(crr));
    return 0;
}