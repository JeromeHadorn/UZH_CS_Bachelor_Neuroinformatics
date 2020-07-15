#include <stdlib.h>
#include <stdio.h>

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

void appendAtPosition(struct list* listA, int val, int i) {

	if (i < 0 || i > size(listA)) {
		return;
	}

	if (i == 0) {
		appendAtHead(listA, val);
		return;
	}

	if (i == size(listA)) {
		appendAtTail(listA, val);
		return;
	}

	int n = 0;

	struct node* curr;
	struct node* new = malloc(sizeof(struct node));

	new->val = val;
	new->next = NULL;

	curr = listA->head;
	while (n + 1 < i)
	{
		n++;
		curr = curr->next;
	}
	new->next = curr->next;
	curr->next = new;
	
}

void print(struct list* listA) {
	struct node* curr = listA->head;

	printf("[ ");
	if (curr != NULL){
		while (curr -> next != listA->head) {
			printf("%d ", curr->val);
			curr = curr->next;
		}
		printf("%d ", curr->val);
	}
	printf("]\n");
}

void deleteVal(struct list* listA, int val) {
	struct node* toDelete;
	struct node* prev = listA->head;

	if (prev != NULL) {
		while (prev->next != listA->head) {
			if (prev == listA->head && prev->val == val) {
				toDelete = prev;
				listA->head = prev->next;
				listA->tail->next = listA->head;
				prev = prev->next;
				free(toDelete);
			}
			else {
				if (prev->next->val == val) {
					toDelete = prev->next;
					prev->next = prev->next->next;
					if (toDelete == listA->tail){
						listA->tail = prev;
					}
					free(toDelete);
				}
				else {
					prev = prev->next;
				}
			}
		}
	}
}

void delete(struct list* listA, int i) {
	struct node* toDelete;
	struct node* prev;
	int c;

	if (i < 0 || i > size(listA) || size(listA)==0) {
		return;
	}

	if (i == 0) {
		if (listA->head != NULL) {
			toDelete = listA->head;
			listA->head = listA->head->next;
			listA->tail->next = listA->head;
			free(toDelete);
		}
	}
	else {
		c = 1;
		prev = listA->head;
		while (c < i) {
			c++;
			prev = prev->next;
		}
		if (c==i){
			toDelete = prev->next;
			prev->next = prev->next->next;
			if (toDelete == listA->tail){
				listA->tail = prev;
			}
			free(toDelete);
		}
	}
}


int main() {
	struct list* l = init();
	appendAtHead(l, 0);
	appendAtHead(l, 2);
	appendAtHead(l, 1);
	appendAtHead(l, 3);
	appendAtHead(l, 5);
	appendAtHead(l, 4);
	appendAtHead(l, 9);
	print(l);
	delete(l, 6);
	delete(l, 3);
	delete(l, 0);
	print(l);
	appendAtHead(l, 9);
	appendAtHead(l, 4);
	appendAtHead(l, 5);
	appendAtTail(l, 3);
	appendAtTail(l, 1);
	appendAtTail(l, 2);
	appendAtTail(l, 0);
	print(l);
	appendAtPosition(l, 7, 4);
	print(l);
	delete(l, 0);
	delete(l, 3);
	delete(l, 6);
	print(l);
	deleteVal(l, 0);
	print(l);

	return 0;
}
// Linux, Mac: gcc task3.c -o task3; ./task3
// Windows: gcc task3.c -o task3; task3
