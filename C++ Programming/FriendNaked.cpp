#include<iostream>
using namespace std;

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
    friend void fun();
};

void fun()      // Naked function
{
    Demo dobj;
    cout<<"Value of i :"<<dobj.i<<"\n";
    cout<<"Value of j :"<<dobj.j<<"\n";
    cout<<"Value of k :"<<dobj.k<<"\n";
}

int main()
{
    fun();

    return 0;
}