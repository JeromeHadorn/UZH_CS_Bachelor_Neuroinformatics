#include <stdio.h>

void swap(int A[], int i, int j);
void printArray(int A[], int n);

void partitioning(int A[], int low, int high, int *p1, int *p2){
    int case1 = 0;
    int case2 = 0;
    int case3 = 0;

    int l = low+1;
    int k = low+1;
    int g = high;
    while (k<g){
        case1 = 0; case2 = 0; case3 = 0;
        if (A[k] < A[low]){
            swap(A,l++, k++);
            case1 = 1;
        } else if (A[k] >= A[high]){
            swap(A, k, --g);
            case2 = 1;
        } else {
            k++;
            case3 = 1;
        }
    printf("%d - %d - %d ===",case1,case2,case3);
    }
    swap(A, low, l-1);
    swap(A, high, k);
    *p1 =  l-1;
    *p2 = k;
}

void swap(int A[], int i, int j){
    int tmp;
    tmp = A[i];
    A[i] = A[j];
    A[j] = tmp;
}

void quicksort(int A[], int low, int high){
    if (high - low <= 0){return;}
    if (A[low] > A[high]){ swap(A, low, high); }
    int p1, p2;
    partitioning(A, low, high, &p1, &p2);
    quicksort(A, low, p1-1);
    quicksort(A, p1+1, p2-1);
    quicksort(A, p2+1, high);
}

void printArray(int A[], int n){
    printf("\n");
    for (int i = 0; i < n;i++){
        printf("%d ", A[i]);
    }
    printf("\n");
}
int main(){

    int A[] = {4,2,5,7,9111,235,235,67,1,88};
    int size = sizeof A  / sizeof *A;
    quicksort(A,0,size-1);
    printArray(A,size);
    return 0;
}
