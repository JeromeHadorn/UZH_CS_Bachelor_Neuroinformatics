# Summary SL08 Dynamic Programming
Design of algorithms
* Design techniques used so far
    * Iterative (brute-force) algorithms
        * Linearsearch,selectionsort,insertionsort,etc
    * Data structure based algorithms
        * Heapsort,PQsort,BSTsort,RBTsort,etc
    * Divide-and-conquer algorithms
        * Binarysearch,mergesort,quicksort,etc
* But there exist other techniques
    * Dynamic programming (remember solutions)
        * Matrixmultiplication,longestcommonsubsequence
    * Greedy algorithms (choose local optimum in each step)
        * Graphbased:minimumspanningtree,shortestpath

**Dynamic programming** - Solve problem by combining solutions of subproblems

## Fibbonaci
Bottom-up approach
* I Keep remembering solutions of solved subproblems
```c
//Algo: Fib2(n)
f[1] = 0;
f[2] = 1;
for i = 3 to n+1 do
    f[i] = f[i-2] + f[i-1]
return f(n+1);
```
* Can compute value of fib(n) in linear time (i.e., O(n))
* Algorithm computes the solution in bottom-up fashion.
* The bottom-up approach trades space for time.


Can do without remembering all the previous results
```c
//Algo: Fib3(n)
s = 0;
t = 1;
for i = 1 to n do
    r = t;
    t = t+s;
    s=r
return t;
```
* Thus, space complexity is constant rather than linear

## MATRIX-CHAIN MULTIPLICATION
Problem definition
* It matters how the product $A1 · · · An$ is parenthesized


**Optimal substructure**
* Let M(i,j) (i <= j) be the minimum number of scalar multiplications necessary to compute Ai...j = Ai · · · Aj
*  Key observations
    * Outer most parenthesis partitions the chain of matrices (i,j) at some k (i <= k < j): (Ai ···Ak)(Ak+1 ···Aj)
    * Optimal parenthesization of matrices (i, j) has optimal parenthesization on either side of k, i.e. for matrices (i, k) and (k + 1, j)
* Example(i=1,j=n,k=3):

**Recursive problem formulation**
One can try out all possible k and take the one with the smallest cost:

M(i,j) = min i<=k<j {M(i,k) + M(k + 1,j) + di-1 dk dj}

* The base case is M(i,i) = 0
* A direct recursive implementation is exponential (there is a lot of duplicated work)
```c
//Algo: MatrixRec(i,j)
if i==j then return 0;
min = MatrixRec(i,i) + MatrixRec(i+1,j) + di-1 di dj;

for k = i+1 to j-1 do
    q = MatrixRec(i,k) + MatrixRec(k+1,j) + di-1 dk dj;
    if q<min then min = q;
return min;
```




**DP solution**
* Idea for dynamic programming solution: store the optimal cost M(i,j) for each subproblem in a two-dimensional array M[1...n,1...n]
* Trivially,M(i,i)=0 for 1<=i<=n
* To compute M(i,j) one needs only values of M for I subproblems of length less than l = j ≠ i
* So, one has to solve subproblems according to their length: first subproblems of length 1, then the ones of length 2, and so on


```c
//Algo: MatrixDP(d)
for l = 1 to n do M[i,i] = 0;
for l = 1 to n-1 do // length
    for i = 1 to n-l do // i
        j = i+l;
        M[i,j] = Œ;
        for k = i to j-1 do
            q = M[i,k] + M[k+1,j] + di≠1dkdj;
            if q<M[i,j] 
            then M[i,j] = q; // cost
            c[i,j] = k; // place of parathesies
return (M,c);

```
**Analysis of the DP algorithm**
* After the execution of the algorithm it holds that
    * M[1,n]contains the value of the optimal solution
    * c stores the optimal subdivisions (choices of k)
* It is easy to see that the running time is O(n3)
    * Note that the algorithm has three nested loops
    * Reduction from exponential to polynomial time
 

**Memoization**
* Memoization is a technique for DP problems that preserves the recursive structure but does not do redundant computation.
* During the recursive calls newly computed solutions are stored in the DP data structure.
* The recursive procedure first checks if the solution has already been computed. If so it return the stored result.
* An advantage is that the exact computation sequence must not be programmed explicitly.


```c
//Algo: MatrixMemo(d,i,j)
if i==j then return 0;
if M[i,j]< infinity then return M[i,j];
for k = i to j-1 do
    q = di≠1dkdj + MatrixMemo(d0,...,dn,i,k) + MatrixMemo(d0 ,...,dn ,k+1,j);

    if q<M[i,j] then M[i,j] = q;
return M;
```


## Hanoi Memo
```c
if m[n] > 0 return m[n]
if (n==1) then return 1
m[n] = HanoiMemo(n-1, A, C, B) + 1 + HanoiMemo(n-1, C, B, A)
return m[m]

//Time linear (compute n elements in an array)
```


