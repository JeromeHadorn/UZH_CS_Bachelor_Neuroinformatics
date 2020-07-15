#include <stdio.h> 
  
// Function to sort the numbers using pointers 
void sort(int n, int* ptr) { 
    int i, j, t; 
  
    for (i = 0; i < n-1; i++) { 
		for (j = 0; j < n-i-1; j++) {
  
            if (*(ptr + j) < *(ptr + j + 1)) { 
  
                t = *(ptr + j + 1); 
                *(ptr + j+1) = *(ptr + j); 
                *(ptr + j) = t; 
            } 
        } 
    } 
  
    for (i = 0; i < n; i++) {
        printf("%d ", *(ptr + i));
	}
} 
  
// Driver code 
int main() { 
	int i, n;
	int arr[100];

	printf("Enter values of A separated by spaces (non-number to stop):");

	i = 0;
	while (scanf("%d", &arr[i]) == 1) {
		i++;
	}
	 n = i;
	scanf("%*s");
    sort(n, arr); 
  
    return 0; 
}
// Linux, Mac: gcc task1.c -o task1; ./task1
// Windows: gcc task1.c -o task1; task1
