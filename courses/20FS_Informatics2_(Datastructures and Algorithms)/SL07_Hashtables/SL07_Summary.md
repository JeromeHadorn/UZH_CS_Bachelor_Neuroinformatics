# Summary SL07 Hashtables
* Dictionaries store elements so that they can be located quickly using keys.
* If order (methods such as min, max, successor, predecessor) is not required it is enough to check for equality.

* Operations that require ordering are still possible (e.g., scanning the entire database) but cannot use the dictionary access structure.
    * Usually all elements must be compared, which is slow.
    * Can be OK if it is rare enough.


### Stats
* BST: insert, search, and delete in $O(h)$ time
* RBT: insert, search, and delete in $O(lg n)$ time
* Hashing: insert, search, and delete in $O(1)$ time
    * Other dictionary operations (min, succ, ...) are not supported
    * Hash table is expensive and difficult to grow and shrink.
    * Application: symbol table for identifiers in a compiler, customer IDs, ...

**Hash tables vs arrays**
* Hash tables are a generalization of arrays
* Big advantage of arrays consists in direct addressing
    * Ability to access arbitrary array position in $O(1)$ time


Different data structures to realize dictionaries
* arrays
* linked lists
* Hash tables
* BST
* RBT


## Hashtable
* We use a hash table of size m to avoid wasting space.
* A hash table is like an array, but with a function to map the large range into one that we can manage efficiently.
* For instance take the original key, **modulo the size** of the relatively small hash table, and use that as an index.
* Example: insert (9635-8904, Jens) into a hash table with five slots (m = 5):
    * 96358904 mod 5 = 4

## Using a Hashfunction
* Put a record with key $k$ in slot $h(k)$ instead of slot k
* Thus, a hash function h is used to compute the slot
* Maps universe $U$ into the slots of hash table $HT [1 . . . m]$
$h: U æ {1,2,...,m}$
item with key $k$ hashes to $h(k)$, $h(k)$ is hash value of $k$
* Hash function reduces range of array indices that need to be handled, i.e., m values instead of |U | values
* There is a hitch: two keys may hash to the same slot
* Need a technique to resolve such collision conflicts
    * Various options: chaining, probing, double hashing


## Collision resolution with chaining
* Chaining: put items that hash to same slot in linked list
* Each slot contains either NIL or a pointer to head of a list
* Search, insert, and delete: relatively easy to implement

```c
struct node {
    char name[20];
    struct node* next;
}

struct node HashTable[70000];
```
* Bad how to handle empty slots?
```c
struct node {
    char name[20];
    struct node* next;
}
struct node* HashTable[70000];
```
* Good no ambiguiuty
* Empty slots are clear

## Analysis of hashing
* Given a hash table $HT$ with m slots that stores $n$ items, define the load factor – of $HT$ as $n/m$
    * $a$ corresponds to average number of items in a list
* Assumption 1: any given item is equally likely to hash into any of the $m$ slots of the hash table
    * This assumption is called uniform simple hashing
