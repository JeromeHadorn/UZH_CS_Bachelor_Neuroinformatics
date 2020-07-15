#include<stdio.h>

void copy_string(char *target, char *source){
    while(*source){
        *target = *source;        
        source++;        
        target++;
    }    
    *target = '\0';
}

int main(){
    char source[100], target[100];    
    printf("Enter source string\n");    
    scanf("%[^\n]s", source);
    copy_string(target, source);    
    printf("Target string is \"%s\"\n", target);    
    return 0;
}
// Linux, Mac: gcc task2.c -o task2; ./task2
// Windows: gcc task2.c -o task2; task2
