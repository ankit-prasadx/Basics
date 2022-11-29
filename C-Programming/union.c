#include<stdio.h>

struct Demo
{
    int i;
    float f;
    double d;
};

union Hello
{
    int i;
    float f;
    double d;
};

int main()
{
    struct Demo dobj;
    union Hello hobj;    

    printf("Size of the structure is : %d\n", sizeof(dobj));
    printf("Size of the union is : %d\n", sizeof(hobj));

    dobj.i  = 11;
    dobj.f = 90.5;
    dobj.d = 9.258;

    hobj.d = 2.548;

    printf("%lf\n",hobj.d);




    return 0;
}