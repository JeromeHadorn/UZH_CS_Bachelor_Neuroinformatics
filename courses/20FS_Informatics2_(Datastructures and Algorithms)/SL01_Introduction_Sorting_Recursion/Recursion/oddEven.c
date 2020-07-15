#include <stdio.h>

int even(n){
    return (n == 0 || odd(n-1));
}

int odd(n){
    // doesn't handle negatives return (n > 0 && even(n-1));
    return ((n < 0 && odd(-1 * n)) || (n>0 && even(n-1)));
}

int main(){
    printf("is 10 odd? %d \n", odd(-10));
    printf("is 10 even? %d \n", even(-10));
    printf("is 11 odd? %d \n", odd(-11));
    printf("is 11 even? %d \n", even(-11));
    return 0;
}
