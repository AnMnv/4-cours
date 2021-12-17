#include <stdio.h>
#include <stdlib.h>
#include<math.h>

double a=2;
double b=5;
double eps= 0.00000001;
int s;
double mod;


int main()
{


  double fa = atan(a) + 0.1*a*a - 0.8*a;
  double fb = atan(b) + 0.1*b*b - 0.8*b;
  double r=(sqrt(5)-1)/2;
  double c = a+(1-r)*(b-a);
  double fc = atan(c) + 0.1*c*c - 0.8*c;
  double d = b-(1-r)*(b-a);
  double fd = atan(d) + 0.1*d*d - 0.8*d;
    do
    {
        if (fc>fd)
        {
          a=c;
          fa=fc;
          c=d;
          fc=fd;
          d = b-(1-r)*(b-a);
          fd = atan(d) + 0.1*d*d - 0.8*d;
        }
        else
        {
          b=d;
          fb=fd;
          d=c;
          fd=fc;
          c = a+(1-r)*(b-a);
          fc = atan(c) + 0.1*c*c - 0.8*c;
        }
      mod=fabs(b-a);
      double x=c;
      double fx = atan(x) + 0.1*x*x - 0.8*x;
      s++;
      printf("\t   x\t\t   f(x)\n");
      printf("------------------\n\n%i min   %e;\t%e\n\n",s ,x ,fx );
      printf("------------------\na=%e\nc=%e\nd=%e\nb=%e\n|b-a|=%e\nf(a)=%e\nf(c)=%e\nf(d)=%e\nf(b)=%e\n",a,c,d,b,mod,fa,fc,fd,fb );
    }

     while(mod>=eps);
  return 0;
}
