#include<stdio.h>
#include<math.h>

int main()
{
double x0=0.2;
double x01=0.3;

double x1=0;
double x;
double e;
double eps = 0.00000001;
double fx;
double fpoper;
printf ("Метод січних:\n");
  fx = cosh(x)-4*x0*x0;

      e = x1-x0;
      x=x1;
      printf("x1\t\t\tdelta\n");
      do
      {

      fpoper = fx;
      fx = cosh(x)-4*x*x;
      e = (fx/(fpoper-fx))*e;
      x = x+e;
      printf ("%e\t\t%e\n",x, e);
      }
      while (fabs(e)>eps);
      printf ("Корінь=%e\t\n", x);

fx = cosh(x)-4*x01*x01;
      e = x1-x0;

      x=x1=0.3;
      printf("x2\n");
      do
      {
      fpoper = fx;
      fx = cosh(x)-4*x*x;
      e = (fx/(fpoper-fx))*e;
      x = x+e;
      printf ("%e\t\t%e\n",x, e);
      }
      while (fabs(e)>eps);
      printf ("Корінь=%e\n", x );


return 0;
}
