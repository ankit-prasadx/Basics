#include<stdio.h>

// typedef JUNA_NAW  NAVIN_NAW

typedef int INTEGER;
typedef unsigned long int ULONG;

struct demo
{
    int a;
    int b;
};

typedef struct demo DEMO;

typedef struct demo * PDEMO;

int main()
{
    INTEGER i = 10;         // int i =10;
    ULONG j = 21;           // unsigned long int j = 21;
    DEMO dobj;              // struct Demo dobj;
    PDEMO ptr = &dobj;      // struct Demo * ptr = &dobj
    
    return 0;
}