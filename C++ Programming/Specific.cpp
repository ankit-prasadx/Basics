#include<iostream>
using namespace std;

int Addi(int i, int j)
{
    int Ans = 0;
    Ans = i + j;
    return Ans;
}

float Addf(float i, float j)
{
    float Ans = 0;
    Ans = i + j;
    return Ans;
}

int main()
{
    int a = 10, b = 11, iRet = 0;
    float x = 90.1f, y = 67.8f, fRet = 0.0f;

    iRet = Addi(a,b);
    cout<<"Addition of integers : "<<iRet<<"\n";
    fRet = Addf(x,y);
    cout<<"Addiion of floats : "<<fRet<<"\n";


    return 0;
}