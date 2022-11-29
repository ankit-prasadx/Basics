#include<iostream>
using namespace std;

// Class Declaration
class Maths
{
    public:                     // Access Specifier
    int iNo1;                   // Characteristics
    int iNo2;                   // Characteristics

    Maths()                     // Consructor (Default)
    {
        iNo1 = 0;
        iNo2 = 0;
    }
    Maths(int A, int B)         // Constructor (Parameterized)
    {
        iNo1 = A;
        iNo2 = B;
    }

    int Addition()              // Behaviour
    {
        return iNo1 + iNo2;
    }

    int Substraction()          // Behaviour
    {
        return iNo2 - iNo2;
    }

};

int main()
{
    Maths mobj1;

    Maths mobj2(11,10);
    

    return 0;
}