# Summary: Chapter 5 - Sequences, Mathematical Induction, and Recursion
## Sequence
A **sequence** is a function whose domain is either all the intergers between two given intergers or all the integers greater than or equal to a given integer

Sequence is typically represented as a set of elements written in a row

$a_{m}, a_{m+1}, a_{m+2},..., a_{n}$

each individual element $a_{k}$ is called a term. The $k$ is called subscript or index.

## Summation Notation
If $m$ and $n$ are integers and $m <= n$, the symbol $\sum_{k=m}^{n} a_{k}$ is the sum of all the terms $a_{m}, a_{m+1}, a_{m+2}, ..., a_{n}.$

## Product Notation
If $m$ and $n$ are integers and $m ≤ n$, the symbol $\prod_{k=m}^{n} a_{k} = a_{m} * a_{m+1}* a_{m+2} ... * a_{n}.$ is the product of all the terms $a_{m}, a_{m+1}, a_{m+2}, ..., a_{n}.$

## Factorial
For each positive integer $n$, the quantity $n$ factorial denoted $n!$, is defined to be the
product of all the integers from $1$ to $n$:

$n! = n·(n − 1)···3·2·1.$

**Zero factorial**, denoted $0!$, is defined to be $1$:
$0! = 1.$

Let $n$ and $r$ be integers with $0 ≤ r ≤ n$. The symbol
$\binom{n}{r}$

is read **“n choose r”** and represents the number of subsets of size $r$ that can be chosen from a set with $n$ elements.

For all integers $n$ and $r$ with $ 0<= r <=n$,

$\binom{n}{r} = \frac{n!}{r!(n-r)}$

## Mathematical Induction
Induction is based on the domino effect. By making the first domino fall and making sure every other domino is going to hit at least one other, the whole sequence gets knocked down.

In this metaphor, making sure each domino hits at least one other corresponds to proving if $n$ is true, $n ± 1$ is also true. Making the first domino fall is equivalent to proving your formula for a specific case at one end of your range (e.g. 0).

Induction works best for problems formulated on $N$, or generally for problems for- mulated on sets where each element has a well-defined successor. Since there is no well-defined successor for each number in R (or any set X ⊇ R, e.g. C), induction is not applicable here.

i. Formulating the induction Hypothesis.
ii. Showing the base case (e.g. $n = 0$).
iii. Performing the induction step ($n \to n + 1$). 
iv. Distilling your findings into a final conclusion.

### Sum of a Geometric Sequence
$\sum_{i=0}^{0}r^{i} = \frac{r^{n+1}-1}{r-1}$

### Trominos
The main insight leading to a proof of this theorem is the observation that because $2^{k+1}$ =$2·2^{k}$, when a $2^{k+1}×2^{k+1}$ board is split in half both vertically and hori- zontally, each half side will have length 2k and so each resulting quadrant will be a $2k × 2k$ checkerboard.
  
A $2^{1} × 2^{1}$ checkerboard just consists of four squares. If one square is removed, the
remaining squares form an L, which can be covered by a single L-shaped tromino, as illustrated in the figure to the left. Hence $P(1)$ is true.

Consider a $2^{k + 1} × 2^{k + 1}$ checkerboard with one square removed. Divide it into four equal quadrants: Each will consist of a $2^{k} × 2^{k}$ checkerboard. In one of the quad- rants, one square will have been removed, and so, by inductive hypothesis, all the remaining squares in this quadrant can be completely covered by L-shaped tromi- noes. The other three quadrants meet at the center of the checkerboard, and the center of the checkerboard serves as a corner of a square from each of those quad- rants. An L-shaped tromino can, therefore, be placed on those three central squares. This situation is illustrated in the figure to the left. By inductive hypothesis, the remaining squares in each of the three quadrants can be completely covered by L- shaped trominoes. Thus every square in the $2k + 1 × 2k + 1$ checkerboard except the one that was removed can be completely covered by L-shaped trominoes.

## Strong Mathematical Induction
Let $P(n)$ be a property that is defined for integers $n$, and let $a$ and $b$ be fixed integers with $a ≤ b$. Suppose the following two statements are true:
1. $P(a),P(a+1),...,$ and $P(b)$ are all true. (basis step)
2. For any integer $k ≥ b$, if $P(i)$ is true for all integers $i$ from a through $k$, then
$P(k + 1)$ is true. **(inductive step)**
Then the statement

for all integers $n ≥ a, P(n)$

is true. (The supposition that $P(i)$ is true for all integers $i$ from a through $k$ is called the inductive hypothesis. Another way to state the inductive hypothesis is to say that $P(a),P(a+1),...,P(k)$ are all true.)
 


## Assertions
Consider an algorithm that is designed to produce a certain final state from a certain initial state. Both the initial and final states can be expressed as predicates involving the input and output variables. Often the predicate describing the initial state is called the **pre-condition for the algorithm**, and the predicate describing the final state is called the **post-condition for the algorithm**.

## Recurrence
A recurrence relation for a sequence $a0,a1,a2,...$ is $a_{k}$ formula that relates each term ak to certain of its predecessors $a_{k}, a_{k}, . . . , a_{k}$ , where i is an integer with k − i ≥ 0. The initial conditions for such a recurrence relation specify the values of $a_{0},a_{1},a_{2},...,a_{i-1}$, if i is a fixed integer, or $a_{0},a_{1},a_{2},...,a_{,}$, where m is an integer with m ≥0, if i depends on k.

## Understand the Tower of Hanoi
## Arithmetic Sequence
A Sequence is only called an arithmetic sequence if and if only there is a constant $d$ such that

$a_{k} = a_{k-1} + d$

## Geometric Series
A Sequence is only called an geometric sequence if and if only there is a constant $r$ such that

$a_{k} = a_{k-1} * r$

## Second Order linear homogenous recurrence relation with constant coefficients
A **second-order linear homogeneous recurrence relation with constant coefficients** is a recurrence relation of the form

$a_{k} = Aa_{k−1} + Ba_{k−2}$ for all integers $k ≥$ some fixed integer

where A and B are fixed real numbers with B ̸= 0.


“Second-order” refers to the fact that the expression for ak contains the two previous terms ak−1 and ak−2, “linear” to the fact that ak−1 and ak−2 appear in separate terms and to the first power, “homogeneous” to the fact that the total degree of each term is the same (thus there is no constant term), and “constant coefficients” to the fact that A and B are fixed real numbers that do not depend on k.


