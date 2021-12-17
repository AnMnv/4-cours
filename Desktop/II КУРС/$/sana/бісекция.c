#include<stdio.h>
#include<math.h>

int main()
{
double c = 0.00000001;
double a = 0.2;
double b = 2;
double x;
double y1 = cosh(x)-4*x*x;
double y;
double e;
int i=0;
double e1;
printf ("\n Mетод бісекції:\n");
printf("\n\n№ітерації\te\t\te1\t\tx\t     Перевірка: e/x=\n");
double proverka;
  do
  {
      x = a + (b-a)/2;
      y = cosh(x)-4*x*x;
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
printf ("\n\n\n\nВідповідь: %f\t\t\n\n", x );
return 0;
}
