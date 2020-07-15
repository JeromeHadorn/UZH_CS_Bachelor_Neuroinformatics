#include <stdio.h>

void swap(int A[], int i, int j) {
  int tmp;
  tmp = A[i];
  A[i] = A[j];
  A[j] = tmp;
}

void heapify(int A[], int i, int n, int d) {
  int max = i;
  int k, child;
  for (k = 1; k<=d; k++){
    child = (d*i) + k;
    if (child < n && A[child]> A[max]) { max = child; }
  }
  if (max != i) {
    swap(A, i, max);
    heapify(A, max, n, d);
  }
}

void buildMaxHeap(int A[], int n, int d) {
  int i;
  for (i = (n-1)/d; i >= 0; i--) {heapify(A, i, n, d);}
}

void heapSort(int A[], int n, int d) {
  int i, s = n;

  buildMaxHeap(A, n, d);
  for (i=n-1; i>0; i--) {
    swap(A, i, 0);
    s--;
    heapify(A, 0, s, d);
  }
}

void printArray(int A[], int n) {
  int i;
  printf("[ ");
  for (i = 0; i < n; i++) {
    printf("%d", A[i]);
    if (i < n-1) {printf(", ");}
  }
  printf(" ]\n");
}

void printHeap(int A[], int n, int d) {
  int i, l, r, k;
     
  printf("graph g {\n");
  for (i = 0; i < n; i++) {
    for (k = 1; k<=d; k++){
       if ((d*i) + k < n) { printf("  %d -- %d\n", A[i], A[(d*i) + k]); }
	}
  }
  printf("}");
}

void main() {
  int A[100];
  int i, n, d;

  printf("Type elements of A seperated by spaces (type 'end' to stop): ");
  i = 0;
  while(scanf("%d", &A[i]) == 1) i++;
  n = i;
  // Read but do not store any terminating not integer values ('end')
  scanf("%*s");

  printf("Type the number of maximum number of child a parent can have in the max heap: ");
  scanf("%d", &d);

  buildMaxHeap(A, n, d);
  printArray(A, n);
  printf("Heap:\n");
  printHeap(A, n, d);
  printf("\nSorted array:\n");
  heapSort(A, n, d);
  printArray(A, n);
}

// Linux, Mac: gcc task1.c -o task1; ./task1
// Windows: gcc task1.c -o task1; task1
