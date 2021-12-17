#include <stdio.h>
#include <stdlib.h>
#include<math.h>

double a=1.0;
double b=3.0;
double eps= 0.00001;
int i;
double mod;


int main()
{
  double fa = a*a - (log(a+0.5)) - 3*a;
  double fb = b*b - (log(b+0.5)) - 3*b;
  double r=(sqrt(5)-1)/2;
  double c = a+(1-r)*(b-a);
  double fc = c*c - (log(c+0.5)) - 3*c;
  double d = b-(1-r)*(b-a);
  double fd = d*d - (log(d+0.5)) - 3*d;
    do
    {
        if (fc>fd)
        {
          a=c;fa=fc;
          c=d;fc=fd;
          d = b-(1-r)*(b-a);
          fd = d*d-log((d+0.5))-3*d;
        }
        else
        {
          b=d; fb=fd;
          d=c; fd=fc;
          c = a+(1-r)*(b-a);
          fc = c*c - (log(c+0.5)) - 3*c;
        }
      mod=fabs(b-a);
      double x=c;
      double fx = x*x -(log(x+0.5)) - 3*x;
      i++;
      printf("\n\n Итерация № %d\n Минимум находится в точке:   (%e; %e)\n",i ,x ,fx );
      printf("\na=%e | c=%e | d=%e | b=%e\n\n|b-a|=%e\n\nf(a)=%e | f(c)=%e | f(d)=%e | f(b)=%e |\n\n",a,c,d,b,mod,fa,fc,fd,fb );
      printf("x=%e\nF(x)=%e\n", x, fx );
    }
     while(mod>=eps);
  return 0;
}
