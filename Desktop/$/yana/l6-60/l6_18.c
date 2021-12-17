#include<stdio.h>
#include<math.h>

int main()
{
double x0=0.01;
double x01=3;
double x02=4;
double x1=0;
double x;
double e;
double eps = 0.00000001;
double fx;
double fpoper;

  fx = (x0*x0-log(x0+0.5))-3*x0;

      e = x1-x0;
      x=x1;
      printf("x1\t\t\tdelta\n");
      do
      {

      fpoper = fx;
      fx = (x*x-log(x+0.5))-3*x;
      e = (fx/(fpoper-fx))*e;
      x = x+e;
      printf ("%e\t\t%e\n",x, e);
      }
      while (fabs(e)>eps);
      printf ("ответ=%e\t\n", x);

fx = (x1*x1-log(x1+0.5))-3*x1;
      e = x1-x0;

      x=x1=3;
      printf("x2\n");
      do
      {
      fpoper = fx;
      fx = (x*x-log(x+0.5))-3*x;
      e = (fx/(fpoper-fx))*e;
      x = x+e;
      printf ("%e\t\t%e\n",x, e);
      }
      while (fabs(e)>eps);
      printf ("ответ=%e\n", x );

return 0;
}
