#include <iostream>
#include <math.h>

using std::cout;
using std::endl;

bool esprimo(int x)
{
    /*Verifica si un numero x es primo mediante sus divisores*/
    for(int i = 2; i <= sqrt(x); i++)
    {
        if (x%i==0)
        {
            return false;
        }
    }
    return true;
}


int main(){

    for (int i = 10; i < 30; i++)
    {
        /*Toma i y verifica que sea primo para imprimirlo en consola*/
        if (esprimo(i)==true)
        {
            cout<<i<<endl;
        }
    }
    return 0;
}

