#include <stdio.h>
#include <stdlib.h>

// Start Helper
void swap(int A[], int i, int j){
    int tmp;
    tmp = A[i];
    A[i] = A[j];
    A[j] = tmp;
}

void heapify(int A[], int i, int n, int d){
    int max = i;
    int k, child;
    for(k = 1; k<=d; k++){
        child = (d*i) + k;
        if (child < n && A[child] > A[max]){
            max = child;
        }
    }
    if (max != i){
        swap(A,i,max);
        heapify(A, max, n, d);
    }
}
// End
void buildMaxHeap(int A[], int n, int d); void printHeap(int A[], int n, int d); void heapSort(int A[], int n, int d); void printArray(int A[], int n);

void buildMaxHeap(int A[], int n, int d){
    int i;
    for (i=(n-1)/d; i>=0;i--){
        heapify(A, i, n, d);
    }
}

void heapSort(int A[], int n, int d){
    int i, s = n;
    
    buildMaxHeap(A,n,d);
    for (i = n-1; i>0; i--){
        swap(A, i, 0);
        s--;
        heapify(A, 0, s, d);
    }
}

void printHeap(int A[], int n, int d){
    int i, l, r, k;

    printf("graph g {\n");
    for (i=0;i<n;i++){
        for (k=1; k<=d; k++){
            if ((d*i)+k < n){
                printf("   %d -- %d \n", A[i], A[(d*i) + k]);
            }
        }
    }
    printf("}");
}

void printArray(int A[], int n){
    for(int i=0; i<n;i++){
        printf("%d,\n",A[i]);
    }
    printf("\n");
}

int main(){
    int A[100];
    int i, n, d;

    printf("Type elem separated by space for A, end with end");
    i = 0;
    while(scanf("%d", &A[i]) == 1){
        i++;
    }
    n=i;
    scanf("%*s");

    printf("enter level of nodes");

    scanf("%d", &d);

    buildMaxHeap(A,n,d);
    printArray(A, n);
    printf("Heap: \n");
    printHeap(A, n, d);
    printf("\n Sorted Aray: \n");
    heapSort(A,n,d);
    printArray(A,n);

    return 0;
}
