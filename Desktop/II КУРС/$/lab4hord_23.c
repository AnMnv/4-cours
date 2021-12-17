#include<stdio.h>
#include<math.h>

int main()
{
  double c = 0.00000001;
  double a = 0.2;
  double b = 2;
  double y;
  double x;
  double ya = a*a+3-(1/a);
  double yb = b*b+3-(1/b);
  double xpoper;
x=a;
int i=1;
  do
      {
      xpoper=x;
      x=a-((ya*b-ya*a)/(yb-ya));
      y = x*x+3-(1/x);

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
   printf("для методу хорд мені знадобилося28 інерацій\nВідповідь: %f\n\n", x);
  return 0;
}
