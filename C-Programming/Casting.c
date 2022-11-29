#include<stdio.h>
#include<stdlib.h>


int main()
{
    char * cptr = NULL;
    int * iptr = NULL;
    int iVar = 547;

    cptr = &iVar;
    iptr = &iVar;

    printf("Value of iVar is :%d\n",iVar);
    printf("Value of *cptr is : %d\n",*cptr);
    printf("Value of cptr is :%d\n",cptr);

    return 0;
}
