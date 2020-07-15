#include <stdio.h>
#include <stdlib.h>

void swap(int A[], int i, int j){
    int tmp;
    tmp = A[i];
    A[i] = A[j];
    A[j] = tmp;
}


void partitioning(int A[], int low, int high, int *p1, int *p2){
    int case1 = 0;
    int case2 = 0;
    int case3 = 0;

    int l = low + 1;
    int k = low + 1;
    int g = high;

    while (k < g){
        case1 = 0; case2 = 0; case3 = 0;
        
        if (A[k] < A[low]){
            swap(A, l++, k++);
            case1 = 1;
        } else if (A[k] >= A[high]){
            swap(A, k, --g);
            case2 = 1;
        } else {
            k++;
            case3 = 1;
        }
        printf("%d_-_%d_-%d_===_",case1,case2,case3);
    }
    
    swap(A,low,l-1);
    swap(A,high,k);
    *p1 = l-1;
    *p2 = k;
}

void quickSort(int A[], int low, int high){
    if (high - low <=0){
        return;
    }

    if (A[low] > A[high]){
        swap(A,low,high);
    }
    int p1,p2;
    partitioning(A,low,high,&p1,&p2);
    quickSort(A,low,p1-1);
    quickSort(A,p1+1,p2-1);
    quickSort(A,p2+1, high);
}

int main(){
    int A[] = {1,5,788,2,4,7,9,31,2,5,88,0,3,47,8};
    quickSort(A,0,15);
    printf("\n\n");
    for (int i= 0; i<16;i++){
        printf("%d,", A[i]);
    }
    printf("\n");
    return 0;
}
