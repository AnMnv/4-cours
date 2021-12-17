#include<stdio.h>
#include<math.h>

int main()
{
  double c = 0.00000001;
  double a = 1;
  double b = 0.2;
  double y;
  double x;
  double ya = cosh(x)-4*a*a;
  double yb = cosh(x)-4*b*b;
  double xpoper;
  printf ("\n Результат отриманий методом хорд:\n");
x=a;
int i=1;
  do
      {
      xpoper=x;
      x=a-((ya*b-ya*a)/(yb-ya));
      y = cosh(x)-4*x*x;

      if ((ya>0 && y>0)||(ya<0 && y<0))
      {
      a=x;
      ya=y;
      }
      else
      {
      b=x;
      yb=y;
      }
      printf("%d\t%f\n", i++, x);
      }
   while(fabs(xpoper-x)>=c);
   printf("%e\n", x);
  return 0;
}
