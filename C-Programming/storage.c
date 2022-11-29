#include<stdio.h>

int A = 10;

void Fun()
{
    auto int B = 20;
    register int D = 20;
    static int E = 20;

    B++;
    D++;
    E++;

    printf("Value of Auto Vriable : %d\n",B);
    printf("Value of Register Vriable : %d\n",D);
    printf("Value of Static Vriable : %d\n",E);

    // printf("Address of Auto Vriable : %d\n",&B);
    // printf("Address of Register Vriable : %d\n",&D);
    // printf("Address of Static Vriable : %d\n",&E);
    

}

int main()
{
    int C = 30;

    printf("First Function Call \n");
    Fun();
    printf("Second Function Call \n");
    Fun();
    printf("Third Function Call \n");
    Fun();

    return 0;
}