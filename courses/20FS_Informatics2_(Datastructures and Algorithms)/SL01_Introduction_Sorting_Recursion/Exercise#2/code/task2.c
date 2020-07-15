#include <stdio.h>
#include <stdlib.h>


void generate(char str[], int K, int n){
    if (n == K){
        str[n] = '\0' ;
        printf("%s ", str); 
        return;
    }

    if (str[n-1] == '1') {
        str[n] = '0';
        generate(str,K , n+1);
    }

    if (str[n-1] == '0'){
        str[n] = '0';
        generate(str, K, n+1);
        str[n] = '1';
        generate(str, K, n+1);
    }   
}

void generateBinaryStrings(int K){

    if (K <= 0)
    {
        return;
    }

    char str[K];

    // Generate all Binary string starts with '0' 
    str[0] = '0';
    generate( str , K,  1 ) ; 
  
    // Generate all Binary string starts with '1' 
    str[0] = '1' ; 
    generate( str , K, 1 );
    
}

int main (){
    int K;

    printf("Enter the size K: ");
    scanf("%d", &K);

    printf("Possible Binary Strings: ");
    generateBinaryStrings(K);
    printf("\n");

    return 0;	
}
// Linux, Mac: gcc task2.c -lm -o task2; ./task2
// Windows: gcc task2.c -lm -o task2; task2
