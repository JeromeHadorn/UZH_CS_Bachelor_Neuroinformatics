#include<stdio.h>
#include<stdlib.h>

int min(int x, int y) {
    return x < y ? x : y;
}

#define INT_MAX 300
int dp[INT_MAX][INT_MAX];

int minimumSquare(int m, int n) { 
    int vertical_min = INT_MAX; 
    int horizontal_min = INT_MAX; 
      
    if (m == n) 
        return 1; 
      

    if (dp[m][n]) 
        return dp[m][n]; 

      
    for (int i = 1;i<= m/2;i++) { 
        horizontal_min = min(minimumSquare(i, n) +  
                minimumSquare(m-i, n), horizontal_min);  
    } 
      
    for (int j = 1;j<= n/2;j++) { 
        vertical_min = min(minimumSquare(m, j) +  
                minimumSquare(m, n-j), vertical_min); 
    } 
          
    dp[m][n] = min(vertical_min, horizontal_min);  
          
    return dp[m][n]; 
} 
  
int main() {
    int m = 3, n = 4; 
    printf("%d\n", minimumSquare(m, n)); 
    return 0; 
} 

// Linux, Mac: gcc task3.c -o task3; ./task3
// Windows: gcc task3.c -o task3; task3
