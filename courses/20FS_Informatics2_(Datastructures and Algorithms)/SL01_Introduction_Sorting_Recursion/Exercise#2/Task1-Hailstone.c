#include <stdio.h>

void sequence(int n){
    printf("%d\n",n);
    if (n % 2 == 0 && n != 1){
        return sequence(n/2);
    } else if (n != 1) {
        return sequence(3*n+1);
    }
}

int main(){
    int n;
    scanf("%d", &n);
    sequence(n);
    return 0;
}
