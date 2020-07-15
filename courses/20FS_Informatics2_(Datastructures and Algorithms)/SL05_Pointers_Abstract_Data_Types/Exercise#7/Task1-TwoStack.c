#include <stdio.h>
#include <stdlib.h>

typedef struct stackADT {
    int *arr;
    int size;
    int top1, top2;
} twoStack;

void intialize(twoStack *s, int n){
    s->size=n;
    s->arr = malloc(n*sizeof(int));
    s->top1 = -1;
    s->top2 = n;
}

void push1(twoStack *s, int value){
    if (s->top1 < s->top2){
        s->top1++;
        s->arr[s->top1] = value;
    } else {
        printf("Stack full");
    }
}

void push2(twoStack *s, int value){
    if (s->top1 < s->top2){
        s->top2--;
        s->arr[s->top2] = value;
    } else {
        printf("Stack full");
    }
}

int pop1(twoStack *s){
    if (s->top1 >= 0){   
        int x = s->arr[s->top1];
        s->top1--;
        return x;
    } else {
        printf("Stack Underflow");
        return -1;
    }
}

int pop2(twoStack *s){
    if (s->top1 < s->size){   
        int x = s->arr[s->top2];
        s->top2++;
        return x;
    } else {
        printf("Stack Underflow");
        return -1;
    }
}

void printStack(twoStack *s){
    if (s->size > 0){
        int i;
        printf("[");
        for (i=0;i <= s->size-1;i++){
            printf("%d ", s->arr[i]);
        }
        printf("]\n");
    }
}

int main(){
    twoStack *s = malloc(sizeof(twoStack));
    intialize(s, 5);
    push1(s, 5);
    push2(s, 10);
    push2(s, 15);
    push1(s, 11);
    push2(s, 7);
    printStack(s);
    printf("%d\n", pop1(s));
    printf("%d\n", pop2(s));
    push1(s, 27);
    push1(s, 92);
    printStack(s);
    return 0;
}