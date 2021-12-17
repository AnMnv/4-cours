#include<stdio.h>
#include<math.h>
int main()
{
double x0=-1;
double x;
double e;
double eps= 0.00000001;
double fx;
double fx1;
int i=0;
printf ("Метод Ньютона-Рафсона (дотичних): \n");
  x=x0;
  printf("\t\tx1\tdelta\n");
    do
    {
    fx = cosh(x)-4*x*x;
    fx1 = sinh(x)-8*x;
    e = (-fx/fx1);
    x = x+e;
    ++i;
    printf ("%i\t%e\t%e\n", i , x , e);
    }
    while (fabs(e)>eps);
    printf ("Корінь=%e\n", x );


    x=x0=0.4;
    printf("\t\tx2\n");
  i=0;
    do
      {
        fx = cosh(x)-4*x*x;
        fx1 = sinh(x)-8*x;
        e = (-fx/fx1);
        x = x+e;
        ++i;
        printf ("%i\t%e\t%e\n", i , x , e);

      }
      while (fabs(e)>eps);
      printf ("Корінь=%e\n", x );



return 0;
}
