#include <stdio.h>
#include <stdlib.h>

struct queue{
    struct node* head;
    struct node* tail;
};

struct node{
    int data;
    struct node* next;
};

struct queue* initialize(){
    struct queue* q = malloc(sizeof(struct queue));

    q->head = NULL;
    q->tail = NULL;
    return q;
}

void enQueue(struct queue *q, int value){
    struct node *temp = malloc(sizeof(struct node));
    temp->data = value;
    if (q->head == NULL){
        q->head = temp;
    } else {
        q->tail->next = temp;
    }

    q->tail = temp;
    q->tail->next = q->head;
}

int deQueue(struct queue *q){
    if (q->head == NULL){
        printf("Queue is empty\n");
        return -1;
    }

    int value;
    //Checking if the last node to be deleted is the head as well
    if (q->head == q->tail){
        value = q->head->data;
        free(q->head);
        q->head = NULL;
        q->tail = NULL;
    } else {
        struct node *temp = q->head;
        value = temp->data;
        q->head = q->head->next;
        q->tail->next = q->head;
        free(temp);
    }
    return value;
}

void displayQueue(struct queue *q){
    struct node *temp = q->head;
    printf("[");
    while(temp->next != q->head){
        printf("%d ", temp->data);
        temp = temp->next;
    }
    printf("%d ]\n", temp->data);
}

int main(){
    struct queue *q = initialize();
    enQueue(q, 14);
    enQueue(q, 22);
    enQueue(q, 6);
    displayQueue(q);
    printf("%d first dequeue\n", deQueue(q));
    printf("%d second dequeue\n", deQueue(q));
    displayQueue(q);
    enQueue(q, 9);
    enQueue(q, 20);
    displayQueue(q);
    return 0;
}