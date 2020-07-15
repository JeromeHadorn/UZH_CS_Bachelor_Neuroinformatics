#include <stdio.h>

/*
Task 1. Write a C program with a function int strLength(char s[]) that determines the length of string s. Assume that all strings are at most 1000 characters long. Your program should prompt the user for an input string, read the string (terminated by a newline), and print the length of the input string to the screen. Do not use any build-in library functions to calculate the length of the string. An input/output example is illustrated below (the user input is typeset in bold):

 Please enter a string: **Hello World**
 String Length: **11**
*/

int strLength(char s[1000]);

int main (){
    char str[1000];
    printf("Please enter a string: ");
    scanf("%s", str);
    
    int res;
    res = strLength(str);
    
    printf("String Length: %d\n", res);
    return 0;
}

int strLength(char s[1000]){

int counter = 0;
for (int i = 0; s[i] != 0; i++){
    counter += 1;
}
    return counter;
}