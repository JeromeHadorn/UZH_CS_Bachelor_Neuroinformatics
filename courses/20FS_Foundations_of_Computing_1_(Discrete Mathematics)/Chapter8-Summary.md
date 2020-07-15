# Summary: Chapter 8 Relations


## Relations
Relations are more general than functions. The key difference is that the same element in the Domain may be related to multiple elements in the Co-domain

## Inverse of a Relation
$𝐑^{-1} = \{ (y,x) \in B\times A | (x,y) \in R \}.$

For all $x \in A$ and $y \in B$,   $(y,x) \in R_{-1}\iff  (x,y) \in R$.

## Reflexivity, Symmetry, and Transitivity
Let R be a relation on a set A.
1. R is **reflexive** if, and only if, for all $x \in A, x R x$.
2. R is **symmetric** if, and only if, for all $x,y \in A,$ if $xRy$ then $yRx$.
3. R is **transitive** if, and only if, for all $x,y,z \in A$, if $xRy$ amd $yRz$ then $xRz$.


## Disproove Reflexivity, Symmetry, and Transitivity
To prove that a relation does not have one the properties, find a counterexample or negate the general statement:
1. R is not **reflexive** ⇔ there is a least an element x in A such that x not R x.
2. R is not **symmetric** ⇔ there are elements x and y in A such that x R y but y not R x.
3. R is not **transitive** ⇔ there are elements x, y and z in A such that x R y and y R z but x not R z.

# The Transitive Closure of a Relation
A relation R may fail to be transitive if it does not contain certain ordered pairs.

To make it transitive, we need to add ordered pairs.

The relation $R^{t}$ obtained by adding the least number of ordered pairs to ensure transitivity is called the transitive closure of the relation.

## Equivalence Relation
Let A be a set and R a relation on A, R is an equivcalence relation if, and only if, R is reflexive, symmetric and transitive


## The Relation Induced by a Partition
A partition of a set A is a collection of mutually disjoint subsets A𝑖 whose union is A.


We can observe that a** relation induced by a partition** is always **reflexive**, **symmetric**, and **transitive**. Thus, a relation induced by a partition is always an equivalence relation!

## Equivalence Classes of an Equivalence Relation
Given an equivalence relation on a certain set A and any particular element a in A, the subset [a] of all elements related to a under R is called the equivalence class of a:

[a] = { x ∈ A | x R a } .

Distinct equivalence classes of an Equivalence Relation form a partition A.

Suppose that a, b ∈ A, if a R b, then [a] = [b]. This is trivial since, all the elements in [a] are also in [b] and vice versa.

Any element of an equivalent class is called “Class Representative”.

## Congruence Modulo n
Let m and n be integers and let d be a postiive integer. We say that m is congruent to n modulo d and write

$m \equiv n$ (mod d)

if an only if, $d | (m-n)$

## Inverse Modulo

For all integers a and n, if gcd(a, n) = 1, then there exists an integer s such that
a*s ≡ 1 (mod n). The integer s is called the inverse of a modulo n.
## RSA
* In RSA, the plaintext M is converted into ciphertext C according to the following formula:

    $C = M^{e}$ $mod$ $pq$

 $pq$ and $e$ are the public keys and anyone can use them to encrypt their messages!
* The plaintext M for a ciphertext C is then recovered as follows:

    $M = C^{d}$ $mod$ $pq$.
Where d is the private key; it is secret and only the recipient knows it.

## When does the RSA Cipher work?
For the RSA to work, the following expression must all for all positive integers M < pq:
$M = (M^{e})^{d}$ $mod$ $pq$

This holds if:
* $p$ and $q$ are prime
* $e$ and the product $(p − 1)(q − 1)$ are relatively prime (e.g., their greatest common divisor is 1)
* $ed \equiv 1$ (𝑚𝑜𝑑(𝑝−1)(𝑞−1)).
    * (i.e.,𝒅 is the inverse of e modulo (𝑝 − 1)(𝑞 − 1)).