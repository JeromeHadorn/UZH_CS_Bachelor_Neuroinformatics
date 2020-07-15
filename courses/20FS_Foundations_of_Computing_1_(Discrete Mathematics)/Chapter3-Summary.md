# Summary: Chapter 3 - Logic & Quantified Statements
## Predicate
If $P(x)$ is a predicate and $x$ has a domain D, the **truth set** of all elements of D that make P(x) true when they are substituted for x. The truth set of P(x) is denoted.

$\{ x \in D | P(x)\}$
> The set of all x in D such that P(x) is true
## Quantifiers
* $\forall x \in D$, $x$ ist mortal
* $\exists$ a person $p, p$ is funny
## Implicit Quantification
Let $P(x)$ and $Q(x)$ be predicated and suppose the common domain of $x$ is $D$.
* $P(x) => Q(x)$, every element in truth set $P(x)$ in $Q(x)$
    * $\forall x, P(x) \to Q(x)$
* $P(x) \iff Q(x)$, have identical truth sets
    * $\forall x, P(x) \iff Q(x)$
## Negation of a universal Statement
$ \forall x$ in $D$, $Q(x)$
$\exist x $ in D such that $\neg Q(x)$


($\neg (\forall x \in D$ such that $Q(x)) \equiv \exist x \in D, \neg Q(x))$
## Negation of an existential Statement
$\exist x $ in D such that $Q(x)$
$ \forall x$ in $D$, $\neg Q(x)$

($\neg (\exist x \in D$ such that $Q(x)) \equiv \forall x \in D, \neg Q(x))$
## Vacuously True (true by default)
Only if, $P(x)$ is false for every $x$ in $D$
## Variants of Universal Cond. Statements
$\forall x \in D,$ if $P(x)$ then $Q(x)$
1. Contrapositive: $\forall x \in D,$ if $\neg Q(x)$ then $\neg P(x)$
2. Converse $\forall x \in D,$ if $Q(x)$ then $P(x)$
3. Inverse $\forall x \in D,$ if $\neg P(x)$ then $\neg Q(x)$
## Two different Quantifiers
$\forall x$ in D, $\exist y$ in E such that $P(x, y)$
* Pick whatever x in D, y in E that works for that particular x.

$\exist x $ in D, $\forall y$ in $E, P(x, y)$
* Find one particular x in D, that will work for no matter what y in E is chosen.
## Negations of Muli-Quant Statements
$\neg (\forall x$ in D, $\exist y$ in E such that $P(x, y)) \equiv \exist x $ in D, $\forall y$ in $E, \neg P(x, y)$

$\neg(\exist x $ in D, $\forall y$ in $E, P(x, y)) \equiv \forall x$ in D, $\exist y$ in E such that $\neg P(x, y)$
## Formal Logical Notation
$\forall x$ in $D, P(x) \equiv \forall(x$ in $D \to P(x))$
$\exist y$ in $D$, such that $P(x) \equiv \exist x (x$ in $D \wedge P(X))$