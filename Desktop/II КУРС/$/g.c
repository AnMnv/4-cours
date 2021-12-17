#include<stdio.h>
#include <sys/ioctl.h>
#include <unistd.h>

int y;
int word_length[100];

int read_file(const char* filename)
{
  FILE *myfile = fopen (filename, "r");
  if(!myfile)
  {
      printf("ERROR \n");
      return 0;
  }
  for (int i = 0; i < 100; i++)
  {
    word_length[i]=0;
  }
  int length = 0;
  char curr;
  int res = fread(&curr, 1, 1, myfile);
  while(res == 1){
//    putchar(curr);
    if(curr != ' ' && curr != '\n'){
      ++length;
    }else{
      ++word_length[length];
      length = 0;
    }
    res = fread(&curr, 1, 1, myfile);
  }
  ++word_length[length];
  fclose(myfile);
  return 0;
}

int max(){
  int res = word_length[0];
  for(int i=1; i<100; ++i){
    if(word_length[i] > res){
      res = word_length[i];
    }
  }
  return res;
}


int min()
{
  int res = word_length[0];
  for(int i=1; i<100; ++i)
  {
    if(word_length[i] < res)
    {
      res = word_length[i];
    }
  }
  return res;
}



int palki(int i)
{
  printf("|");
  while (i)
  {
    printf("|");
    --i;
  }
  return 0;
}

int check(int a, int b){
  if(a < b){
    return 0;
  } else{
    return 1;
  }
  return 1;
}

#define MAX_HEIGHT 30
int main(int argc, char* argv[])
{
  read_file(argv[1]);
  struct winsize w;
  ioctl(STDOUT_FILENO, TIOCGWINSZ, &w);
//  for (int i = 1; i < 100; i++)
//  {
//    if(word_length[i])
//      printf("words of length %i - %i\n", i, word_length[i]);
//  }
  int koef=(max()- min())/w.ws_row;
//printf("%i %i %i\n",min(), max(), koef);
  /*for (int i = 1; i < 100; i++)
  {
    if(word_length[i])
    {
      printf("%i\t", i);
      palki((word_length[i]-min())/koef);
      printf("\n");
    }

  }
  */

for(int i=w.ws_row; i >=0; --i){
  printf("\t");
  for(int j=0;j<100;++j){
    if(word_length[j]){
      if(check((word_length[j]-min())/koef, i)){
        printf("* ");
      }else{
        printf("  ");
      }
    }
  }
  printf("\n");
}
  return 0;
}
