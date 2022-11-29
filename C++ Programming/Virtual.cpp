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
        virtual void gun()             // Function defination
        {
            cout<<"Base gun\n";
      
        }
        virtual void sun()                  // Function defination
        {
            cout<<"Base sun\n";
        }

};

class Derived : public Base
{
    public:
        int X,Y;

        void gun()                  // Function Re-defination
        {
            cout<<"Derived gun\n";
        }
        void run()                  // Function defination  
        {
            cout<<"Derived run\n";
        }
        virtual void mun()         // Function defination  
        {
            cout<<"Derived mun\n";
        }

};

int main()
{
    // cout<<"Size of Base class : "<<sizeof(Base)<<"\n";
    // cout<<"Size of Derived class : "<<sizeof(Derived)<<"\n";

    Base *bp = NULL;
    Derived dobj;
    bp = & dobj;    // Upcasting

    bp->fun();
    bp->gun();
    bp->sun();

    return 0;
}