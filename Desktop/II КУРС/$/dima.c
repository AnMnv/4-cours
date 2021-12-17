#include<stdio.h>
#include<math.h>

int main()
{
double c = 0.00000001;
double a = 0.5;
double b = 0;
double x;
double y1 = cos(a)+cos(3*a);
double y;
double e;
int i=0;
double e1;
printf("i\t\te\t\tx\t\te1\t\tproverka\n");
double proverka;
  do
  {
      x = a + (b-a)/2;
      y = cos(x)+cos(3*x);
      if ((y1>0 && y>0)||(y1<0 && y<0))
      {
         a=x;
      }
      else
      {
         b=x;
      }
      e = fabs(b-a);
      i++;
      e1=0.5*e;
      printf ("%d\t\t%e\t%e", i, e, x);
      printf ("\t%e", e1);
      proverka=e/e1;
      printf ("\t%e\n", proverka);
  }
while (fabs(e)>=c);
x = a + (b-a)/2;
printf ("\n\n\n\n%e\t\t", x );
return 0;
}
