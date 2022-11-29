#include<stdio.h>

int main()
{
    int iNo1 = 0;
    int iNo2 = 0;
    int iTemp = 0;

    printf("Enter first number :\t");
    scanf("%d",&iNo1);
    printf("Enter second number :\t");
    scanf("%d",&iNo2);

    printf("The Numbers before Swap are  %d  &  %d\n",iNo1,iNo2);

    iTemp = iNo1;
    iNo1 = iNo2;
    iNo2 = iTemp;

    printf("The Numbers after Swap are  %d  &  %d\n",iNo1,iNo2);

    return 0;
}