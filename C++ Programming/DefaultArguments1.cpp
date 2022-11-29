#include<iostream>
using namespace std;

class Demo
{
    public:
        int A,B;

        Demo()
        {
            A = 0;
            B = 0;
        }

        Demo(int i)
        {
            A = i;
            B = 0;
        }

        Demo(int i, int j)
        {
            A = i;
            B = j;
        }
};

int main()
{
    Demo dobj1;
    Demo dobj2(11);
    Demo dobj3(11,21);

    return 0;
}