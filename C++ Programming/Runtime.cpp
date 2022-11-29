#include<iostream>
using namespace std;

class Base
{
    public:                         // Access Specifier 
        int A,B;

        void fun()                  // Function defination
        {
            cout<<"Base fun\n";
        }
        void gun(int i)             // Function defination
        {
            cout<<"Base gun with one integer\n";
        }
        void gun(int i, int j)      // Overloaded function defination
        {
            cout<<"Base gun with two integers\n";
        }

};

class Derived : public Base
{
    public:
        int X,Y;

        void sun()                  // Function defination
        {
            cout<<"Derived sun\n";
        }
        void fun()                  // Function Re-defination  
        {
            cout<<"Derived fun\n";
        }

};

int main()
{
    Derived dobj;

    dobj.Base::fun();
    dobj.gun(11);
    dobj.gun(11,21);
    dobj.sun();

    return 0;
}