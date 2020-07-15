#include <stdlib.h>
#include <stdio.h>

#define black 0
#define red 1

struct rb_node {
  int key;
  int color;
  struct rb_node* left;
  struct rb_node* right;
  struct rb_node* parent;
};

struct rb_tree {
  int bh;
  struct rb_node *root;
  struct rb_node *nil;
};

struct rb_tree* rb_initialize() {
  // your implementation goes here
}

void rb_leftRotate(struct rb_tree* T, struct rb_node* x) {
  // your implementation goes here
}

void rb_rightRotate(struct rb_tree* T, struct rb_node* y) {
  // your implementation goes here
}

struct rb_node* rb_insertFixup(struct rb_tree* T, struct rb_node* z) {
  // your implementation goes here
}

void rb_insert(struct rb_tree* T, int key) {
   // your implementation goes here
}

struct rb_node* rb_search(struct rb_tree* tree, int q) {
    struct rb_node* x = tree->root;

    if (x == tree->nil)
        return x;
    while (x->key != q) {
        if (q < x->key)
            x = x->left;
        else
            x = x->right;
        if (x == tree->nil)
            return x;
    }
    return x;
}

void rb_printRecursive(struct rb_node *root, struct rb_tree *tree) {
  if (root == tree->nil) {
    return;
  }
  rb_printRecursive(root->left, tree);
  printf(" %d (%s) -- %d\n", root->key, (root->color==red?"RED":"BLACK"),
         root->left->key);
  rb_printRecursive(root->right, tree);
  printf(" %d (%s) -- %d\n", root->key, (root->color==red?"RED":"BLACK"),
         root->right->key);
}

void rb_print(struct rb_tree *tree) {
  printf("graph g {\n");
  rb_printRecursive(tree->root, tree);
  printf("}\n");
}

int main(int argc, char **argv) {
  struct rb_tree *T;

  T = rb_initialize();
  rb_insert(T, 5);
  rb_insert(T, 90);
  rb_insert(T, 20);
  rb_print(T);
  rb_rightRotate(T, rb_search(T, 90));
  rb_leftRotate(T, rb_search(T, 5));
  rb_print(T);
  rb_insert(T, 60);
  rb_insert(T, 30);
  rb_print(T);
  rb_rightRotate(T, rb_search(T, 90));
  rb_print(T);
  return 0;
}
// Linux, Mac: gcc task3_framework.c -o task3_framework; ./task3_framework
// Windows: gcc task3_framework.c -o task3_framework; task3_framework