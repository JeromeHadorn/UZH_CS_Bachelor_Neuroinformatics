#include <stdio.h>

void insertionSort(int A[], int n) {
	int position, value, i;

	for (i = 1; i < n; i++) {
		value = A[i];
		position = i;

		while (position > 0 && A[position-1] > value) {
			A[position] = A[position-1];
			position--;
		}
		A[position] = value;
	}
}

void evenOddInsertionSort(int A[], int n){
	int evenCount, oddCount, i, evenSum, oddSum;
	int evenList[n], oddList[n];
	evenCount = 0;
	oddCount = 0;
	evenSum = 0;
	oddSum = 0;
	i = 0;

	insertionSort(A, n);
	for (i = 0; i < n; i++){
		if (A[i]%2 == 0){
			evenList[evenCount] = A[i];
			evenSum += A[i];
			evenCount++;
		}
		else{
			oddList[oddCount] = A[i];
			oddSum += A[i];
			oddCount++;
		}
	}
    
	printf("Sorted even numbers: "); 
	for (i = 0; i < evenCount; i++){
		printf("%d ", evenList[i]);
	}
	printf("\nSum of even numbers: ");
	printf("%d ", evenSum);
    printf("\nSorted odd numbers: ");
	for (i = 0; i < oddCount; i++){
		printf("%d ", oddList[i]);
	}
	printf("\nSum of odd numbers: ");
	printf("%d ", oddSum);
}

void main() {
	int A[100];
	int n, i;

	printf("Values of A separated by spaces (non-number to stop):");
	i = 0;
	while (scanf("%d", &A[i]) == 1) {
		i++;
	}
	n = i;
	scanf("%*s");
	
	printf("Result: ");
	evenOddInsertionSort(A, n);
}
// Linux, Mac: gcc task4.c -o task4; ./task4
// Windows: gcc task4.c -o task4; task4
