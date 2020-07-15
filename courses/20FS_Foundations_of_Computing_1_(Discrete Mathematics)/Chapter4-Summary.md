# Summary: Chapter 4 - Number Theory & Methods of Proof
## Prime Def
$n$ is prime $\iff \forall$ pos interger $r$ and $s$, if $n$ = $r*s$
($r = 1 \wedge s = n) \vee (r = n \wedge s = 1)$

$n$ is composite $\iff \exist$ pos. interger $r$ and $s$ such that $n=r*s$ and $1 < r <n$ and $1 < s < n$
## Even Number
$n$ is even $\iff \exist$ int $k$ such that $n = 2k$
$n$ is odd $\iff \exist$ int $k$ such that $n = 2k + 1$
## Disproof by Counterexample
Find x in D where hypothesis is true and conclusion is false
## Rational
$r$ is rational $\iff \exist$ int $a$ and $b$ such that $r = \frac{a}{b} $
## Divisibility
$n$ is divisble by $d$, if and only if, $n * d$ (times n)
$d |n \iff \exist$ int $k$ such that $n = d*k$

(d divides n)
## Prime Divisiblity
????
## Unique Factorization of Int.
$n$ = $p_{1}^{e_{1}} * p_{2}^{e_{2}}$

* prime $p$
* $n > 1$
* some int $e_{x}$
## Quotient Remainder Theory
$n = d*q + r$
($0 <= r < d$)
* $n$ is int
* $d$ is positive int
## Div - Mod
n div d = int when n/d
n mod d = nonegativ remainder of n div d

$n$ div $d = q$
&& 
$n$ mod $d = r \iff n = d*q = r$

($d <= r < d$)
## Triangle Inequality
//TODO:
## Method of Contradiction
* Suppose statement is false -> Negation needs to be true
* Supposition leads to contradiction
* Statement to be proven is true
## Method of Proof by Contraposition
* Prove contrapositive by a direct proof
## Irrationality of √2
//TODO:
## Euclidean Algorithm
$A$ and $B$ find greatest common denominator

```c
while (b != 0){
    r = a mod b;
    a = b;
    b = r;
}
return a;
```