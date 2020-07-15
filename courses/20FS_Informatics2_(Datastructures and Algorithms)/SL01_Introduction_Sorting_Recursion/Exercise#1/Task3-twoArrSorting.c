#include <stdio.h>

void countPairs(int A[], int nA, int B[], int nB);

int main(){
    int A[] = {100, 64, 34, 25, 12, 22, 11, 90};
    int nA = sizeof(A)/sizeof(A[0]);
    int B[] = {100, 64, 34, 25, 12, 22, 11, 90};
    int nB = sizeof(B)/sizeof(B[0]);
    countPairs(A, nA, B, nB);
    return 0;
}

void countPairs(int A[], int nA, int B[], int nB){
    int i,j,count;
    i=0;
    j=0;
    count=0;
    printf("Pairs:\n");
    while (i < nA){

        while (A[i] > B[j] && j < nB){
            j++;
        }

        while (A[i] == B[j] && j < nB){
            j++;
            count++;
        }
        printf(" (%d, %d)", A[i], count);
        i++;
        count = 0;
    }
}
