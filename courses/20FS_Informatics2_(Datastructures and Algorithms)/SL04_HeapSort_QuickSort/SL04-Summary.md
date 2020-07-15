# Summary: SL04 Heapsort & Quicksort
## Binary Trees
* Each node may have a left or a right **child**.
* Each node has at most one **parent**
* The **root** has no parent
* A **leaf** has no children
* The **depth** (level) of a node x is the length of the path from the root to x
* The **height** of a node x is the length of the longest path from x to  a leaf
* The **right subtree** of a node x is the tree rooted at the right child of x
* The **left subtree** of a node x is the tree rooted at the left child of x
### Complete trees
* A **complete binary tree** is a binary tree where
    * all the leaves have the same depth
    * all internal nodes have two children
* A **nearly complete binary tree** is a binary tree where
    * all levels of non-maximal depth $d$ are full (have $2^{d}$ nodes)
    * all the leaves with maximal depth are as far left as possible
## Heapsort
### Heap
* A binary tree is a (binary) **heap** if and only if
    * it is a nearly complete binary tree and, furthermore,
    * each node is greater than or equal to all its children

**Fundamental Properties**
* Let $i$ be a node index.
* Heap property: `A[parent(i)] >= A[i]`
* A binary heap can be efficiently stored as an array
    * Because it is a nearly complete binary tree.

* Finding parent, left child, and right child:
    ```
        Algo: Parent(i)
        return ⌊i/2⌋;

        Algo: Left(i)
        return 2*i;

        Algo: Right(i)
        return 2*i + 1;
    ```

**Max-Heap** is where the largest element is at the root.
**Min-Heap** is where the smallest element is at the root.
### Heapify
* Heapify takes as **inputs**:
    * Array $A$
    * index $i$ in Array $A$
    * number of heap elements

* Binary trees rooted at left(i) and right(i) are binary heaps
* $A[i]$ may be smaller than its children, thus violating the heap property
* `heapify(A, i, s)` transforms the binary tree rooted at i into a binary heap
* Strategy: move $A[i]$ down the heap until the heap property is satisfied again

```c
void Heapify(int A[], int i, int s){
    int m = i;
    int l = Left(i);
    int r = Right(i);

    // Checks if left exists and if left elements is larger than parent
    if (l < s && A[l] > A[m]){
        m = l;
    }

    // Checks if right exists and if right elements is larger than parent
    if (r < s && A[r] > A[m]){
        m = r;
    }


    if (i != m){
        exchange(A[i], A[m]);
        Heapify(A, m, s);
    }
}
```
**Running Time**
* The running time of heapify on a subtree of size n rooted at $i$ includes time to
    * determine relationship between elements: $Θ(1)$
    * run heapify on a subtree rooted at one of $i$'s children
* $2n/3$ is the worst case size of the subtree (half filled bottom level) and thus

    * $ T(n) <= T(2n/3) + Θ(1)$, ie. $T(n) = O(lg n)$
### Build Heap
Build a Heap from an Array A with $n$ elements into a heap

* Note that elements in $A[⌊n/2⌋+1...n]$ are 1-element heaps

```c
void BuildHeap(int A[], int n){
    for(int i = ⌊n/2⌋; i > 1; i--){
        Heapify(A, i, n)
    }
}
```

**Running Time**
* There are $O(n)$ calls to heapify and so $T(n) = O(n lg n)$
* Not an asymptotically tight bound - but good enough for an overall $O(n lg n)$ bound for heap sort
* Intuition for tight bound: time for heapify to run at a node i varies with the height of $i$
    * An n-element binary heap has height lg n
    * The heap has at most $⌈n/2h+1⌉$ nodes of height $h$
    * The cost for one call of heapify is $O(h)$

### Heap Sort
```c
void HeapSort(int A[], int n){
    int s = n;
    BuildHeap(A);   // O(n)
    for(int i = n; i > 1; i--){
        exchange(A[i], A[1]);
        s = s-1;
        Heapify(A, 1, s); // O(log n)
    }
}
```
**Running time**
Heapsort runs in time $O(n)+ n O(lgn)=O(nlgn)$
## Quicksort
#### Rough Idea
* Quicksort is a divide-and-conquer algorithm
    * Divide: partition array into two subarrays such that the items in the lower part <= the items in the upper part
    * Conquer: recursively sort the two subarrays
    * Combine: trivial since sorting is in place


```c
void QuickSort(int A[], int n, int l, int r){
    if (l<r){
        int m = LomutoPartition(A, n, l, r) || HoarePartition(A, n, l, r);
        QuickSort(A, n, l, m-1); // smallest Elements
        QuickSort(A, n, m+1, r)  // largest Elements

        // Important no Merge needed at the end
    }
}


int LomutoPartition(int A[], int n, int l, int r){
    int x = A[r]; // middle element (pivot) (we take rightmost element as middle element)
    int i = l-1;
    for(int j=l; j< r-1; j++){ // elements l..r-1 are inserted into either the smaller or larger part
        i = i+1; // smaller part grows by one
        exchange(A[i], A[j]);
    }
    exchange(A[i+1], A[r]); // putting pivot in right place
    return i+1;
}


int HoarePartition(int A[], int n, int l, int r){
    int x = A[r];
    int i = l-1;
    while (true){
        repeat j=j-1 until A[j] < x; // searches in the right part for a wrong (too small) element
        repeat i=i+1 until A[i] > x; // searches int he left part for a wrong (too large) element
        if (i < j){
            exchange(A[i], A[j]); // Swap of "wrong" elements
        } else {
            return i;
        }
    }

}
```


**Performance**
Worst Case
* Occurs when the array is already completely sorted
* Partitioning produces one subproblem with $n − 1$ items and one with 0 elements
* If such a partitioning arises at each recursive call then $T (n) = T (n − 1) + T (0) + Θ(n) = T (n − 1) + Θ(n)$
where $Θ(n)$ is the cost of partitioning the array
* Sum of the costs incurred at each level of the recursion yields an arithmetic series (i.e., $\sum_{i=0}^{n}i$)
* It thus follows that, in the worst case, $T(n) = Θ(n^{2})$

Best Case
* Partitioning produces two subproblems of size $n/2$
* If such a partitioning arises at each recursive call then
$T (n) = 2T (n/2) + Θ(n)$
* It thus follows that, in the best case, $T (n) = Θ(n lg n)$

Average case
* Actually much closer to best case than to worst case
* Quick sort’s behavior is determined by the ordering of the array elements
* In average, there is a mix of “good” and “bad” splits
* Underlying assumption: all permutations of the input numbers are equally likely
* Randomized algorithm: partition around random item (instead of last item)
    * Running time is independent of input ordering
    * No specific input triggers worst case behavior
    * Worst case determined only by output of the random-number generator
* Randomization is a general tool to improve algorithms with bad worst-case but good average-case complexity