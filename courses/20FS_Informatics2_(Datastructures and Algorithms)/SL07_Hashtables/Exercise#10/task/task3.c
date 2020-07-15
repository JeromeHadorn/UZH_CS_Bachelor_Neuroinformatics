#include <math.h>
#include <stdio.h>

#define m 7

void init(int A[]) {
    int i;
    for(i = 0; i < m; i++) {
        A[i] = 0;
    }
}

int h(int k, int i) {
    int h1 = (k % m) + 1;
    int h2 = (m-1)-(k % (m-1));

    return (int)(h1 + i * h2) % m;
}

int search(int A[], int key) {
    int counter = 0;
    int hkey;
    do {
        hkey = h(key, counter);
    } while(A[hkey] != key && A[hkey] != 0 && counter++ < m);
    if(A[hkey] == key) {
        return hkey;
    } else {
        return -1;
    }
}

void insert(int A[], int key) {
    int counter = 0;
    int hkey;
    do {
        hkey = h(key, counter);
    } while(A[hkey] != 0 && counter++ < m);
    A[hkey] = key;
}

void printHash(int A[]) {
    int i;
    printf("Table size: %d\n", m);
    for(i = 0; i < m; i++) {
        if(A[i] != 0) {
            printf("i: %d\tkey: %d\n", i, A[i]);
        }
    }
}

int main() {
    int A[m];
    init(A);

    insert(A, 1313);
    insert(A, 1314);
    insert(A, 1315);

    insert(A, 2000);
    insert(A, 2001);
    insert(A, 2002);

    printHash(A);

    int searchValues[] = {2000, 10, 1314, 1313, 337};
    int i;
    for(i = 0; i < 5; i++) {
        if (search(A, searchValues[i]) == -1) {
            printf("Searching for %d, not found\n", searchValues[i]);
        }
        else {
            printf("Searching for %d, found %d\n", searchValues[i], search(A, searchValues[i]));
        }
    }

    return 0;
}

// Linux, Mac: gcc task3.c -o task3; ./task3
// Windows: gcc task3.c -o task3; task3