#include <stdio.h>

void countPairs(int A[], int nA, int B[], int nB){
	int i,j, count;
	i = 0;
	j = 0;
	count = 0;
    printf("Pairs");
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

void main() {

	int i, nA, nB;
	int A[1000], B[1000];

	printf("Type elements of A separated by spaces (type non-number value to stop): ");
	i = 0;
	while (scanf("%d", &A[i]) == 1) {
		i++;
	}
	nA = i;
	scanf("%*s");

	printf("Type elements of B separated by spaces (type non-number value to stop): ");
	i = 0;
	while (scanf("%d", &B[i]) == 1) {
		i++;
	}
	 nB = i;
	scanf("%*s");
	
	printf("Pairs:");
	countPairs(A, nA, B, nB);
}
// Linux, Mac: gcc task3.c -o task3; ./task3
// Windows: gcc task3.c -o task3; task3
