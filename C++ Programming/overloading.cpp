#include<iostream>
using namespace std;

class Overloading
{
    public:
        // Add@2ii
        int Add(int a, int b)                   // 1000
        {
            cout<<"Addition of 2 integers\n";
            return a + b;
        }
        // Add@2ff
        float Add(float a, float b)             // 2000
        {
            cout<<"Addition of 2 floats\n";
            return a + b;
        }
        // Add@2dd
        double Add(double a, double b)          // 3000
        {
            cout<<"Addition of 2 doubles\n";
            return a + b;
        }
        // Add@3iii
        int Add(int a, int b, int c)            // 4000
        {
            cout<<"Addition of 3 integers\n";
            return a + b + c;
        }

        void fun(int a, float b)
        {

        }
        void fun(float b, int a)
        {

        }
};
int main()
{
    Overloading obj;

    int i;
    float f;
    double d;

    i = obj.Add(11,21);                 // CALL 1000
    cout<<i<<"\n";
    i = obj.Add(11,21,51);              // CALL 4000
    cout<<i<<"\n";
    f = obj.Add(10.2f,19.55f);          // CALL 2000
    cout<<f<<"\n";
    d = obj.Add(10.254,55.654);         // CALL 3000
    cout<<d<<"\n";

    //obj.fun(10, 12.251);



    return 0;
}