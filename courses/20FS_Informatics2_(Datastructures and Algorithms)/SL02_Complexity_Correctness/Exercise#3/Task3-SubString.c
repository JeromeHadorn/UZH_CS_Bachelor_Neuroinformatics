#include <stdio.h>


int substrings(char A[], char B[]){
    if (A == NULL || B == NULL || A[0] == '\0' || B[0] == '\0'){
        return 0;
    }
    
    int sizeB = 0;
    while (B[sizeB] != '\0'){
        sizeB++;
    }

    int numOccurences = 0;
    int matchingChars = 0;
    int currentPosition = 0;

    while (A[currentPosition] != '\0'){
        matchingChars = 0;
        
        while(B[matchingChars] != '\0' && A[currentPosition + matchingChars] == B[matchingChars]){
                matchingChars++;
            }
        
    
            if (matchingChars == sizeB){
                numOccurences++;
                printf("(%d,%d) ", currentPosition + 1, currentPosition + sizeB);
            }

            currentPosition++;
        
    }
    return numOccurences;
}


int main(){

    char A[] = "Banana";
    char B[] = "an";
    int Matches = 0;
    Matches = substrings(A,B);
    printf("\n %d Matches\n", Matches);
    return 0;
}
