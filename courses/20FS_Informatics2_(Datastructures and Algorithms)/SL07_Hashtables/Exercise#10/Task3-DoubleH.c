#include <stdio.h>
#include <stdlib.h>

#define m 7

void init(int A[]){
    int i;
    for(i=0; i<m;i++){
        A[i] = 0; 
    }
}

int h(int k, int i){
    int h1 = (k % m) + 1;
    int h2 = (m-1) - (k % (m-1));

    return (int)(h1 + i*h2) % m;
}

void insert(int A[], int key){
    int hkey; int counter = 0;
    do {
        hkey = h(key, counter);
        counter += 1;
    } while (A[hkey] != 0 && counter < m);
    A[hkey] = key;
}

int search(int A[], int key){
    int hkey; int counter = 0;
    do {
        hkey = h(key, counter);
    } while (A[hkey] != 0 && A[hkey] != key && counter++ < m);
        if (A[hkey] == key){
            return hkey;
        } else {
            return -1;
        }    
}

void printHash(int A[]){
    int i;
    printf("table size %d\n", m);
    for(i =0; i<m;i++){
        if (A[i] != 0){
            printf("%d\n", A[i]);          
        }
        
}}


int main(){
    int A[m];
    init(A);
    insert(A, 1313);
    insert(A, 1314);
    insert(A, 1315);
    insert(A, 2000);
    insert(A, 2001);
    insert(A, 2002);

    printHash(A);


    int valuesToSearch[] = {2000, 10, 1314, 1313, 337};
    for(int i = 0; i < 5; i++){
        int searchresult = search(A, valuesToSearch[i]);

        if (searchresult == -1){
            printf("nope not there\n");
        } else {
            printf("Found %d at index %d \n", valuesToSearch[i], searchresult);
        }
    }


    return 0;
}
