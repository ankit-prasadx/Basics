#include<stdio.h>

int Additon(int No1, int No2)
{
    int Ans = 0;

    printf("Inside Addition\n");

    Ans = No1 + No2;

    return Ans;
}

int main()
{
    int A = 11, B = 10, Ret = 0;

    printf("Inside main\n");

    Ret = Additon(A,B);

    printf("Addition is : %d\n",Ret);

    return 0;
}