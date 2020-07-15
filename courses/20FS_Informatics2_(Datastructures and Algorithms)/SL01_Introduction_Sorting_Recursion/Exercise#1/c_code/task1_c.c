#include <stdio.h>

int strLength(char s[]){
	int i = 0;
	
	while (s[i] != '\0')
		i++;
	
	return i;
}

void main(){
	char s[1001];
	int length;

	printf("Please enter a string: ");
	scanf("%[^\n]s", s);
	length = strLength(s);
	printf("String Length: %d\n", length);
}
// Linux, Mac: gcc task1.c -o task1; ./task1
// Windows: gcc task1.c -o task1; task1

