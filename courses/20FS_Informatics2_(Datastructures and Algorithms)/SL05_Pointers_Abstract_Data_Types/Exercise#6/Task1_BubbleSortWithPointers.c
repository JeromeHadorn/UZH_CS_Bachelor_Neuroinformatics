#include <stdio.h>

void bubbleSortWithPointers(int* ptr , int n){
    int i; int j; int t;

    for(i = 0; i < n-1; i++){
        for (j=0; j< n-i-1;j++){
        
            if (*(ptr + j) < *(ptr+j+1)){
                t = *(ptr + j + 1);
                *(ptr + j+ 1)= *(ptr+j);
                *(ptr + j) = t;
            }
        }
    }
}

int main(){
    int A[] = {5,3,791,123,521,45,1,3,753,99,6};
    int n = sizeof(A)/sizeof(A[0]);
    bubbleSortWithPointers(A,n);
    for (int i = 0; i < n; i++){
        printf("%d, ", A[i]);
    }
    printf("\n");
}




