#include<iostream>
// using namespace std;

namespace
{
    class Demo
    {
        public:
            int i,j;

            void fun()
            {
                std::cout<<"Inside fun of Demo from Unnamed namespace\n";
            }
    };
}

int main()
{
    Demo obj1;
    obj1.fun();

    return 0;
}