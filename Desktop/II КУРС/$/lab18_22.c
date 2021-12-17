#include <stdio.h>
#include <math.h>

#define DOUBLE float

DOUBLE fx(DOUBLE x)
{
  return 2.0*sinh(x) - x*x;
}
DOUBLE integral(DOUBLE x)
{
  return (6.0*cosh(2.0)-14.0)/3.0;
}
DOUBLE integral_ab(DOUBLE a, DOUBLE b)
{
  return integral(b)-integral(a);
}
DOUBLE pribluzno(DOUBLE a, DOUBLE b, int n){
  DOUBLE res = 0;
  for(int i=0; i<=n-1; ++i)
  {
    DOUBLE nachalo = a + ((b - a)/n)*i;
    DOUBLE konetz = a + ((b - a)/n)*(i+1);
    DOUBLE delta = konetz - nachalo;
    res = res + delta/2*(fx(nachalo)+fx(konetz));
  }
  return res;
}
int main()
{
  DOUBLE a = 0;
  DOUBLE b = 2.0;
//   printf("\n\n  f (x) = 2sh(x) – x^2\n");
  DOUBLE I = integral_ab(a, b);
  //printf("Результат интегрирования моей функции---->   %e\n", I);

  int n = 0;
  for(n = 0 ;n<200; n+=1)
  {
    DOUBLE It = pribluzno(a, b, n);
    DOUBLE e = It - I;
    printf("%d %f\n", n, e);
  }
  return 0;
}
