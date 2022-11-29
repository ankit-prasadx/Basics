#include<iostream>
using namespace std;

class Base
{
    public:
        int A;
        int B;

        Base()
        {
            cout<<"Inside Base Constructor\n";
        }
        ~Base()
        {
            cout<<"Inside Base Destructor\n";
        }

        void fun()
        {
            cout<<"Inside Base of fun\n";
        }

};

class Derived : public Base
{
    public:
        int X;
        int Y;

        Derived()
        {
            cout<<"Inside Derived Constructor\n";
        }

        ~Derived()
        {
            cout<<"Inside Derived Destructor\n";
        }
        void gun()
        {
            cout<<"Inside gun of Derived\n";
        }

};

int main()
{
    Derived * ptr = NULL;

    ptr = new Derived;

    cout<<"Size of Object is "<<sizeof(*ptr)<<"\n";

    ptr->fun();
    ptr->gun();

    delete ptr;

    return 0;
}