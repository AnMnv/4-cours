#include<stdio.h>
#include<math.h>
int main()
{
double x0=0.2;
double x;
double e;
double eps= 1e-5;
double fx;
double fx1;
int i=0;

  x=x0;
  printf("\n\t  X\t\tDelta\n");
    do
    {
    fx = x*x+3-(1/x);
    fx1 = 2*x+(1/(x*x));
    e = (-fx/fx1);
    x = x+e;
    ++i;
    printf ("%i\t%f\t%f\n", i , x , e);
    }
    while (fabs(e)>eps);
    printf ("\nответ= %e\n\n", x );



return 0;
}
