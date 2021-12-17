#include <stdio.h>
#include <stdlib.h>
#include<math.h>

double a=2;
double b=1.8;
double eps= 0.0001;
int s;
double mod;


int main()
{
  double fa = a*a-log(a+0.5)-3*a;
  double fb = b*b-log(b+0.5)-3*b;
  double r=(sqrt(5)-1)/2;
  double c = a+(1-r)*(b-a);
  double fc = c*c-log(c+0.5)-3*c;
  double d = b-(1-r)*(b-a);
  double fd = d*d-log(d+0.5)-3*d;
    do
    {
        if (fc>fd)
        {
          a=c;
          fa=fc;
          c=d;
          fc=fd;
          d = b-(1-r)*(b-a);
          fd = d*d-log(d+0.5)-3*d;
        }
        else
        {
          b=d;
          fb=fd;
          d=c;
          fd=fc;
          c = a+(1-r)*(b-a);
          fc = c*c-log(c+0.5)-3*c;
        }
      mod=fabs(b-a);
      double x=c;
      double fx = x*x-log(x+0.5)-3*x;
      s++;
      printf("\t   x\t\t   f(x)\n");
      printf("------------------\n\n%i min   %e;\t%e\n\n",s ,x ,fx );
      printf("------------------\na=%e\nc=%e\nd=%e\nb=%e\n|b-a|=%e\nf(a)=%e\nf(c)=%e\nf(d)=%e\nf(b)=%e\n",a,c,d,b,mod,fa,fc,fd,fb );
    }

     while(mod>=eps);
    //printf("\n\n\na=%e\nc=%e\nd=%e\nb=%e\n|b-a|=%d\nf(a)=%e\nf(c)=%e\nf(d)=%e\nf(b)=%e\n",a,c,d,b,mod,fa,fc,fd,fb );

  return 0;
}
