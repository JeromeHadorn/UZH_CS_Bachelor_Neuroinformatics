#include <stdio.h>
#include <stdlib.h>

int sumKLowest(int a[], int k, int n) {
  int i, j, swp;
  int mini;
  int sum = 0;
  for(i = 0; i < k; i++) {
    mini = i;
    for(j = i + 1; j < n; j++) {
      if(a[j] < a[mini]) mini = j;
    }

    sum += a[mini];

    swp = a[i];
    a[i] = a[mini];
    a[mini] = swp;
  }
  return sum;
}

int main() {

  int A[10] = {10, 12, 3, 4, 9, 7, 1, 25, 2, 1}; 
  int k=4, n=10;
  
  printf("k= %d\n", k);
  printf("sum= %d\n", sumKLowest(A, k, n));
  
  return 0;
}

// Linux, Mac: gcc task1.c -lm -o task1; ./task1
// Windows: gcc task1.c -lm -o task1; task1


