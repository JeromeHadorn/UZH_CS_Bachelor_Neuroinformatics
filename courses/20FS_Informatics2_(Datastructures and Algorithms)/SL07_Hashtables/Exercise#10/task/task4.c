#include <stdio.h>
#include <stdlib.h>
#include <math.h>

#define m 8

struct element {
  int val;
  struct element *next;
};

struct element* H[m];

void init() {
  int i;
  for (i = 0; i < m; i++)
    H[i] = NULL;
}

int h(int val) {
  float A=(sqrt(7)-1)/2;
  return m*(A*val - (int)(A*val));
}

void insert(int val) {
  int i = h(val);
  struct element* e = malloc(sizeof(struct element));

  e->val = val;
  e->next = H[i];
  H[i] = e;
}

struct element* search(int val) {
  int hkey = h(val);
  struct element *e = H[hkey];
  while (e != NULL) {
    if (e->val == val) { return e; }
    else { e = e->next; }
  }

  return NULL;
}

void printHash() {
  struct element *e;
  int i;

  printf("Table size: %d\n", m);
  for (i = 0; i < m; i++) {
    if (H[i] != NULL) {
      printf("i: %d\t val:", i);
      e = H[i];
      while (e != NULL) {
        printf(" -> %d", e->val);
        e = e->next;
      }
      printf("\n");
    }
  }
}

int main () {
  struct element* tmp;
  int i;

  init();
  insert(111);
  insert(10112);
  insert(1113);
  insert(5568);
  insert(63);
  insert(1342);
  insert(21231);

  printHash();
  
  int searchValues[] = {1, 10112, 1113, 5568, 337};
  for (i = 0; i < 5; i++) {
    tmp = search(searchValues[i]);
    if (tmp==NULL) printf("Searching for %d, not found\n", searchValues[i]);
    else printf("Searching for %d, found %d\n", searchValues[i], tmp->val);
  }

  return 0;
}
// Linux, Mac: gcc task4.c -o task4; ./task4
// Windows: gcc task4.c -o task4; task4
