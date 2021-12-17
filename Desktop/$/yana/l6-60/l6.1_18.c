#include<stdio.h>
#include<math.h>
int main()
{
double x0=0.01;
double x;
double e;
double eps= 0.00000001;
double fx;
double fx1;
int i=0;

  x=x0;
  printf("\t\tx1\tdelta\n");
    do
    {
    fx = (x*x-log(x+0.5))-3*x;
    fx1 = 2*x-3-(1/(x+0.5));
    e = (-fx/fx1);
    x = x+e;
    ++i;
    printf ("%i\t%e\t%e\n", i , x , e);
    }
    while (fabs(e)>eps);
    printf ("ответ=%e\n", x );


    x=x0=3;
    printf("\t\tx2\n");
  i=0;
    do
      {
        fx = (x*x-log(x+0.5))-3*x;
        fx1 = 2*x-3-(1/(x+0.5));
        e = (-fx/fx1);
        x = x+e;
        ++i;
        printf ("%i\t%e\t%e\n", i , x , e);

      }
      while (fabs(e)>eps);
      printf ("ответ=%e\n", x );

return 0;
}
