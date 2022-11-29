/*
    Steps to develop the application
    Step 1: Understand the problem statement
    Step 2: Write the algorithm
    Step 3: Decide the programming language (C/C++/Java/Python)
    Step 4: Write the program
    Step 5: Test the program
*/

// Accept N numbers from the addition

// Input
// Value of N = 5
// Vaues : 10 20 30 40 50

// Output
// Addition is : 150

// Algorithm
/*
    START
        Accept the number of elements from user
        Allocate he memory to store the numbers
        Accept the numbers from user
        Perform addition of all numbers
        Display the addition
    END
*/

#include <stdio.h>           // For printf & scanf
#include <stdlib.h>          // For malloc & free

/////////////////////////////////////////////////////
//
//  Application Name :  Addition of N numbers
//  Input :     N numbers
//  Output :    Addition
//  Author :    Ankit Ramashish Prasad
//  Date :      18-September-2022
//
////////////////////////////////////////////////////

int main()
{
    int *Arr = NULL;            // Pointer to hold address of array
    int iSize = 0;              // Variable to hold size of array
    register int i = 0;         // Loop Counter
    int iSum = 0;               // To hold the addition

    printf("Please enter how many elements you want ?\n");
    scanf("%d",&iSize);

    // Allocate the memory
    Arr = (int *)malloc(iSize * sizeof(int));
    printf("Memory allocation is Successfull\n");

    printf("Please enter the elements\n");

    for(i = 0; i < iSize; i++)
    {
        scanf("%d",&Arr[i]);
    }

    // Perform Addition
    for(i = 0; i < iSize; i++)
    {
        iSum = iSum + Arr[i];
    }

    printf("Addition is : %d\n",iSum);
    
    free(Arr);
    printf("Memory Deallocated\n");

    return 0;
}