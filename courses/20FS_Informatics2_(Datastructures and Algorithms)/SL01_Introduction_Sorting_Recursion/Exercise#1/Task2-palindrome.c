/*
Task 2. Write a C program with a function bool isPalindrome(char s[]) that determines whether a string is a palindrome or not. A palindrome is a string that reads the same backwards as forwards. You can use function strLength(char s[]) written in Task 1 to determine the string length. Your program should prompt the user to type input string and then should print “TRUE” if it is a palin- drome or “FALSE” if it isn’t. An input/output example is illustrated below (input is typeset in bold):

 
 Please enter a string to check if it is palindrome: wow
 
 Result string: TRUE
*/

#include <stdio.h>

int strLength(char s[1000]);
int isPalindrome(char s[1000]);

int main(){
    char str[1000];
    printf("Please enter a string to check if it is palindrome: ");
    scanf("%s", str);

    int res;
    res = isPalindrome(str);
 
    printf("Result String: %d\n", res);
    return 0;

}

int isPalindrome(char s[1000]){
	int length = strLength(s);
	for (int i = 0; i < (length/2); i++){

		if (s[i] != s[length-1-i]) {
			return 0;
		}
	}
	return 1;
}

int strLength(char s[1000]){

int counter = 0;
for (int i = 0; s[i] != 0; i++){
    counter += 1;
}
    return counter;
}
