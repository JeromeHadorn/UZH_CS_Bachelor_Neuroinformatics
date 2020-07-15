A **binary search tree** is a binary tree where the nodes are ordered in a specific way.

Binary search tree (and its variants) are used heavily since they allow to quickly find values in a large set of values.

**Tree Search**
```C
void TreeSearchIterative(struct node* p,int value){
    while(t != NULL && p->key != NULL){
        if(v < p->key){
            p = p->left;
        } else {
            p = p->right;
        }
    }
    return p;
}

void TreeSearchRecurisve(struct node* p, int value){
    if(p == NULL || p->key == value){
        return p;
    }

    if(value < p->key){
        return TreeSearchRecursive(p->left, value);
    } else {
        return TreeSearchRecursive(p>right, value);
    }
}
```

**Analysis of tree search**
* Running time on tree of height $h$ is $O(h)$
* In the worst case $h$ is the number of nodes

**Finding the minimum**
* Finds the minimum key in a tree rooted at p
* Running time is proportional to height of tree
* We do not have to compare keys.

```c
void TreeMin(struct node* p){
    while(p->left != NULL){
        p = p->left;
    }
    return p;
}
```