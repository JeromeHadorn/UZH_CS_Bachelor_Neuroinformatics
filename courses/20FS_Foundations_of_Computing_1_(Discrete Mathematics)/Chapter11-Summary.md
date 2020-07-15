# Summary: Chapter 11 Analysis of Algorithm Efficiency
## O-, Ω-, and Θ-Notations
The O-, Ω-, and Θ-notations provide approximations that make it easy to evaluate large-scale differences in algorithm efficiency.

* They provide differences in asymptotic performance, i.e., ignoring differences of a constant factor and differences that occur only for small sets of input data (e.g., data initialization).

### O Notation
Suppose $𝑓(𝑥)$ and $𝑔(𝑥)$ are real-valued functions of a real variable $𝑥$. If, for sufficiently large values of $𝑥$:

1. the values of $|𝑓|$ are less than those of a multiple of $|𝑔|$, then $𝒇$ is of order at most $g$, or $𝑓(𝑥)$ is $𝑂(𝑔(𝑥))$. (Read O: big-O)
### Ω Notation
Suppose $𝑓(𝑥)$ and $𝑔(𝑥)$ are real-valued functions of a real variable $𝑥$. If, for sufficiently large values of $𝑥$:
1. the values of $|𝑓|$ are greater than those of a multiple of $|𝑔|$, then $𝒇$ is of order at least $𝒈$, or $𝑓(𝑥)$ is $Ω(𝑔(𝑥))$. (Read $Ω$: Omega)
### Θ Notation
Suppose $𝑓(𝑥)$ and $𝑔(𝑥)$ are real-valued functions of a real variable $𝑥$. If, for sufficiently large values of $𝑥$:
1. the values of $|𝑓|$ are bounded both above and below by those of multiples of $|𝑔|$, then $𝒇$ is of order $𝒈$, or $𝑓(𝑥)$ is $Θ(𝑔(𝑥))$. (Read $Θ$: Theta).

The $Θ$ notation is the most used in computer science. If $𝒇$ is of order $𝒈$ it means that they behave the same asymptotically, up to a multiplicative factor.

### O-, Ω-, and Θ-Notations in terms of Limits
Alternative and more practical definitions of O-, Ω-, Θ-Notations are:
 1. $𝑓(𝑥)$ is $𝑂(𝑔(𝑥))$ if $lim_{x \to \infin} |\frac{f(x)}{g(x)}|$ < ∞ (i.e., 0 or a non-zero constant)
 2. $𝑓(𝑥)$ is $Ω(𝑔(𝑥))$ if $lim_{x \to \infin} |\frac{f(x)}{g(x)}|$ > 0 (i.e., a non-0 constant or ∞)
 3. $𝑓(𝑥)$ is $Θ(𝑔(𝑥))$ if $lim_{x \to \infin} |\frac{f(x)}{g(x)}|$ non zero constant
## Algorithm Efficiency – Recap Table
These are the algorithms seen thus far and their complexities:
* Sequential Search: $𝑛$
* Binary Search: $log2 𝑛$
* Insertion Sort: $𝑛2$
* Merge Sort: $𝑛  *log2 𝑛$
* Bag-of-Words feature look-up: $log_{𝑏}𝑛$
* Tower of Hanoi: $2^{n}$
## Tractable and Intractable Problems
Problems whose solutions can be found with algorithms whose worst- case order with respect to time is a polynomial, or $O(n^{c})$, are said to belong to class P.
* Polynomial-time algorithms and are said to be tractable.
* Problems that cannot be solved in polynomial time are called intractable.

For some problems, it is possible to check the correctness of a solution with a polynomial-time algorithm, but it may not be possible to find a solution in polynomial time.
* Such problems are said to belong to class NP.

The biggest open question in theoretical computer science is whether every problem in class NP belongs to class P.
* Known as the P vs. NP problem.