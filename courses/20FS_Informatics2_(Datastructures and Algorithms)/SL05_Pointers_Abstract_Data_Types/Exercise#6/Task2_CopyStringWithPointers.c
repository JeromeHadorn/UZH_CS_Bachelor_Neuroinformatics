#include <stdio.h>


void copy(char* ptr, char* target){
    while (*ptr){
        *(target) = *(ptr);
        ptr++;
        target++;
    }
    *target = '\0';
}



int main(){
    char source[] = "copy this please";
    char target[] = "";
    copy(source, target);
    int i = 0;
    while(target[i] != '\0'){
        printf("%c", target[i]);
        i++;
    }
    printf("\n");
    return 0;
}
