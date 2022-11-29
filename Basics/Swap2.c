#include<stdio.h>

int main()
{
    int iNo1 = 0;
    int iNo2 = 0;

    printf("Enter First Number : ");
    scanf("%d", &iNo1);
    
    printf("Enter Second Number : ");
    scanf("%d", &iNo2);

    printf("Numbers before swap %d and %d", iNo1,iNo2);

    iNo2 = iNo1 + iNo2;

    iNo1 = iNo2 - iNo1;

    iNo2 = iNo2 - iNo1;

    printf("Numbers after swap %d and %d", iNo1,iNo2);

    return 0;
}