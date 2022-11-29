#include<iostream>

using namespace std;

class Demo
{
    public:
        int i;
        int j;
        
        // Default Constructor
        Demo()
        {
            int i = 11;
            int j = 21;
        }

        // Parameterized Constructor
        Demo(int x, int y)
        {
            i = x;
            j = y;
        }

};

int main()
{
    Demo dobj1;
    Demo dobj2(10, 20);

    const Demo obj3;
    const Demo obj4(15, 25);


    return 0;
}