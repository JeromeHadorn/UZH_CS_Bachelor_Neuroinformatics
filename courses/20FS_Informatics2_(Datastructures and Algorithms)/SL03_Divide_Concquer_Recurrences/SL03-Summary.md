# Summary: SL03 Divide and Conquer, Recurrences
## Divide and conquer
* Recursive algorithms: divide-and-conquer approach
* Principle: if problem size is small enough to be solved trivially then solve it; else
    1. Divide problem into a number of subproblems
    2. Conquer subproblems by solving them recursively
    3. Combine solutions of the subproblem into solution for the original problem


* Requires some practice and is the key part
* Fundamental properties of a decomposition
    * It reduces the problem to smaller problems
    * Often, these smaller problems are the same as the original problem
    * A sequence of decompositions eventually yields the base case (trivial solution)
    * It must contribute to solving the original problem
### Merge Sort
Closely follows the divide-and-conquer paradigm
To sort an n-element sequence proceed as follows
* **Divide**: divide the sequence into two n/2-element sequences
* **Conquer**: sort the two sequences recursively using merge sort
* **Combine**: merge the two sorted sequences to produce the solution

Recursion stops when the sequence that must be sorted has length 1.


```c
void mergeSort(int A[], int l, int r){
    if (l < r){
        int m = floor((l+r)/2);
        mergeSort(A,l,m);
        mergeSort(A,m+1,r);
        merge(A,l,r,m);
    }
}

void merge(int A[], int l, int r, int m){
    int B[100];

    int bSize=0;
    for (int i=l; i <= m;i++){
        B[i] = A[i];
        bSize++;
    }
    for (int i=m+1; i<r; i++){
        //reverse filling
        B[r+m-i+1] = A[i];
        bSize++;
    }

    int nA = sizeof(B)/sizeof(B[0]);
    int i=l;
    int j=r;

    for (int k=l; k<r;k++){
        if (B[i] < B[j]){
            A[k] = B[i];
            i=i+1;
        } else {
            A[k] = B[j];
            j=j-1;
        }
    }
    
}
```
### Tromino Tiling
Provide a tromino tiling for a 2n × 2n board with a hole

**Trivial case: n = 1**
* Tromino tiling for a 2<sup>1</sup> × 2<sup>1</sup> board with a hole
* Solution is easy, place one of the 4 tile variantions
* Idea for 2<sup>n</sup> × 2</sup>n</sup> board: reduce size of the board
 
**General case: n > 1**
* Problem: get only one problem of size 2<sup>n−1</sup> × 2<sup>n−1</sup>
* But what about the other squares? There are no holes
* Solution: use a tromino to simulate missing holes
* One can repeat this until the 2<sup>1</sup> × 2<sup>1</sup> case is reached



**Sketch of algorithm**
* Input: board size n (2<sup>n</sup> × 2<sup>n</sup>), location l of the hole
* Output: tiling of 2<sup>n</sup> × 2<sup>n</sup> board with hole in location l
* Rough outline of tile (n, l)
    * If n = 1 then tile with one tromino
    * Otherwise, proceed as follows
        * Divide the board in to four equal-sized boards
        * Put a tromino to simulate the three missing holes
        * Call tile(n−1,l1), tile(n−1,l2), tile(n−1,l3),and tile(n − 1, l4) where l1, l2, l3, and l4 are the locations of the four holes
 

 ```c
void Tile(n,L){

    //Input: 2nx2n board, location L of hole

    //Output: tiling of the board

    if (n==1){
        //then tile with one tromino and return;
    } else {
        Divide board into four equal-sized boards;
        Place one tromino at center to cover 3 holes;
        Let L1, L2, L3, L4 be positions of the 4 holes; // coordinates (x/y)
    Tile(n-1,L1);
    Tile(n-1,L2);
    Tile(n-1,L3);
    Tile(n-1,L4);
    }
}
 ```
