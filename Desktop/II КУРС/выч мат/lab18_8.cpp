#include <iostream>
#include <fstream>
#include <math.h>
#include <thread>
#include <iomanip>

template <class T>
T f(T x){
  return atan(x)-(x+1.0)/(x+2.0);
}

template <class T>
T integral(T x){
  return x*atan(x)-x+log(x+2)-log(x*x+1)/2;
}

template <class T>
T integral_ab(T a, T b){
  return integral(b)-integral(a);
}

template <class T>
T integral_Simpson(T a, T b, int n){
//  int n = (nn%2)?nn:(nn+1);
  T res = 0;
  for(int i=0; i<=n-2; i+=2){
    T b1 = a + ((b - a)/n)*i;
    T b2 = a + ((b - a)/n)*(i+1);
    T b3 = a + ((b - a)/n)*(i+2);
    T h = b2 - b1;
    res = res + h*(f(b1)+f(b2)*4.0+f(b3))/3.0;
  }
  return res;
}

template <class T>
void lab18(T a, T b, const std::string& file_name){
  T I = integral_ab(a, b);
std::cout << std::setprecision (15) << I << std::endl; 
  std::ofstream of(file_name);
  for(int n = 2;n<40000; n+=2){
    T Is = integral_Simpson(a, b, n);
    T e = fabs(I - Is);
    of << n << "\t" <<std::setprecision (15)<< e << std::endl;
  }
}

int main(){
  std::thread t1([](){
    lab18<float>(0.0f, 3.0f, "lab18_float.txt");
  });
  
  std::thread t2([](){
    lab18<double>(0.0d, 3.0d, "lab18_double.txt");
  });
  t1.join();
  t2.join();
  return 0;
}
