#include<iostream>
using namespace std;

class Demo
{
    public:
        int A,B;
        // Optimized Constructor
        Demo(int i = 0, int j = 0)
        {
            A = i;
            B = j;
        }
};

int main()
{
    Demo dobj1;             // i = 0    j = 0
    Demo dobj2(11);         // i = 11   j = 0
    Demo dobj3(11,21);      // i = 11   j = 21

    return 0;
}