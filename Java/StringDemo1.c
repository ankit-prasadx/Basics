#include<stdio.h>
#include<string.h>

int main()
{
    char Arr[10] = "Hello";
    char * Ptr = Arr;
    char * lPtr = &Arr;
    lPtr++;
    printf("%d\n",lPtr);

    int iCnt = 0;

    printf("%d\n",Ptr);
    printf("%d\n",Arr);

    while(*Ptr != '\0')
    {
        iCnt++;
        Ptr++;
    }
    printf("Length of string is : %d\n",iCnt);

    return 0;
}