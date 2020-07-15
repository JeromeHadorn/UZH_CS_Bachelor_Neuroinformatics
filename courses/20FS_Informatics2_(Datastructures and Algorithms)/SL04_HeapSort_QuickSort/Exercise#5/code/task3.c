#include <stdio.h>
#include <math.h>

#define ARRAY_SIZE 10
void swap(int A[], int i, int j) {
    int tmp = A[i];
    A[i] = A[j];
    A[j] = tmp;
}

void printArray(int a[], int size) {
    printf("[");
    int i;
    for(i = 0; i < size; i++) { printf(" %d", a[i]); }
    printf(" ]\n");
}

void partitioning(int A[], int low, int high, int *p1, int *p2) {
    int case1 = 0, case2 =0, case3 = 0;
    int l = low+1;
    int k = low+1;
    int g = high;
    while(k < g) {
        case1 = 0; case2 =0; case3 = 0;
        if (A[k] < A[low]) { swap(A, l++, k++); case1 = 1; }
        else if (A[k] >= A[high]) { swap(A, k, --g); case2 = 1;}
        else { k++; case3 = 1;}
        printf("%d - %d - %d === ",case1,case2,case3);
        printArray(A, ARRAY_SIZE);
    }
    swap(A, low, l-1);
    swap(A, high, k);
    *p1 = l-1;
    *p2 = k;
}

void quicksort(int A[], int low, int high) {
    if (high - low <= 0) { return; }
    if (A[low] > A[high]) { swap(A, low, high); }
    int p1, p2;
    partitioning(A, low, high, &p1, &p2);
    quicksort(A, low, p1-1 );
    quicksort(A, p1+1, p2-1 );
    quicksort(A, p2+1 , high);
}

int main() {
    int A[] = {10, 7, 3, 15, 6, 2, 5, 1, 17, 8};
    int n= 10;
    printArray(A, n);
    quicksort(A, 0, n-1);
    printArray(A, n-1);
    return 0;
}

// Linux, Mac: gcc task3.c -o task3; ./task3
// Windows: gcc task3.c -o task3; task3
