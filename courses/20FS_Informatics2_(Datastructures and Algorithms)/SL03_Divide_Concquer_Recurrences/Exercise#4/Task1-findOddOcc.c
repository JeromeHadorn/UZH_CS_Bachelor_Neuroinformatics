#include <stdio.h>



int findOddOcc(int A[], int l, int r){
    if (l==r){
        return l; // or r doesn't matter
    }

    int m = (l+r)/2;
    if (A[m] % 2){
        // Middle is Odd
        if (A[m] == A[m-1]){
            // Left Number = Current Number
            return findOddOcc(A,m+1,r);
        } else {
            return findOddOcc(A,l,m-1);
        }
    } else {
        //Middle is even
        if (A[m] == A[m+1]){
            return findOddOcc(A,m+1,r);
        } else {
            return findOddOcc(A,l,m-1);
        }
    }
}






int main(){
    int A[] = {1,1,2,2,3,3,4,4,4,5,5};
    int n = sizeof(A) / sizeof(A[0]);
    int r = findOddOcc(A,1,n);
    printf("odd element is: %d at index: %d \n",A[r],r);
    return 0;
}

