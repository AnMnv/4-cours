#include<stdio.h>
#include <stdlib.h>
#include <math.h>
#define EPS 1e-6

int read_n(FILE* f){
  int nn;
  fscanf(f,"%d", &nn);
  return nn;
}

double** init_matrix(int n){
  double ** res;
  res = malloc(n*sizeof(double*));
  if(!res){
    return NULL;
  }
  for(int i=0; i<n; ++i){
    res[i] = malloc(n*sizeof(double));
    if(!res[i]){
      return NULL;
    }
  }
  return res;
}

double** init_one_matrix(int n){
  double** res = init_matrix(n);
  for(int i=0; i<n;++i)
  {
    for (int j = 0; j < n; j++)
    {
      if(i==j)
      {
       res[i][j]=1;
      }
       else {
         res[i][j]=0;
       }
     }
   }
  return res;
}
double** read_symm_matrix(FILE* f, int n){
  double ** res = init_matrix(n);
  for(int i=0; i<n; ++i)
  {
      for(int j=0; j<n; ++j)
      {
          fscanf(f,"%lf", &res[i][j]);
      }
  }
  return res;
}

double** transpon_matrix(int n, double** matrix){
  double** res = init_matrix(n);
  for(int i=0;i<n;++i){
    for(int j=0; j<n; ++j){
      res[j][i]=matrix[i][j];
    }
  }
  return res;
}

double** mul_matrix(int n, double** m1, double** m2){
  double** res = init_matrix(n);
  for(int i=0; i<n; ++i){
    for(int j=0; j<n; ++j){
      res[i][j]=0;
      for(int k=0;k<n; ++k){
        res[i][j]+=m1[i][k]*m2[k][j];
      }
    }
  }
  return res;
}

int print_matrix(int i, double** m);


int jacobi(int n, double** d, double** q, double eps)
{
  int iterations=1;
  for(int i=0; i<n;++i)
  {
    for (int j = 0; j < n; j++)
    {
      if(i==j)
      {
       q[i][j]=1;
      }
       else {
         q[i][j]=0;
       }
     }
   }
   do {
     double dlm=d[1][0];
     int l=1;
     int m=0;
     for (int  i = 1; i < n; i++)
     {
       for (int j = 0; j < (i-1); j++)
       {
         if(fabs(d[i][j]) > fabs(dlm))
         {
           dlm=d[i][j];
           l=i;
           m=j;
         }
       }
     }

     if (fabs(dlm)<eps) break;

     double t=(d[l][l]-d[m][m])/(2.0f*d[l][m]);
     double u=t/sqrt(1.0f+t*t) ;
     double c=sqrt((1.0f+u)/2.0f);
     double s=sqrt((1.0f-u)/2.0f);

     for(int i=0; i<n; i++)
     {
       double qil = q[i][l]*c+q[i][m]*s;
       double qim = -q[i][l]*s+q[i][m]*c;
       q[i][l]=qil;
       q[i][m]=qim;
     }
     double dll=d[l][l]*c*c+2*d[l][m]*c*s+d[m][m]*s*s;
     double dmm=d[l][l]*s*s-2*d[l][m]*c*s+d[m][m]*c*c;
     d[l][l]=dll;
     d[m][m]=dmm;
     d[l][m]=0;
     d[m][l]=0;

     for (int i = 0; i < n; i++)
     {
       if(i!=l && i!=m)
       {
         double dil= d[i][l]*c+d[i][m]*s;
         double dim=-d[i][l]*s+d[i][m]*c;
         d[i][l]=dil;
         d[l][i]=d[i][l];
         d[i][m]=dim;
         d[m][i]=d[i][m];
       }
     }
     printf("%d\n",iterations);
     iterations++;
     print_matrix(n, q);
     print_matrix(n, d);
     printf("\n\n\n");
   }
   while(1);
   return 0;
}

int print_matrix(int n, double** m)
{
  for(int i=0; i<n; ++i)
  {
      for(int j=0; j<n; ++j)
      {
          printf(" %f\t ", m[i][j]);
      }
      printf(" \n ");
  }
    printf(" \n ");
  return 0;
  }

int compare_matrix(int n, double** m1, double** m2){
  for(int i=0;i<n;++i){
    for(int j=0; j<n; ++j){
      if(fabs(m1[i][j]-m2[i][j])>EPS)// сравнение с точностью
      {
        printf("%d %d %f %e\n",i,j, m1[i][j], m2[i][j]);
        return 0;
      }
    }
  }
  return 1;
}

double** copy_matrix(int n, double** m){
  double** res=init_matrix(n);
  for(int i=0;i<n;++i){
    for(int j=0; j<n; ++j){
      res[i][j]=m[i][j];
    }
  }
  return res;
}

int main(int argc, char* argv[]){
  if(argc != 2){
    printf("Usage:\n\t %s <file with matrix>\n", argv[0]);
    return 1;
  }
  FILE *f = fopen(argv[1], "r");
  if(!f){
    printf("error: can't open file %s\n", argv[1]);
    return 2;
  }
  int n = read_n(f);
  double** a = read_symm_matrix(f, n);
  double** d = copy_matrix(n,a);
  double** q = init_matrix(n);

  print_matrix(n, d);

  jacobi(n, d, q, EPS);
  printf("Ортогональна матриця власних векторів Q: \n\n");

  print_matrix(n, q);
  printf("Діагональна матриця власних чисел D: \n\n");
  print_matrix(n, d);
  double** qt = transpon_matrix(n, q);
  printf("Транспонована матриця: \n\n");
  print_matrix(n, qt);
  double** qqt = mul_matrix(n, q, qt);
  printf("Перевіряемо Q^T*Q==E: \n\n");
  print_matrix(n, qqt);
  double** e=init_one_matrix(n);
//  printf("Qt*Q %s E\n", compare_matrix(n, qqt, e)?"==":"!=");
  double** qd = mul_matrix(n, q, d);
  double** qdqt = mul_matrix(n, qd, qt);
  printf("Перевіряемо QD^T*Q==А: \n\n");
  print_matrix(n, qdqt);
  //printf("Q*D*Qt %s A\n", compare_matrix(n, qdqt, a)?"==":"!=");
  return 0;
}
