#include<iostream>
using namespace std;
class Demo
{
    public:                 // access specifier
        int i;              // instance variable
        int j;              // instance variable
        static int k;       // class variable
        static int l;       // class variable
    
    Demo()                  // Default Constructor
    {
        i = 0;
        j = 0;
    }    

    Demo(int a, int b)      // Parameterized Constructor
    {
        i = a;
        j = b;
    }    

    void fun()              // instance method
    {
        // static variables + non-static
        cout<<"Inside non static method \n";
        cout<<"Value of i : "<<this->i<<"\n";
        cout<<"Value of j : "<<this->j<<"\n";
        cout<<"Value of k : "<<k<<"\n";
        cout<<"Value of l : "<<l<<"\n";
    }

    static void gun()       // class method
    {
        // static variables only

    }

};
// Load time variables
int Demo::k = 0;
int Demo::l = 0;

int main()
{
    cout<<"Value of k : "<<Demo::k<<"\n";
    cout<<"Value of l : "<<Demo::l<<"\n";

    Demo::gun();

    Demo dobj1(10,11); // object or instance
    Demo dobj2(20,21); // object or instance

    cout<<"Value of i in dobj1 : "<<dobj1.i<<"\n";
    cout<<"Value of j in dobj1 : "<<dobj1.j<<"\n";
    
    cout<<"Value of i in dobj2 : "<<dobj2.i<<"\n";
    cout<<"Value of j in dobj2 : "<<dobj2.j<<"\n";
    
    // cout<<sizeof(dobj1);



    return 0;
}

// size of object is summation of sizes of its non-static charcteristics
// sizeof(dobj) = sizeof(i) + sizeof(j);
// sizeof(dobj) = 4 + 4;
// sizeof(dobj) = 8;
