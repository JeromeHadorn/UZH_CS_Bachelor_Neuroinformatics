#include <stdlib.h>
#include <stdio.h>
#include <string.h>

struct list {
  struct node* head;
  struct node* tail;
};

struct node {
  int val;
  struct node* next;
};

struct list* init() {
  struct list* l = malloc(sizeof(struct list));

  l->head = NULL;
  l->tail = NULL;
  return l;
}

void appendAtHead(struct list* listA, int val) {
	struct node* new = malloc(sizeof(struct node));

	new->val = val;
	if (listA->head == NULL){
		listA->head = new;
		listA->tail = new;
		listA->tail->next = listA->head;
	}
	else {
		new->next = listA->head;
		listA->head = new;
		listA->tail->next = new;
	}
}

void appendAtTail(struct list* listA, int val) {
	struct node* new = malloc(sizeof(struct node));

	new->val = val;
	if (listA->head == NULL){
		listA->head = new;
		listA->tail = new;
		listA->tail->next = listA->head;
	}
	else {
		new->next = listA->head;
		listA->tail->next = new;
		listA->tail = new;
	}
}

int size(struct list* listA) {
	int i = 0;
	struct node* curr = listA->head;

	if (curr != NULL){
		while (curr->next != listA->head) {
			i++;
			curr = curr->next;
		}
	}
	else{
		i = 0;
	}
	return i+1;
}

void printArray(int a[], int size) {
    int i;
    for(i = 0; i < size; i++) { printf("%d", a[i]); }
}

void print(struct list* listA) {
	struct node* curr = listA->head;
  int n = size(listA);
  int i = n-1;
  int arr[n];

	if (curr != NULL){
		while (curr -> next != listA->head) {
      arr[i] = curr->val;
      i--;
			curr = curr->next;
		}
    arr[i] = curr->val;
	}
  printArray(arr, n);
}



struct list* addTwoLists (struct list* numA, struct list* numB) {
  struct list* res = init();
  struct node* first = numA->head->next;
  struct node* second = numB->head->next;
  int a = numA->head->val, b=numB->head->val;
  int carry = 0, sum;

  sum = carry + a + b;
  if (sum >= 10) carry = 1;
  else carry = 0;

  sum = sum % 10;
  appendAtTail(res, sum);

  while (first != numA->head || second != numB->head) {
    if (first!=numA->head) a = first->val;
    else a = 0;
    if (second!=numB->head) b = second->val;
    else b = 0;
    
    sum = carry + a + b;

    if (sum >= 10) carry = 1;
    else carry = 0;

    sum = sum % 10;
    appendAtTail(res, sum);

    if (first != numA->head) first = first->next;
    if (second != numB->head) second = second->next;
  }

  if (carry > 0) {
    appendAtTail(res, 1);
  }
  res->tail->next = res->head;

  return res;
}

int main() {
  struct list* a = init();
  struct list* b = init();
  struct list* res = NULL;
  // first list: 91
  appendAtHead(a, 9);
  appendAtHead(a, 1);
  // second list: 1249
  appendAtHead(b, 1);
  appendAtHead(b, 2);
  appendAtHead(b, 4);
  appendAtHead(b, 9);
  res = addTwoLists(a, b);
  printf("Sum of ");
  print(a);
  printf(" and ");
  print(b);
  printf(" = ");
  print(res);
  printf("\n");

  return 0;
}

// Linux, Mac: gcc task4.c -o task4; ./task4
// Windows: gcc task4.c -o task4; task4
