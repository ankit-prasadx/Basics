#include<stdio.h>

int main()
{
    int iNo1 = 0;
    int iNo2 = 0;
    int iSum = 0;
    
    printf("Enter First number :\t");
    scanf("%d",&iNo1);
    printf("Enter Second number :\t");
    scanf("%d",&iNo2);

    iSum = iNo1 + iNo2;

    printf("The sum is : %d\n",iSum);

    return 0;
}