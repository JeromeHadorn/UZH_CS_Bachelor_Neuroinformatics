#include <stdio.h>
#include <stdbool.h>

int strLength(char s[]){
	int i = 0;
	
	while (s[i] != '\0')
		i++;
	
	return i;
}

bool isPalindrome(char s[]) {
	int c, i, sLength;
	c = 0;
    
    sLength = strLength(s);
	for (i = 0; i < sLength/2; i++){
		if (s[i] == s[sLength-i-1]){
			c++;
		}
	}
	
	if (c == sLength/2) {
		return true;
	}
	
	return false;
}


void main() {
	bool palindromeCheck;
	
	char s[1001];

	printf("Please enter a string to check if it is palindrome: ");
	scanf("%[^\n]s", s);
	palindromeCheck = isPalindrome(s);

	if (palindromeCheck){
		printf("Result string: %s\n", "TRUE");
	}	
	else {
		printf("Result string: %s\n", "FALSE");
	}
}
// Linux, Mac: gcc task2.c -o task2; ./task2
// Windows: gcc task2.c -o task2; task2
