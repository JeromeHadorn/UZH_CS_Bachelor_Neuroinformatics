# Summary SL05 - Abstract Data Types & Pointers
## Dynamic data structures
### Pointer
Informal definition of pointers:
* A common technique is to allocate storage space dynamically
* That means the storage space (memory) is allocated during runtime
* Compiler reserves space only for addresses to these dynamic parts
* These addresses are usually called pointers

**Pointer** points to an address.

#### Pointers in C
To follow (chase, dereference) a pointer we write `*p`
```c
    *p = 12
```
<br>

To get the address of a variable `i` we write `&i`
```c
    p = &i
```
<br>

To allocate memory we use `malloc(sizeof(Type))`
```c
p = malloc(sizeof(int))
```
<br>

To free storage space pointed to by a pointer p we use `free`
```c
free(p)
```
<br>

Declaring a pointer to type `T` we write `T*`
```c
int* p
```



`*` is used for two purposes:
* Declaring a pointer variable
    ```c
    int* p
    ```
* Following a pointer
    ```c
    *p = 15
    ```
### Linked lists
* A list of integer $root -> 3 -> 4->5-|$

```c
struct node {
    int val;    //value
    struct node* next; // pointer
}

struct node* root; //starting point
```

**Accessing a field:**
```c
(*p).a
// or more conveninet
p->a
```

**Creating List 88-> 52->12-|**
```c
root = malloc(sizeof(struct node)); 
root->val = 88;
root->next = malloc(sizeof(struct node));

p = root->next;
p->val = 52;
p->next = malloc(sizeof(struct node));

p = p->next;
p->val = 12;
p->next = NULL;
```
#### Doubly linked list
Variants of linked lists
* Lists with explicit tail
    * Do have an extra pointer to the last item of the list
    * No need to scan the entire list if an operation applies only to the last item

* Doubly linked list
    * Each node has a field with a pointer to the previous node of the linked list
    * Provides means to quickly navigate forth and back in the linked list
## ADT: abstract data types
An abstract data type is a mathematical model that defines a data type by its behavior from the point of view of a user (in terms of possible values, possible operations, and the behavior of operations).

It is equipped with a specific interface, i.e., a collection of signatures for the operations that can be invoked on an instance

Furthermore, it is equipped with a set of axioms (pre- and postconditions) that define the semantics of each operation (i.e. what the operations do to instances of the ADT, but not how)


Similarity with OO-paradigm
* ADT = instance variables + procedures
* Class = instance variables + methods

Some popular examples
* Stacks & queues
    * LIFO vs. FIFO principle
* Priority queues
    * Another application of heaps
* Ordered lists
    * Linked lists where items are ordered according to a key

### Stacks
Properties of stacks
* In a stack, insertion and deletion follow the last-in, first-out (LIFO) principle
* Hence, the item that has been in the stack for the shortest time is deleted first
    * Example: elimination of recursion
* Implemented by a data structure where items are
    * inserted at the end/beginning (push)
    * removed from the end/beginning (pop)
* Appropriate data structures for their implementation
    * arrays (end) or singly linked lists (beginning)


We design a solution for a single stack (i.e., stack is implicit; not a parameter in operations)

**Array implementation**
* Inserting and removing items from a stack
```c 
void push(x)
    S[t] = x;
    t = t+1;
```
```c
int pop()
    t = t-1;
    return S[t];
```

* The stack is implemented by an array S[1..n] of length n
* The variable $t$ functions as pointer to top of the stack
* $S$ and $t$ are global variables.
* Notice that if **t = 1** then the stack is actually empty
* Error checking for under/overflow has been omitted
### Queues
**Properties of queues**
* In a queue, insertion and deletion follow the first-in, first-out (FIFO) principle
* Hence, the item that has been in the queue for the longest time is deleted first
    * Example: managing jobs of a printer
* Implemented by a data structure where items are
    * inserted at the end/beginning (enqueue)
    * removed from the beginning/end (dequeue)
* Appropriate data structures for their implementation
    * arrays or singly linked lists with an explicit tail (handy for dequeuing)
    
We design a solution for a single queue (i.e., queue is implicit; not a parameter in operations)

**Enqueue and Dequeue**
```c
void enqueue(int x){
    Q[t] = x;
    t = t+1 mod n;
}

int dequeue(){
    int i = h;
    h = h+1 mod n;
    return Q[i];
}
```
* The queue is implemented by an array $Q[0..n − 1]$ of length $n$ used in **circular fashion**
* Variables $h$ and $t$ function as pointers to head and tail of the queue
* Notice that if $h = t$ then the queue is actually empty
### Ordered Lists
* In an ordered list elements are ordered according to a key
* We design a solution for multiple ordered queues (the ordered queue is a parameter in operations)
* all arguments in procedures and functions are copies
    * give a copy of doc to somebody
    * copy is changed
    * original is still unchanged
* `node** l`- pointer to a pointer to a node, why? ensures that l never changes

```c
struct node {
    int val;
    struct node* next;
};
struct node** init() {
    struct node **l;
    l = malloc(sizeof(struct node**));
    *l = NULL;
    return l;
}

int first(struct node** l) {
    if (*l == NULL) return -1;
    else return (*l)->val;
}

void insert(struct node** l, int x) { 
    struct node* p;
    struct node* q;
    if (*l == NULL || (*l)->val > x) {
        p = malloc(sizeof(struct node));
        p->val = x;
        p->next = *l;
        *l = p;
    } else {
        p = *l;
        while (p->next != NULL && p->next->val < x){
            p = p->next;
        }
        q = malloc(sizeof(struct node)); 
        q->val = x;
        q->next = p->next;
        p->next = q;    
    }
}

struct node* root1;
struct node* root2;
```