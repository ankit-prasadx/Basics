#include<iostream>

using namespace std;

class Demo
{
    public:
        int i;
        int j;
        const int k;
        const int l;

        // Default Constructor
        Demo() : k(15), l(215)
        {
            int i = 11;
            int j = 12;
        }

        // Parameterized Constructor
        Demo(int a, int b, int c, int d) : k(a), l(b)
        {
            i = c;
            j = d;
        }

};

int main()
{
    Demo dobj1;
    Demo dobj2(11,21,51,101);


    return 0;
}