#include <stdio.h>
#include <stdlib.h>

struct TreeNode {
    int val;
    struct TreeNode* left;
    struct TreeNode* right;
};

void insert(struct TreeNode** root, int val){
    struct TreeNode* newTreeNode = NULL;
    struct TreeNode* prev = NULL;
    struct TreeNode* current = *root;
    
    newTreeNode = malloc(sizeof(struct TreeNode));
    newTreeNode->val = val;
    newTreeNode->left = NULL;
    newTreeNode->right = NULL;

    while(current != NULL){

        prev = current;

        if (val < current->val){
            current = current->left;
        } else {
            current = current->right;
        }
    }

    if (prev == NULL){
        *root = newTreeNode;
    } else if (val < prev->val){
        prev->left = newTreeNode;
    } else {
        prev->right = newTreeNode;
    }
}
struct TreeNode* search(struct TreeNode* root, int val){
    struct TreeNode* current = root;
    while(current != NULL && current->val != val){
        if (val < current->val){
            current = current->left;
        } else {
            current = current->right;
        }
    }
    return current;
}
void delete(struct TreeNode** root, int val){
    struct TreeNode* x = search(*root, val);
    if(x == NULL){
        return;
    }
    
    struct TreeNode* u = *root; // the node to be deleted
    struct TreeNode* v = NULL; // the node before

    while (u != x){
        v = u;
        if (x->val < u->val){
            u = u->left;
        } else {
            u = u->right;
        }
    }

    if (u->right == NULL){
        // Root Check
        if(v == NULL){
            *root = u->left;
        } else if(v ->left == u){
            v->left = u->left;
        } else {
            v->right = u->right;
        }

    } else if (u->left == NULL){
        // Root Check
        if(v == NULL){
            *root = u->right;
        } else if(v ->left == NULL){
            //TODO: understand this if block
            v->left = u->right;
        } else {
            v->right = u->right;
        }

    } else {
        //TODO: understand this block
        struct TreeNode* p = x->left;
        struct TreeNode* q = p;
        while(p->right != NULL){
            q = p;
            p = p->right;
        }


        // Root Check
        if(v == NULL){
            *root = p;
        } else if (v->left == u){
            v->left = p;
        } else {
            v->right = p;
        }

        p->right = u->right;
        if(q != p){
            q->right = p->left;
            p->left = u->left;
        }
    }
}
void printTreeRecursive(struct TreeNode *root){
    if (root == NULL){
        return;
    }
    if (root->left != NULL){
        printf("__%d__%d\n", root->val, root->left->val);
        printTreeRecursive(root->left);
    }   
    if (root->right != NULL){
        printf("__%d__%d\n", root->val, root->right->val);
        printTreeRecursive(root->right);
    }
}

void printTree(struct TreeNode *node){
    printf("graph_g_{\n");
    printTreeRecursive(node);
    printf("}\n");
}

struct TreeNode* maximum(struct TreeNode* root){
    struct TreeNode* current = root;
    while(current->right != NULL){
        current = current->right;
    }
    return current;
}
struct TreeNode* minimum(struct TreeNode* root){
    struct TreeNode* current = root;
    while(current->left != NULL){
        current = current->left;
    }
    return current;
}


int distanceToRoot(struct TreeNode* root, int val){
    if(root->val == val) return 0;
    else if(root->val > val) return 1 + distanceToRoot(root->left, val);
    else return 1 + distanceToRoot(root->right, val);
}

int main(){
    struct TreeNode* root = malloc(sizeof(struct TreeNode));
    insert(&root, 4);
    insert(&root, 2);
    insert(&root, 3);
    insert(&root, 8);
    insert(&root, 6);
    insert(&root, 7);
    insert(&root, 9);
    insert(&root, 12);
    insert(&root, 1);

    printTree(root);
    
    printf("min val %d \n", minimum(root)->val);
    
    printf("distance to root from root to val 7 %d \n", distanceToRoot(root, 7));

    printf("Deleting: 4, 12, 2\n");

    delete(&root, 4);
    delete(&root, 12);
    delete(&root, 2);

    printTree(root);

    printf("max val %d \n", maximum(root)->val);

    printf("distance to root from root to val 6 %d \n", distanceToRoot(root, 6));


    return 0;
}