#include<stdio.h>

int main()
{
    char c = 'A';
    int i = 11;
    float f = 9.36;
    double d = 89.898989;

    char *cp = &c;
    int *ip = &i;
    float *fp = &f;
    double *dp = &d;

    void *vp = &c;

    printf("Value of char : %c\n",c);
    printf("Address of char : %p\n",&c);
    printf("Value inside cp  : %p\n",cp);
    printf("Data refer by cp: %c\n",*cp);
    printf("Size of char : %d\n",sizeof(c));
    printf("Size of cp : %d\n",sizeof(cp));    

    printf("Data refer by vp: %c\n",*(char *)vp);

    return 0;
}