## Recurrences
Informal definition
* Running times of algorithms with recursive calls can be described using recurrences
* A recurrence is an equation or inequality that describes a function in terms of its value on smaller inputs
* Example: the running time of merge sort is described by the following recurrence

T(n)
        =  Θ(1)          |    if n=1
        = 2T(n/2) + Θ(n)  |  if n > 1


### Repeated (backward) Substitution
* Is not a strictly formal proof
* The procedure is straightforward
    * Substitute, expand, substitute, expand, etc.
    * Observe a pattern and determine the expression after the 􏰀 i-th substitution
    * Find out what the highest value of i should be to get the base case of the recurrence
    * Insert the cost of the base case and the expression for i into the observed expression

Observe pattern
```
  T (n)
= 2T (n/2) + 2n + 3                  // Substitute
= 2(2T (n/4) + n + 3) + 2n + 3       // Expand
= 4T (n/4) + 4n + 9                  // Substitute
= 4(2T(n/8) + n/2 + 3) + 4n + 9      // Expand
=8T(n/8)+3·2n+(4+2+1)3               // Find Pattern
```
= 2<sup>i</sup>T(n/2<sup>i</sup>) + 2in + 3 ∑ <sup>i−1</sup><sub>j=0</sub> 2j

* Upper bound for i is **lg n**
* Insert this for i and simplify
* -> **Θ(n lg n)**

### Substitution method
Basic methodology
* The substitution method for solving recurrences entails two steps
    1. Guess the form of the solution
    2. Use induction to prove the solution


```
Example: consider the recurrence T (n) = 4T (n/2) + n

Guessed solution: T(n) = n^3, i.e. T(n) is of the form n^3

Mathematical induction: need to show that T (n) ≤ cn^3

Need to show that T(n) ≤ cn3 for T(n) = 4T(n/2) + n

    T (n)   = 4T (n/2) + n          (recurrence)
            ≤ 4c(n/2)^3 + n         (inductive hyp.)   
            = cn^3/2 + n            (simplification)
            = cn^3 − (cn^3/2 − n)   (rearrangement)
            ≤ cn3                   (for c ≥ 2, n ≥ 1)


It follows that T (n) = O(n3)
```
### Recursion method
Basic methodology
* A recursion tree is a convenient way to visualize what happens when a recurrence is iterated
* Good for guessing asymptotic solutions to recurrences
* Example:consider T(n) = T(n/4) + T(n/2) + n^2


Tree will give you a guess which you will use to do a substitution.
### Master Method
To solve a class of recurrences that have the form
> T(n) = aT(n/b) + f(n)

Assumptions:
* a ≥ 1,
* b > 1,
* f(n) asymptotically positive
 
* T (n) describes running time of a divide-and-conquer algorithm
    * a subproblems of size n/b are solved recursively, each in timeT(n/b)
    * f(n) is the cost of dividing the problem and combining the solutions


```
T(n) = f(n) + aT(n/b)
= f(n) + af(n/b) + aT(n/b2)
= f (n) + af (n/b) + a2 f (n/b2 ) + . . .
+ alogb n−1f(n/blogb n−1) + alogb nT(1) = 􏰈logb n−1 aif(n/bi) + Θ(nlogb a)
i=0
```
* logb n levels
* a <sup>log b n</sup> = n <sup>log b a </sup>    (leaves)

Underlying intuitions
* Three possible cases
    * Running time dominated by the cost at the root (case 3)
    * Running time dominated by the cost at the leaves (case 1)
    * Running time evenly distributed throughout tree (case 2)
* Solve recurrence by identifying dominant term
* In each case compare f(n) with n <sup>log<sub>b</sub> a</sup>
 

**Case 1**: f(n) = O(nlogb a−ε) yields T(n) = Θ(nlogb a)
**Case 2**: f(n) = Θ(nlogb a) yields T(n) = Θ(nlogb a logb n)
**Case 3**: f(n) = Ω(nlogb a+ε) and af(n/b) ≤ cf(n) (c < 1, n > n0) yield T(n) = Θ(f(n))