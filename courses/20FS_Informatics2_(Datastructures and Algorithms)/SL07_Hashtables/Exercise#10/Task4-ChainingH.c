#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#define m 7

struct element {
    int val;
    struct element *next;
};

struct element* H[m];

void init(){
    int i;
    for(i=0;i<m;i++){
        H[i] = NULL;
    }
}

int h(int val){
    float A = (sqrt(7)-1)/2;
    return m*(A*val -(int)(A*val));
}

struct element* search(int val){
    int hkey= h(val);
    struct element *e = H[hkey];
    while(e != NULL){
        if(e->val == val){
            return e;
        } else {
            e = e->next;
        }
    }
    return NULL;
}

void insert(int val){
    int i= h(val);
    struct element* e = malloc(sizeof(struct element));

    e->val = val;
    e->next = H[i];
    H[i] = e;
}

void printHash(){
    struct element *e;

    int i;

    printf("tablesize %d\n", m);
    for(i=0;i<m;i++){
        if(H[i] != NULL){

            printf("i %d\t val", i);
            e=H[i];
            while(e != NULL){
                printf(" -> %d", e->val);
                e = e->next;
            }
            printf("\n");
        }
    }
}
int main(){
    int i;
    init();
    insert(111);
    insert(10122);
    insert(1113);
    insert(5568);
    insert(63);
    insert(1342);
    insert(21231);
    printHash();

    int searchValues[] = {1, 10112, 1113, 5568, 337};
    struct element* tmp;
    for(i=0;i<5;i++){
        tmp = search(searchValues[i]);
        if (tmp==NULL) {
            printf("Searching for %d, not found\n", searchValues[i]);
        } else{
            printf("Searching for %d, found %d \n", searchValues[i], tmp->val);
    }
    }
    return 0;
}
