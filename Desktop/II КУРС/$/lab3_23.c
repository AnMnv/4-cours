#include<stdio.h>
#include<math.h>

int main()
{
double y, y1, y2;
double x = -2;
  printf("  X\t\t\t   F\t\t\t  F'\t\t\t  F''\n");
  do
  {
    y = x*x+3-(1/x);
    y1 = 2*x+(1/x*x);
    y2= 2-(2/x*x*x);
    x+=0.3;
    printf("%f\t\t%f\t\t%f\t\t%f\n",x, y, y1, y2);

  }
    while (x<=3);



return 0;
}
