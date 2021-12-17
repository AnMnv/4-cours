#include <stdio.h>
#include <stdlib.h>
#include<math.h>

double a=0;
double b=6;
double eps= 0.00001;
int i;
double mod;


int main()
{
  double fa = cosh(a) -4*a*a;
  double fb = cosh(b)- 4*b*b;
  double r=(sqrt(5)-1)/2;
  double c = a+(1-r)*(b-a);
  double fc = cosh(c)- 4*c*c;
  double d = b-(1-r)*(b-a);
  double fd = cosh(d)- 4*d*d;
    do
    {
        if (fc>fd)
        {
          a=c;fa=fc;
          c=d;fc=fd;
          d = b-(1-r)*(b-a);
          fd = cosh(d)- 4*d*d;
        }
        else
        {
          b=d; fb=fd;
          d=c; fd=fc;
          c = a+(1-r)*(b-a);
          fc = cosh(c) - 4*c*c;
        }
      mod=fabs(b-a);
      double x=c;
      double fx = cosh(x)- 4*x*x;
      i++;
      printf("\n\n Итерация номер %d\n Минимум находится в точке:   (%e; %e)\n",i ,x ,fx );
      printf("\na=%e | c=%e | d=%e | b=%e\n\n|b-a|=%e\n\nf(a)=%e | f(c)=%e | f(d)=%e | f(b)=%e\n\n",a,c,d,b,mod,fa,fc,fd,fb );
      printf("x=%e\nF(x)=%e\n", x, fx );
    }
     while(mod>=eps);
  return 0;
}
