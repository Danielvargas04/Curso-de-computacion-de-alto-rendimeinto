#include <iostream>
#include <math.h>

using std::cout;
using std::endl;

float suma1(int N)
{
    float suma = 0.0;
    for (int i = 1; i <= N; i++)
    {
        suma += 1.0/i;
    }
    return suma;
}

float suma2(int N)
{
    float suma = 0.0;
    for (int i = N; i >= 1; i--)
    {
        suma += 1.0/i;
    }
    return suma;
}

int main()
{
    float s1 = 0.0, s2 = 0.0;
    float delta;
    cout<<"N "<<"S1 "<<"S2 "<< "delta "<<endl;
    for (int i = 2; i <= 1e6; i+=128)
    {
        s1 = suma1(i);
        s2 = suma2(i);
        delta = suma2(i);
        cout<<i<<" "<<s1<<" "<<s2<<" "<< fabs(1- s1/s2)<<endl;
    }
    return 0;
}