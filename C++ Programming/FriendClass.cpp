#include<iostream>
using namespace std;

class Marvellous
{
    public:
        void gun();     // Naked Function
        void fun();     // Naked Function
};

class Demo
{
    public:
        int i;
    private:
        int j;
    protected:
        int k;
    public:
        Demo()
        {
            i = 10;
            j = 20;
            k = 30;
        }
    friend class Marvellous;
};

void Marvellous::fun()      // Member Function
{
    Demo dobj;
    cout<<"Value of i :"<<dobj.i<<"\n";
    cout<<"Value of j :"<<dobj.j<<"\n";
    cout<<"Value of k :"<<dobj.k<<"\n";
}
void Marvellous::gun()      // Member Function
{
    Demo dobj;
    cout<<"Value of i :"<<dobj.i<<"\n";
    cout<<"Value of j :"<<dobj.j<<"\n";
    cout<<"Value of k :"<<dobj.k<<"\n";
}

int main()
{
    Marvellous mobj;

    mobj.fun();
    mobj.gun();

    return 0;
}