## Dynamic Programming
* We typically apply dynamic programming to optimization problems.
* The goal is to find a solution with the optimal (minimum or maximum) value.
* Dynamic programming is used frequently in bioinformatics (sequence alignment) and economics (macroeconomic models).
* Dynamic programming solves problems by combining the solutions to subproblems.
* Dynamic programming applies when subproblems overlap.
* A dynamic-programming algorithm solves each subproblem just once.


**Step 1:** Show optimal substructure – an optimal solution to a problem contains optimal solutions to subproblems
* Solution to a problem
    * Makingachoiceoutofanumberofpossibilities(lookwhat I possiblechoicestherecanbe)
    * Solving one or more subproblems that are the result of such a choice (characterize the space of subproblems)
* Show that solutions to subproblems must themselves be optimal for the whole solution to be optimal

**Step 2**: Give a recursive problem formulation for getting the optimal value
* Mopt = mink{(combination of Mopt of all subproblems resulting from the choice k) + (cost associated with making the choice k)}
 
**Step 3:** Compute the value of an optimal solution in a bottom-up fashion (or use memoization)
* Show that the number of different instances of subproblems is bounded by a polynomial
* Check whether it is possible to reduce the space requirements (forget no longer needed solutions)
 

**Step 4**: If required construct an optimal solution from the computed information (sequence of choices made)

## LONGEST COMMON SUBSEQUENCE
```c
//Algo LCSrec(i,j)
if (i==0 || j== 0)then return 0
else if (x[i] == y[i]) then return LCSrec(i-1, j-1) + 1
else return max(LCSrec(i-1,  j) LCS(i, j-1))
```

```c
//Algo LCSmemo(i,j)
if (i==0 || j==0) then return 0
else if (c[i][j] != -1) then return c[i][j]
else if(x[i] == y[i]) then
    c[i][j] = LCSmemo(i-1, j-1) +1;
    return c[i][j];
else
    c[i][j] = max(LCSmemo(i-1,j), LCSmemo(i, j-1))
    return c[i][j]
```


DP algorithm:
```c
//Algo: LCSdyn(Xn,Ym)
for i = 1 to n do c[i,0] = 0;
for j = 0 to m do c[0,j] = 0;
for i = 1 to n do
    for j = 1 to m do
        if xi == yj then
            c[i,j] = c[i-1,j-1] + 1
        else
            if c[i-1,j]Øc[i,j-1] then
                c[i,j] = c[i-1,j]
            else
                c[i,j] = c[i,j-1]
return c;
```

Print Longest Common Subs.
```c
printLCS(i,j)
if (i==0 || j ==0) then return
if (c[i,j] > c[i-1,j] && c[i,j] > c[i,j-1]) then
    printLCS(i-1, j-1)
    pritntf("%c", x[i])
else if (c[i,j] == c[i-1, j]) then
    printLCS(i-1,j)
else
    printLCS(i, j-1)
```

## Coin Changes
* Assume you have coins of different denominations, e.g., 5,
15, 20, 50.
* Assume that of each denomination you have an unlimited
number of coins.
* Given an amount A and m denominations the goal is to
change A with as few coins as possible.
* Example:
    * Denominations: 1, 2, 5, 10
    * A = 27, change = 2*10 + 1*5 + 1*2


Given are coins of different denominations (e.g., 1, 5, 15, 20, 50,
etc). The goal is to pay out amount A with the smallest possible
numbers of coins. Develop a solution.

Three cases:
1. No solution: e.g., A=3 and the only available coin is 2.
2. Greedy solution (i.e., in each step use the highest possible
coin) gives the optimal solution. Typically, denominations
are designed in such a way.
3. DP solution if the optimal solution cannot be found by
choosing the largest possible coin in each step (e.g., A=12,
coins = (10, 6, 1))

```c
Coin(A)
    if (A==0) then return 0;
    if (A < 0) then return -1;
    
    min = -1;
    
    for k=0 to m-1 do
        nr = Coin(A-d[k]);
        if(nr != -1 && (min == -1 /*No solution so far*/ || 1 + nr < min /*better solution*/)) {
            min = 1 + nr
        }
    return min
```

Memoization
```c
Initialization
for i=0 to A do
    c[i] = -1

Coin(A)
    if (A==0) then return 0;
    if (A < 0) then return -1;
    if (c[A] != -1) return c[A];
    
    for k=0 to m-1 do
        nr = Coin(A-d[k]);
        if (nr != -1 && (c[A]!= -1 || 1 + nr < c[A])) {
            c[A] = 1 + nr
        }
    return c[A]
```

Dynamic Programming
```c
CoinDynamic(int A){
    c[0] = 0
    for i=1 to A do
        c[i] = -1;
        
        for k=0 to m-1 do
            if(d[k] <= i /*coin is small enough*/&& c[i-d[k]] != -1 /*smaller amount can be changed (there exists a solution*/&& (c[i] != -1 /*No Solution yet*/ || 1+ c[i-d[k]] < c[i] /*better solution*/)){
                c[i] = 1 + c[i-d[k]];
            }
}
```