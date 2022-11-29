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
            cout<<"Inside fun of Base\n";
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

class DerivedX : public Derived
{
    public:
        int i;
        int j;

        DerivedX()
        {
            cout<<"Inside DerivedX Constructor\n";
        }
        ~DerivedX()
        {
            cout<<"Inside DerivedX Destructor\n";
        }
        void sun()
        {
            cout<<"Inside sun of DerivedX\n";
        }

};

int main()
{
    // cout<<"Size of Base : "<<sizeof(Base)<<endl;
    // cout<<"Size of Derived : "<<sizeof(Derived)<<endl;
    // cout<<"Size of DerivedX : "<<sizeof(DerivedX)<<endl;

    // DerivedX dobj;

    // dobj.fun();
    // dobj.gun();
    // dobj.sun();

    DerivedX * ptr = NULL;

    ptr = new DerivedX;

    cout<<"Size of Object is "<<sizeof(*ptr)<<"\n";

    ptr->fun();
    ptr->gun();
    ptr->sun();

    delete ptr;

    return 0;
}