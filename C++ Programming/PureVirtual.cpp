#include<iostream>
using namespace std;

class Circle
{
    public:
        float PI;
        float Radius;
        
        Circle()
        {
            PI = 3.14;
            Radius = 0.0;
        }
        Circle(float A, float B)
        {
            PI = A;
            Radius = B;
        }
        void Display()
        {
            cout<<"Value of Radius is : "<<Radius<<"\n";
        }
        virtual float Area() = 0;
        virtual float Circumference() = 0;
};

class Marvellous : public Circle
{
    public:
        Marvellous() : Circle()
        {
        }
        Marvellous(float X, float Y) : Circle(X,Y)
        {
        }
        float Area()
        {
            float Ans = PI * Radius * Radius;
            return Ans;
        }
        float Circumference()
        {
            float Ans = 0.0;
            Ans = 2 * PI * Radius;
            return Ans;
        }
};
int main()
{
    // Circle cobj;

    Marvellous mobj1;
    Marvellous mobj2(3.14f, 10.89f);

    float fret = 0.0f;

    fret = mobj2.Area();
    cout<<"Area is :"<<fret<<"\n";

    fret = mobj2.Circumference();
    cout<<"Circumference is : "<<fret<<"\n";
    

    return 0;
}