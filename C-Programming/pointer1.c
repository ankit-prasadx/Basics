#include<stdio.h>

int main()
{

    int iNo = 11;
    
    int *iPtr = &iNo;


    printf("Value of iNo is :%d\n",iNo);
    printf("Value of iPtr is :%d\n",iPtr);
    // printf("Value of iPtr is :%p\n",iPtr);

    printf("Size of iNo is :%d\n",sizeof(iNo));
    printf("Size of iPtr is :%d\n",sizeof(iPtr));

    // printf("Address of iNo is :%p\n",&iNo);
    printf("Address of iNo is :%d\n",&iNo);
    printf("Address of Ptr is :%d\n",&iPtr);
    // printf("Address of iPtr is :%p\n",&iPtr);



    return 0;
}