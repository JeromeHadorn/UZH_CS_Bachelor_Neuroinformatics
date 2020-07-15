# include <stdio.h>

void evenOddInsertionSort(int A[], int n);
void insertionSort(int A[], int n);

int main(){
	int numbers[100] = {2,10,3,22,15,12};

	int size = sizeof(numbers);
	evenOddInsertionSort(numbers, 6);

	return 1;
}

void printArray(int arr[], int size){
         int i;
         for (i=0;i< size;i++){
             printf("%d ", arr[i]);
         }
         printf("\n");
  }


void insertionSort(int A[], int n){
    int position, value, i;

    for (i = 1; i < n; i++){
        value = A[i];
        position = i;
        
        while (position > 0 && A[position - 1] > value){
            A[position] = A[position-1];
            position--;
        }
        A[position] = value;
    }
}

void evenOddInsertionSort(int A[], int n){
   int evenCount, oddCount, i, evenSum, oddSum;
   int evenList[n], oddList[n];

   evenCount = 0; oddCount = 0;
   evenSum = 0; oddSum = 0;

   insertionSort(A, n);

   for (i = 0; i < n; i++){
       if (A[i] % 2 == 0){
        evenList[evenCount]=A[i];
        evenCount += 1;
        evenSum += A[i];
       } else {
        oddList[oddCount] = A[i];
        oddCount += 1;
        oddSum += A[i];
       }
   }
    printf("Sorted even numbers: ");
    for (i=0; i < evenCount; i++){
       printf("%d ",evenList[i]);
    }
    printf("Sum of even numbers: %d \n", evenSum);

    for (i=0; i < oddCount; i++){
       printf("%d ",oddList[i]);
    }

    printf("Sum of odd numbers: %d \n", oddSum);

}
