#include<stdio.h>
#include<math.h>

int main()
{
  double c = 0.00000001;
  double a = 1.9;
  double b = 0;
  double y;
  double x;
  double ya = cos(a)+cos(3*a);
  double yb = cos(b)+cos(3*b);
  double xpoper;
x=a;
int i=1;
  do
      {
      xpoper=x;
      x=a-((ya*b-ya*a)/(yb-ya));
      y = cos(x)+cos(3*x);

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