* Assumption 2: h(k) can be computed in constant time (independent of # elements)
* Search (unsuccessful/successful) takes O(1 + –) time
    * best case, $n=1, m=1M \to a = 1/1M ≈ 0, O(1)$
    * best case, $n=1M, m=1 \to a = 1M/1 ≈ n, O(n)$ (cost of linear search)

* Make your hashtable large enough!

## BTR Advantages
* only when very large

## Hash Functions
Design of hash functions
* Hash function h must be computed in constant time
* Must satisfy the assumption of simple uniform hashing
    * Each key is equally likely to hash to any of the m slots
    
Hashing non-integer keys
* Consider set N of natural numbers as universe of keys
* If the keys are not natural number then a way is found to interpret them as such

## Division Method
* Hash function takes the remainder of k divided by m
    * $h(k)=(kmodm)+1$
    * $m=12,k=100 \to h(k)=5$
* Generally, one tries to avoid certain choices for m
    * For $m=2^{p},h(k)$ gives the $p$ least significant bits of $k$ and all keys with the same ending go to the same slot
* Good choice for $m$: prime number not close to $2^{p}$
  * Hash table $HT$ for roughly $n = 2000$ character strings
  * One may choose $m = 701$ because it is a prime near $2000/3$
        * (≈ 3 items per list) but not near any power of 2


## Multiplication Method
* Multiply key k by A and extract fractional part of $kA$
    * $h(k)=[m(kAmod1)]+1$
    * A constant such that $0 < A < k$ 
    * $kA mod 1$: fractional part of $kA$, i.e. $kA - [kA]$
* Advantage: value of m is not critical, typically use 2p
* Optimal choice for A depends on data characteristics
  * Knuth suggests that A ≈ $\frac{\sqrt{5}-1}{2}$ ≈ 0.618 works well
* Example: assume that A = 0.618 and m = 12
* $k=102:h(k)=[12·0.036]+1=[0.432]+1=1$
* $k=103:h(k)=[12·0.654]+1=[7.848]+1=8$
* $k=104:h(k)=[12·0.272]+1=[3.264]+1=4$

## Collision Resolution
### Chaining
* The simplest approach is chaining.
* Chaining maintains a table of links, indexed by the keys, to lists of items with the same key.
* **Pros**: easy, flexible, hash table never gets full
* **Cons**: stores elements outside hash table, additional space
### Open Addressing
* The idea is to store all items in the hash table itself
    * Each table entry contains either an item or is empty
    * No lists and no items are stored outside the table
* A drawback is that the table can fill up: load factor $a$ never exceeds 1
* Advantage of open addressing: avoid pointers
    * No need to follow pointers when accessing items
    * Simply compute sequence of slots to be examined
    * Larger number of slots for same amount of memory

Open addressing uses an extended hash function that includes the probe number:
    $h : U x \{1, 2, . . . , m\} \to \{1, 2, . . . , m\}$
    $\forall k: <h(k,1),...,h(k,m)>$ is permutation of $<1,...,m>$

* All dictionary operations systematically probe table slots
* Sequence of positions probed depends on given key

## Linear Probing
* Uses a hash function of the form
    * $h(k,i) = (h'(k)+ci)$ mod m
    * where $h'$ is a hash function
* We try out (probe) a number of positions:
    * NextLoc = (PreviousLoc + StepSize) mod m
* The step size should be chosen such that all locations are probed.
* Often a step size of one (c=1) is chosen. This guarantees that all locations are probed. (but data not distributed well)


**Steps**:
* If the current location is used, try the next table location:
* Lookups walk along the table until the key or an empty slot is found
* Uses less memory than chaining: one does not have to store the links
* Slower than chaining: one might have to probe the table for a long time

```c
//Algo: LinearProbingInsert(k)
if table is full then return error;
probe = h(k);
while HT[probe] is used do
    probe = (probe+1) mod m
table[probe] = k;
```

## Double Hashing
Two hash functions:
1. $h1$ determines the initial location
2. $h2$ determines the step size
3. $h(k,i) = (h1(k)+i* h2(k)$mod m
* Initial probe is to position $HT[h1(k)]$, successive probe positions are offset by $h2(k)$.


```c
//Search:
//Algo: DoubleHashingInsert(HT,k)
i = 0;
repeat
    probe = (h1(k) + i*h2(k)) mod m;
    i = i+1;
until (HT[probe] is free ‚ i>m);
if i>m then Error: hash table overflow;
else HT[probe] = k;
```

* h2(k) must be relatively prime to hash table size m 
    * m a power of 2, h2 always produces an odd number
    * m prime, h2 always produces a positive integer < m
* Example: m prime and h2(k) positive integer < m
    * Leth1(k)=(kmodm)+1, h2(k)=(k mod m')+1
    * Choose m' to be slightly less than m (say m' = m-1)
    * Given k=123456,m=701,m' =700: h1(k)=81, h2(k) = 257 (first probe to 81, then every 257th slot)
* Cost of searching in open-address hash table with $a = n/m < 1$
    * unsuccessful:1/(1-a)
    * successful: ln(1/(1 - a))/a
 

**Dictionary operations**
* Inserting and searching are relatively straightforward
    * At least if one assumes that there are no deletions
* Deletion is difficult: cannot mark deleted slot as empty
    * Solution: use special value to mark a deleted slot
    * This affects all hash table functions (e.g., the simple
procedures for insertion must be extended)


## Hashing with Open Addressing
```c
struct elem {
    int key;
    int status;
    /* 0: OCCupied, -1: EMPty, -2: DELeted */
};
struct elem HT [7000];
```

```c
//Algo: HTinit(HT)
for i = 0 to m-1 do HT[i].status = EMP;
```


```c
//Algo: HTinsert(HT,k)
i = -1;
repeat
    i++; probe = h(k,i);

until i>=m || HT[probe].status != OCC;

if i>=m then return -1;

HT[probe].status = 0;
HT[probe].key = k;
return probe
```

```c
//Algo: HTsearch(HT,k)
i = -1;
repeat
    i++; probe = h(k,i);
until i >= m /*searched unsuccseful*/|| /*Elem found*/ (HT[probe].status==OCC && HT[probe].key==k) || HT[probe].status==EMP (/*end of chain*/);
if i>=m || HT[probe].status==EMP then return -1;
return probe
```

```c
//Algo: HTdelete(HT,k)
i = -1;
repeat
    i++; probe = h(k,i);
until i>=m /*searched m slots without finding k*/ ‚ HT[probe].status==EMP /*end of chain*/|| HT[probe].status==OCC && HT[probe].key==k /*element found*/;

if i>=m || HT[probe].status==EMP then return -1;
HT[probe].status = DEL;
return probe
```