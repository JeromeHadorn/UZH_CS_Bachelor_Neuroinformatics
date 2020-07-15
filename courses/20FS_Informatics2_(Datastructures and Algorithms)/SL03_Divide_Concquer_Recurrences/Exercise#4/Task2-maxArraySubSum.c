#include <stdio.h>

int overLapArraySum(int arr[], int l, int m, int r){
    int sum = 0;int i = 0;
    int leftSum = -50000;
    for (i=m; i>=l;i--){
        sum = sum + arr[i];
        if (sum > leftSum){
            leftSum = sum;
        }
    }

    sum = 0; i=m+1;
    int rightSum = -50000;
    for (i=m+1;i<r;i++){
        sum = sum + arr[i];
        if (sum > rightSum){
            rightSum = sum;
        }
    }
    return leftSum + rightSum;
}
int maxSubArraySum(int arr[], int l, int r){
    if (l == r){
        return l; // or r doesn't matter
    }

    int m = (l+r)/2;

    int leftArraySum = maxSubArraySum(arr,l,m);
    int rightArraySum = maxSubArraySum(arr,m+1,r);
    int overlapArraySum = overLapArraySum(arr,l,m,r);
    
    if (leftArraySum>rightArraySum && leftArraySum>overlapArraySum){
        return leftArraySum;
    } else if (rightArraySum>leftArraySum && rightArraySum>overlapArraySum){
        return rightArraySum;
    }
    return overlapArraySum;
}

int main(){
    int a[] = {1,-4,5,2,-8,9,1,5,3,-10,12};
    int size = sizeof(a)/sizeof(a[0]);
    int r = maxSubArraySum(a,0,size-1);
    printf("max Sum is: %d \n",r);
    return 0;
}
