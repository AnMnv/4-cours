#include<stdio.h>
#include<math.h>

int main()
{
double x0=0;
double x;
double xpoper;
double e;
double eps= 0.00000000001;

  x=x0;
  printf("x\n");
    do
    {
    xpoper=x;
    printf("\t%f\n",x);
    x = 1/(x*x+3);
    e = x-xpoper;
    }
    while (fabs(e)>eps);
    printf ("Відповідь: %f\n", x );




return 0;
}
