# Summary SL06 Trees & Red/Black Trees
## Dictionaries
A dictionary D is a dynamic data structure with the following operations (items have key and data part)
* $search (D, v)$: searches for v in D and, eventually, returns a pointer x such that $x.key = v$
* $delete (D, x)$: deletes item pointed to by x from D
* $insert (D, x)$: inserts item pointed to by x into D

Furthermore, one may want to support the following operations (which require that keys are comparable)
* $minimum (D)$ and $maximum (D)$
* $successor (D, v)$ and $predecessor (D, v)$
* (Not always required, Trees support this, hash tables do not support this)
 
**Possible implementations**
Singly linked lists
* Insert and delete: $Θ(1)$
* Search, min, max, succ, and pred: $Θ(n)$
* Ordered lists do not provide a real improvement

Binary search trees
* Binarysearch: $Θ(lgn)$
* Represent search space as a binary tree
* Insert & delete may yield unbalanced search trees

Balanced binary trees
* Cost of operations: $Θ(lgn)$
* Red-black trees as device to keep trees balanced
 
 ## Binary Trees
 Binary Trees are a linked datastructure with the following specifications:
 * For each node x there is (we assume that a node is accessed through a pointer to the node)
    * $x→key$: value of the key (usually an integer value; not necessarily unique)
    * $x→lft$: pointer to left child
    * $x→rgt$: pointer to right child
* root points to the root of the tree
* For a leaf node $p$ we have $p→lft$ = $p→rgt = NIL$

**Inorder Tree Walk**
* Divide-and-conquer algorithm that visits all the nodes of a binary tree
* Running time of In order Tree Walk is linear $(Θ(n))$

```c
// We first go to the left -> middle -> right
void InorderTreeWalk(struct node* p){
    if (p != NULL){
        InorderTreeWalk(p->left);
        VisitNode(p);
        InorderTreeWalk(p->right);
    }
}

void VisitNode(struct node* p){
    printf("%d ", p->value);
}
```

There are alternative ways to walk through a tree
* Preorder: visit node before moving to the children
* Postorder: move to the children before visiting node
* Simply change position of $VisitNode (p)$ in the code
Inorder tree walk can be seen as a projection of the tree nodes onto a one-dimensional interval

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

    if(v < p->key){
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

**Finding the successor**
Given node $p$, find the node with the smallest $key ≥ p→key$
* Case 1 (p→rgt != NIL)
    * successor of $p$ is left-most node in right subtree
* Case 2 (p→rgt = NIL)
    * successor of $p$ is lowest ancestor whose left subtree contains $p$

```c
struct node* SuccAbove(struct node* p, struct node* x){
    struct node succ;
    succ = NULL;
    while (p != x) {
        if (x->key < p->key) { succ = p; p = p->lft; }
        else if (x->key > p->key) { p = p->rgt; }
    }
    return succ;
}
```

**Inserting Items**
Assume that a node p whose left and right children are NIL is given
* Insertion is similar to searching
* To insert the node $p$ into a tree rooted at $root$
    * find location in tree where $p$ belongs to
    * then add the new node p there
* Makes use of a “one step delayed” pointer
* Running time on tree of height $h$ is $O(h)$

Problematic instances
* If items are inserted in order, the tree looks like a list
* That is: height $h = n$, the number of nodes in the tree
* Worst case: the running time of the operations is $O(n)$
```c
struct node* TreeInsert(struct node* p, struct node* r) {
    struct node* y = NULL; // node to be inserted
    struct node* x = r; // root of tree
    
    // We search for place where p must be inserted (x) and the node above (y)
    while (x != NULL) {
        y := x;
        if (x->key < p->key) x = x->rgt
        else x = x->lft;
    }

    if (y == NULL) r = p; //1) insert into empty tree
    else if (y->key < p->key) y->rgt = p; // 2) insert to right of y
    else y->lft = p; // 3) insert to left of y
    
    return r; // in case it changed
}
```


**Deleting Items**
General remark
* Deletion depends on how many children a node has

Deletion: case 1
* Node $t$ has no children: remove $t$

Deletion: case 2
* Node $t$ has one child $x$: let parent of $t$ point to $x$ and then remove t

Deletion: case 3
* Node $t$ has two children: find largest (smallest) child $s$ in left (right) subtree of $t$, then replace $p→key$ with $s.key$ and remove $s$
    * (often this is done by changing pointers (makes it independent of node content))

```c
//Node x is a pointer to the node to be deleted
struct node* delete(struct node* root, struct node* x) {
    u = root;
    v = NULL;
    
    //we search x and the node above
    while (u != x) {
        v = u;
        if (x->key < u->key) u = u->lft;
        else u = u->rgt;
    }

    if (u->rgt == NULL) {
        if (v == NULL) root = u->lft;
        else if (v->lft == u) v->lft = u->lft; else v->rgt = u->lft;
    } else if (u->lft == NULL) {
        if (v == NULL) root = u->rgt;
        else if (v->lft == u) v->lft = u->rgt;
        else v->rgt = u->rgt;
    } else {
        p = x->lft;
        q = p;
        while (p->rgt != NULL) {
            q = p;
            p = p->rgt;
        }

        if (v == NULL) root = p;
        else if (v->lft == u) v->lft = p;
        else v->rgt = p;

        p->rgt = u->rgt;
        if (q != p) {
            q->rgt = p->lft;
            p->lft = u->lft;
        }
    }
    return root
```

**Calculate Height**
```c
int heightBT(struct node* p){
    if (p === NULL) return -1;
    return max(heightBT(p->left), heightBT(p->right)) + 1;
}
```


## Red and Black Trees
**Goal**: balanced tree with a guarantee for the worst case runnign time

Balanced binary trees
* Problem: running time of tree operations is $O(h)$, worst case is $O(n)$
* Solution: balanced search trees guarantee small height $h = O(lg n)$


**Red-black property**
A red-black tree is a binary search tree with the following (additional) properties
1. Every node is either red or black
2. The root is black
3. Every leaf (NIL) is black
4. If a node is red then both its children are black
5. For each node,all paths from the node to descendant leaves
contain the same number of black nodes

Black-height $bh(x)$ of node $x$: number of black nodes on
any path from, but not including, $x$ down to a leaf

Black-height $bh$ of tree: $bh(root)$, black-height of root

Consequences:
* Some Measures
    * n internal nodes
    * h-height of tree
    * bh - black height
* $h/2 ≤ bh$
* $2bh − 1 ≤ n$
* $2h/2 ≤ n + 1$
* $h/2 ≤ lg(n + 1)$
* $h ≤ 2lg(n+1)$ - this is good

* Operations on a binary search tree (search, insert, delete, etc.) are accomplished in $O(h)$ time
* A RB-tree is a binary search tree whose height is bound by $2lg(n+1)$
* Thus, operations are accomplished in $O(lg n)$ time
* Note that there is the following constraint
    * Insertions and deletions may destroy RB-property
    * So, cost for restoring it cannot be more than $O(h)$
 
 ### Rotations
 // TODO: 
 ![](rbt.png)
 ![](rbt-delete.png)