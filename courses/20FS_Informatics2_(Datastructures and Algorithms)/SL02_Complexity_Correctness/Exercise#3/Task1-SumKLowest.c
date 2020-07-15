#include <stdio.h>


int sumKLowest(int A[], int k, int n){
    int mini = 0;
    int sum = 0;
    
    for (int i = 0; i < k; i++){
        
        mini = i;

        for (int j = i + 1; j < n; j++ ){
            if (A[j] < A[mini]){
                mini = j;
            }
        }

        sum = sum + A[mini];
        int swp = A[i];
        A[i] = A[mini];
        A[mini] = swp;
    }
    return sum;
}


int main(){
    int k;
    scanf("%d", &k);
    int A[] = {100, 64, 34, 25, 12, 22, 11, 90};
    int nA = sizeof(A)/sizeof(A[0]);
    int sum = sumKLowest(A,k,nA);
    printf("sum %d Lowest = %d \n", k,sum);
    return 0;
}
