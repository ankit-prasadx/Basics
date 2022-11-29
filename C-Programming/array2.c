#include<stdio.h>

int main()
{
    int arr[4] = {10,20};
    int brr[4];

    printf("%d\t",arr[0]);
    printf("%d\t",arr[1]);
    printf("%d\t",arr[2]);
    printf("%d\n",arr[3]);

    
    brr[0] = 10;
    brr[1] = 20;

    printf("%d\t",brr[0]);
    printf("%d\t",brr[1]);
    printf("%d\t",brr[2]);
    printf("%d\n",brr[3]);
    
    return 0;
}