#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int n; // порядок матрици
double** slar;// СЛАР
double* r;
double* result;
double determinant;
double i;
double eps= 0.00000001;

int read(const char* filename)
{
  FILE *myfile = fopen (filename, "r");
  if(!myfile)
  {
      printf("ERROR \n");
      return 0;
  }
    fscanf(myfile,"%d", &n);
    slar=malloc(n*sizeof(double*));
    for(int i=0; i<n; ++i)
    {
      slar[i]=malloc(n*sizeof(double));
    }
    r=malloc(n*sizeof(double));
    result=malloc(n*sizeof(double));

    for(int i=0; i<n; ++i)
    {
        for(int j=0; j<n; ++j)
        {
            fscanf(myfile,"%lf", &slar[i][j]);
        }
    }
    for(int j=0; j<n; ++j)
    {
        fscanf(myfile,"%lf", &r[j]);
    }
    fclose(myfile);
return 1;
}

//________________________________________________________________________________
int scan()
{
  printf("n=");
  scanf("%d", &n);

  slar=malloc(n*sizeof(double*));
  for(int i=0; i<n; ++i)
  {
    slar[i]=malloc(n*sizeof(double));
  }
  r=malloc(n*sizeof(double));
  result=malloc(n*sizeof(double));

  for(int i=0; i<n; ++i)
  {
      for(int j=0; j<n; ++j)
      {
          printf("СЛАР[%i][%i]=", i+1, j+1);
          scanf("%lf", &slar[i][j]);
      }
  }
  for(int j=0; j<n; ++j)
  {
      printf("ПР[%i]=", j+1);
      scanf("%lf", &r[j]);
  }
  return 1;
}

//________________________________________________________________________________
int print()
{
  for(int i=0; i<n; ++i)
  {
      for(int j=0; j<n; ++j)
      {
          printf("%f ", slar[i][j]);
      }
      printf(" | %f\n", r[i]);
  }
  printf("\n");
return 1;
}

int print_result()
{
  for(int i =0; i<n; ++i)
  {
    printf("x[%i]=%f\n",i, result[i]);
  }
return 1;
}

//________________________________________________________________________________
int copy_vector(double* dest, double* source)
{
  for(int i=0; i<n; ++i)
  {
    dest[i]=source[i];
  }
  return 0;
}
//________________________________________________________________________________
double summ(int i)
{
  double res=0;
  for (int j=0; j<n; ++j)
  {
    if(j != i)
    {
      res += slar[i][j]*result[j];
    }

  }
  return res;

}
//________________________________________________________________________________

int jacobi()
{
  double* xnov;
  double delta_max;
  double delta;
  xnov=malloc(n*sizeof(double));
  copy_vector(result,r);
    do
    {
      delta_max=0;
      for(int i=0; i<n; ++i)
      {
          xnov[i]=(r[i]-summ(i))/slar[i][i];
          delta = fabs(xnov[i]-result[i]);
          if(delta>delta_max)
          {
            delta_max=delta;
          }
      }

      copy_vector(result, xnov);
    }

    while(delta_max>=eps);

  return 0;
}


int gauss()
{
  for(int i=0; i<n-1; ++i)
  {

    int m =i;

    for(int k=i+1; k<n; ++k)
    {
      if(fabs(slar[k][i])>fabs(slar[m][i]))
        m=k;
    }
    if(m!=i)
    {
      for(int j=i; j<n; ++j)
      {
        double t=slar[m][j];
        slar[m][j]=slar[i][j];
        slar[i][j]=t;
      }
      double t=r[m];
      r[m]=r[i];
      r[i]=t;
    }

print();
   if (slar[i][i]==0)
   {
     printf("ERROR (МАТРИЦЯ ВИРОДЖЕНА)\n");
   return 0;
   }
//________________________________________________________________________________
    for(int k=i+1; k<n; ++k)
    {
      double p=slar[k][i]/slar[i][i];
        for(int j=i; j<n; ++j)
        {
            slar[k][j]=slar[k][j]-p*slar[i][j];
        }
    r[k]=r[k]-p*r[i];
    print();
    }
  }
  result[n-1]=r[n-1]/slar[n-1][n-1];
  for (int i = n-2; i>=0; --i)
  {
    double s=0;
    for(int j=i+1; j<n; ++j)
    {
      s=s+slar[i][j]*result[j];
    }
    result[i]=(r[i]-s)/slar[i][i];
  }
return 1;
}

//________________________________________________________________________________
int main(int argc, char* argv[])
{
/*if(argc!=2)
{
  printf("usage: \n\t%s <file>\n",argv[0]);
  return 0;
}*/
/*int i;*/
read(argv[1]);
print();
//gauss();
gauss();
print_result();

determinant=slar[0][0];

for (int i = 1; i < n; i++)
{
  determinant=determinant*slar[i][i];
}

printf("Детерминант=%f\n", determinant);
return 0;
}
