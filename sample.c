/* sample.c
 * contains: malloc, strcpy, strncpy, memcpy, puts, printf, free
 *
 * gcc -g -o sample.elf sample.c -Wall -Wextra -O0
 *
 */



#include <stdio.h>
#include <stdlib.h>
#include <string.h>


int main(int argc, char ** argv)
{
  char arr[100];
  char * buf;
  int len;


  buf = malloc(1024);
  
  strncpy(buf, "Hallo", 1000);

  len = strlen(buf);

  memcpy(arr, buf, sizeof(char)*(len+1));

  puts(arr);

  printf("%d\n", argc);

  free(buf);

  return 0;
}
