#include <stdio.h>
#include <math.h>

#define DOUBLE double

DOUBLE my_func(DOUBLE x){
  return 10.0*x*x*exp(-x)-3.0*x;
}

DOUBLE my_func_integral(DOUBLE x){
  return 10.0*(-(x*x)-2.0*x-2.0)*exp(-x)-(3.0*x*x)/2.0;
}

DOUBLE my_func_integral_ab(DOUBLE a, DOUBLE b){
  return my_func_integral(b)-my_func_integral(a);
}

DOUBLE near_integral(DOUBLE a, DOUBLE b, int n){
  DOUBLE res = 0;
  for(int i=0; i<=n-1; ++i){
    DOUBLE beg = a + ((b - a)/n)*i;
    DOUBLE end = a + ((b - a)/n)*(i+1);
    DOUBLE h = end - beg;
    res = res + h/2*(my_func(beg)+my_func(end));
  }
  return res;
}

int main()
{
  DOUBLE a = -1.0;
  DOUBLE b = 2.0;
  printf("\n\nМоя функция:----------------------------->  10x^2exp(-x)-3x\n");
  DOUBLE I = my_func_integral_ab(a, b);
  printf("Результат интегрирования моей функции---->   %e\n", I);

  int n = 1;
  for(;n<4000; n+=1){
    DOUBLE It = near_integral(a, b, n);
    DOUBLE e = It - I;
    printf("%d\t%e\t%e\n", n, e, It);
  }

/*  printf("\n\nМоя функция:----------------------------->  10x^2exp(-x)-3x\n");
    DOUBLE a = (10*(-(x*x)-2*x-2)*exp(-x)-(3*x*x)/2) - (10*(-(c*c)-2*c-2)*exp(-c)-(3*c*c)/2);
    printf("Результат интегрирования моей функции---->   %e\n", a);
     DOUBLE h = (x – c)/n;
    //DOUBLE it = ;
    //DOUBLE e = i-it;
*/
  return 0;
}
