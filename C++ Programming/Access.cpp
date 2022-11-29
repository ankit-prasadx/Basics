#include<iostream>
using namespace std;

class Base
{
    public:
        int i;
    private:
        int j;
    protected:
        int k;        
    public:
        Base()
        {
            i = 10;
            j = 20;
            k = 30;
        }
        void fun()
        {
            cout<<"Value of public i : "<<i<<"\n";
            cout<<"Value of private i : "<<j<<"\n";
            cout<<"Value of protected i : "<<k<<"\n";
        }
};

// class Derived : public Base
// {

// };

int main()
{
    Base bobj;
    // cout<<"Value of public i : "<<bobj.i<<"\n";
    // cout<<"Value of private i : "<<bobj.j<<"\n";
    // cout<<"Value of protected i : "<<bobj.k<<"\n";
    
    bobj.fun();

    return 0;
}