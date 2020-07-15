#include <stdio.h>
#include <stdlib.h>

void sequence(int n) {
  printf("%d ", n);
	
  if (n == 1){
    return;
  }	

  if (n%2 == 0) {
    n = n/2;
  } else {
    n = 3*n+1;
  }
  sequence(n);
}

void main() {
  int n;

  printf("Enter the first sequence number: ");
  scanf("%d", &n);
	
  printf("Sequence: ");
  sequence(n);
  printf("\n");	
}
// Linux, Mac: gcc task1.c -lm -o task1; ./task1
// Windows: gcc task1.c -lm -o task1; task1
