#include <stdio.h> 
int maxOverlapArraySum(int arr[], int l, int m, int r) { 
    int sum = 0, i=0; 
    int left_sum = -50000; 
    for ( i = m; i >= l; i--) { 
        sum = sum + arr[i]; 
        if (sum > left_sum) {
          left_sum = sum; 
      }
    } 
    sum = 0;
	i=0; 
    int right_sum = -50000; 
    for (i = m+1; i <= r; i++) { 
        sum = sum + arr[i]; 
        if (sum > right_sum) {
          right_sum = sum; 
      }
    } 
    return left_sum + right_sum; 
} 

int maxSubArraySum(int arr[], int l, int r) { 
   if (l == r) 
     return arr[l]; 
   int m = (l + r)/2;  
   int leftArraySum  = maxSubArraySum(arr, l, m);
   int rightArraySum = maxSubArraySum(arr, m+1, r); 
   int overlapArraySum = maxOverlapArraySum(arr, l, m, r);
   if (leftArraySum>rightArraySum && leftArraySum>overlapArraySum) {
   		return leftArraySum; 
   } else if (rightArraySum>leftArraySum && rightArraySum>overlapArraySum) {
   		return rightArraySum; 
   } 
   return overlapArraySum;
} 
  
int main() 
{ 
   int arr[] = {-1, 2, -3, 4, 3, -5, 1, 5}; 
   int n = 8; 
   int max_sum = maxSubArraySum(arr, 0, n-1); 
   printf("Maximum contiguous sum is %d \n", max_sum); 
   return 0; 
} 


// Linux, Mac: gcc task2.c -o task2; ./task2
// Windows: gcc task2.c -o task2; task2