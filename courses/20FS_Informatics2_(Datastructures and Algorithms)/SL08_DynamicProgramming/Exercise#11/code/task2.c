#include<stdio.h>
#include<stdlib.h>

void swap(int *xp, int *yp) { 
    int temp = *xp; 
    *xp = *yp; 
    *yp = temp; 
} 

void sort(int arr[], int n) { 
   int i, j; 
   for (i = 0; i < n-1; i++)          
       for (j = 0; j < n-i-1; j++)  
           if (arr[j] > arr[j+1]) 
              swap(&arr[j], &arr[j+1]); 
} 
  
int lenOfLongestGP(int set[], int n) { 
    if(n < 2) { return n;}
    if (n == 2) {
        return (set[0] % set[1] == 0 || set[1] % set[0] == 0) + 1;
    }
    sort(set, n);
    // An entry L[i][j] in this table stores LLGP with 
    // set[i] and set[j] as first two elements of GP 
    // and j > i. 
    int L[n][n];
    int llgp = 1;
    int i,j; 
    for (i = 0; i < n-1; ++i) {
        if (set[n-1] % set[i] == 0) {
            L[i][n-1] = 2;
            if(L[i][n-1] > llgp) {
                llgp = L[i][n-1];
            }
        } else {
            L[i][n-1] = 1;
        }
    }
    // Consider every element as second element of GP
    for (j = n - 2; j >= 1; --j) {
        // i, j, k that form a GP
        int i = j-1, k=j+1;

        while(i>= 0 && k <= n-1) {
            // when do these form a GP?  set[i] * set[k] == set[j]^2, k/j = j/i

            if(set[i] * set[k] < set[j]*set[j]) {
                ++k;
            } else if (set[i] * set[k] > set[j]*set[j]) {
                if (set[j] % set [i] == 0) {
                    L[i][j] = 2;
                    if (L[i][j] > llgp) {
                        llgp = L[i][j];
                    }
                } else {
                    L[i][j] = 1;
                }
                --i;
            }
            //i, j, k is a GP
            else {
                L[i][j] = L[j][k] + 1;
                // Update
                if(L[i][j] > llgp) {
                    llgp = L[i][j];
                }

                --i;
                ++k;
            }
        }

        while (i >= 0) {
            if(set[j] % set[i] == 0) {
                L[i][j] = 2;
                if(L[i][j] > llgp) {
                    llgp = L[i][j];
                }
            } else {
                L[i][j] = 1;
            }
            --i;
        }
    }
    return llgp; 
} 


int main() 
{ 
    int set1[] = {1, 3, 9, 27, 81, 243}; 
    int n1 = sizeof(set1)/sizeof(set1[0]); 
    printf("Length of Longest GP: %d\n", lenOfLongestGP(set1, n1));
  
    int set2[] = {1, 3, 4, 9, 7, 27}; 
    int n2 = sizeof(set2)/sizeof(set2[0]); 
    printf("Length of Longest GP: %d\n", lenOfLongestGP(set2, n2));
  
    int set3[] = {2, 3, 5, 7, 11, 13}; 
    int n3 = sizeof(set3)/sizeof(set3[0]); 
    printf("Length of Longest GP: %d\n", lenOfLongestGP(set3, n3));

    int set4[] = {2, 4, 5, 7, 13};
    int n4 = sizeof(set4)/sizeof(set4[0]);
    printf("Length of Longest GP: %d\n", lenOfLongestGP(set4, n4));
  
    return 0; 
} 

// Linux, Mac: gcc task2.c -o task2; ./task2
// Windows: gcc task2.c -o task2; task2
