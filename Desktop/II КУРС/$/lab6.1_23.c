#include<stdio.h>
#include<math.h>

int main()
{
double x0=0.2;
double x01=0.5;
double x,x1=1;
double e;
double eps = 1e-5;
double fx;
double fpoper;

  fx = x0*x0+3-(1/x0);

      e = x1-x0;
      x=x1;
      printf("\nX\t\t\tDelta\n");
      do
      {

      fpoper = fx;
      fx = x*x+3-(1/x);
      e = (fx/(fpoper-fx))*e;
      x = x+e;
      printf ("\n%f\t\t%f\n",x, e);
      }
      while (fabs(e)>eps);
      printf ("\nответ= %f\t\n", x);


return 0;
}
