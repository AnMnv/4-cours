#include<stdio.h>
#include<math.h>

int main()
{
double c = 0.00000001;
double a = 0.2;
double b = 2;
double x;
double y1 = a*a+3-(1/a);
double y;
double e;
int i=0;
double e1;
printf("\n\ni\t\te\t\te1\t\tx\t     proverka: e/x=\n");
double proverka;
  do
  {
      x = a + (b-a)/2;
      y = x*x+3-(1/x);
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
      printf ("%d\t\t%f\t%f", i, e, x);
      printf ("\t%f", e1);
      proverka=e/e1;
      printf ("\t%f\n", proverka);
  }
while (fabs(e)>=c);
x = a + (b-a)/2;
printf ("\n\n\n\nВидповидь: %f\t\t\n\n", x );
return 0;
}
