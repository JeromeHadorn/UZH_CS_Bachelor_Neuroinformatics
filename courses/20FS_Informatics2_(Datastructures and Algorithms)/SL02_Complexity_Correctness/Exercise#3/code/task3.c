#include <stdio.h>

void printArray(char a[]) {
  int i=0;
  printf("[");
  while (a[i] != '\0'){
    if (a[i+1] == '\0') {
      printf("%c ]", a[i]);
      break;
    }
    else {
       printf("%c, ", a[i]);
       i++;
    }
  }
  printf("\n");
}

int substrings(char A[], char B[]) {
  
  /* Cases 3 & 4 */
  if(A == NULL || B == NULL) {
    return 0;
  }

  /* Cases 1 & 2*/
  if(A[0] == '\0' || B[0] == '\0') {
    return 0;
  }

  /* Calculate length of B */
  int sizeB = 0;
  while(B[sizeB] != '\0') {
    sizeB++;
  }

  int numOccurrences = 0;
  int currentPosition = 0;
  
  /* #chars matching B, starting from current position */
  int matchingChars = 0;

  while(A[currentPosition] != '\0') {

    matchingChars = 0;

    /* Cases 5 & 6 */
    while ( B[matchingChars] != '\0' &&
    A[currentPosition + matchingChars] == B[matchingChars]) {
      matchingChars++;
    }
    if(matchingChars == sizeB) {
      printf("(%d,%d) ", currentPosition + 1, currentPosition + sizeB);
      numOccurrences++;
    }
    /* Cases 7 & 8 */
    currentPosition++;
  }

  return numOccurrences;
}


int main() {
  
  char a[] = "nitrite";
  char b[] = "it";
  
  printArray(a);
  printArray(b);
  printf("\nrep_num: %d\n\n", substrings(a, b));
  
  // You can assign different variables to a,b
  // to check it for all the cases 
  
  return 0;
}


// Linux, Mac: gcc task3.c -lm -o task3; ./task3
// Windows: gcc task3.c -lm -o task3; task3