# Summary: Chapter 2- Logic & Compound Statements
## Statement
Sentence that is either true or false but not both.
## Logically equivalent
If two statements have identical truth values for each possible substitution for their statement variables
    $ P \equiv Q$
## De Morgan Laws
$ \neg (p \wedge q) \equiv \neg p \vee \neg q$
$ \neg (p \vee q) \equiv \neg p \wedge \neg q$
## Tautology
No matter the variables is always true. **t**
## Contradiction
No matter the variables is alaways false. **c**
## Conditional Statement
If $p$ then $q$   
 $p$ (hypothesis) $\to q$ (conclusion)

It is false when $p$ is true and $q$ is false, otherwise it is true.

If conclusion is false then statement automatically True no matter the conclusion

$p \vee q \to r \equiv (p \to r) \wedge (q \to r)$
$p \to q \equiv \neg q \vee q$
## Contrapositve
if $p$ then $q$:  **if $\neg q$ then $\neg p$**
## Converse
if $q$ then $p$
## Inverse
If $\neg p$ then $\neg q$
## Biconditional
If both true then true else not true
$ p \iff q \equiv (p \to q) \wedge (q \to p)$
## Conditions
$r$ is a sufficient condition for $s$ - if $r$ then $s$
$r$ is a necessary conditoin for $s$ - if $\neg r$ then $\neg s$
## Circuits
//TODO:
## Argument Form
If $p$ then  $q$    (Premises)
$p$             (Premises)
∴ q (therefore Conclusion)

An **Argument** is a sequence of statements
An **Argument Form** is a sequence of statement Forms.
If all premises are true, then the conclusion is true.
## Modus Ponens
If $p$ then $q$
$p$
∴ $q$ 
## Modus Tollens
If $p$ then $q$
$\neg q$
∴ $\neg p$ 
## Generalization
$p$
∴ $p \vee q$ 
## Specialization
$p \wedge q$
∴ $p$ 
## Conjunction
$p$
$q$
∴ $p \wedge q$ 
## Elimination
$p \vee q$
$\neg q$
∴ $p$ 
## Division into Cases
$p \vee q$
$q \to r$
$p \to r$
∴ $r$ 
## Transivity
$p \to q$
$q \to r$
∴ $p \to r$ 
## Contradiction Rule
$\neg p \to c$
∴ $p$ 