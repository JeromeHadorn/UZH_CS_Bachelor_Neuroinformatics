#include <stdio.h>

int findOddOccuring(int arr[], int l, int r){
	// base case
	if (l == r) {
		return l;
	}
    
	int mid = (l + r) / 2;
	if (mid %2 == 1){ // if mid is odd
		if (arr[mid] == arr[mid - 1])
			return findOddOccuring(arr, mid + 1, r);
		else
			return findOddOccuring(arr, l, mid - 1);
	}
	else{ // mid is even
		if (arr[mid] == arr[mid + 1])
			return findOddOccuring(arr, mid + 2, r);
		else
			return findOddOccuring(arr, l, mid);
	}
}

// main function
int main(void){
	int arr[] = { 2, 2, 1, 1, 3, 3, 2, 2, 4, 4, 3,  1, 1 };
	int n = 13;

	int index = findOddOccuring(arr, 0, n - 1);
	printf("The odd occurring element is %d ", arr[index]);

	return 0;
}


// Linux, Mac: gcc task1.c -o task1; ./task1
// Windows: gcc task1.c -o task1; task1