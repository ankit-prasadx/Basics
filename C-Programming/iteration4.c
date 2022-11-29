#include<stdio.h>

int main()
{

    int arr[4] = {11,21,51,101};
    int iCnt = 0;

    printf("Elements of array are :\n");


    for(iCnt = 0; iCnt <= 3; iCnt++)
    {
    printf("%d\n", arr[iCnt]);
    }

    return 0;
}