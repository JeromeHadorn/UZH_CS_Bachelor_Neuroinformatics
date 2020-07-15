#include <stdio.h>

void generate(char str[], int k, int n){
    if (k == n){
        str[n]= '\0';
        printf("%s ", str);
        return;
    }

    if (str[n-1] == '1'){
        str[n] = '0';
        generate(str, k, n+1);
    } else{
        str[n] = '0';
        generate(str, k, n+1);

        str[n] = '1';
        generate(str, k, n+1);
    }
}

void generateBinaryString(int k){
    if (k<=0){
        return;
    }

    char str[k+1];
    
    //Start with 0
    str[0] = '1';
    generate(str,k,1);

    // Start with 1
    str[0] = '0';
    generate(str,k,1);

}


int main(){
    int k;
    scanf("%d", &k);
    generateBinaryString(k);
    return 0;
}
