#include <iostream>
#include<cmath>
#include <fstream>
using namespace std;

int main()
  {
  ofstream fout("DP8205.txt");
  double y, x;

  for(x = 0; x <= M_PI/4; x += M_PI/40)
      {
      y = sin(abs(x));
      fout << x << " \t " << y << "\n";
      }
  fout.close();
  }
