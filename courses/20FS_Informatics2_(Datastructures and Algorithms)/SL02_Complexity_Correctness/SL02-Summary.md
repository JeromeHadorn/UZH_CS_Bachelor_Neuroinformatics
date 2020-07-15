# Summary: SL02 Complexity and Correctness
## Algorithmic complexity
### Efficiency
* Predicting the resources that the algorithm requires
    * Resources in terms of time: running time
    * Resources in terms of space: memory usage
* Efficiency (use of resources) depends on input size
* Various ways of determining the size of input data
    * Depends on the problem being studied
    * Number of items in the input (e.g. sorting) 􏰀 Total number of bits (e.g. integer arithmetic)
* Must have a model of the implementation technology
### Best, Worst and Average Case
* Usually, one focuses on worst case running time
* There are basically the following three reasons
    * Worst case running time provides an upper bound
        * Guarantee that algorithm will never take any longer
    * For some algorithms, worst case occurs fairly often
        * Example:searching for an element that is not present
    * Average case is often roughly as bad as worst case
        * Example:insertion sort is still quadratic on average
* Might be quite difficult to find typical average case


## Binary Search
How many times is the loop executed?
* Each iteration the difference between r, l is cut in half
    * Initially the difference is n
    * Stops when it becomes 0
* How many times do we have to cut n in half to get 0?
    * log2 n — better than brute-force linear search (n)
* Cost of linear versus cost of binary search
    * For n = 0.2M one gets log2 200′000 ≈ 18
    * For n = 2M one gets log2 2′000′000 ≈ 21
    * For n = 20M one gets log2 20′000′000 ≈ 24
```c
int binSearch(int arr[], int n, int v){
    int l = 0;
    int r = n-1;
    int m;

    m = (int)floor((l+r)/2);

    while (l <= r && v != arr[m]){
        if (v < arr[m]){
            r = m-1;
        } else {
            l = m+1;
        }
        m = (int)floor((l+r)/2);
    }

    if (l <= r){
        return m;
    } else {
        return -1;
    }
}
```
## Correctness
### Pre/post-conditions
* **Assertion**: statement about the state of execution
    * Example:A[1],...,A[i]formanincreasingsequence
* To prove partial correctness one associates a number of assertions with specific checkpoints in the algorithm
* **Preconditions**: assertions that must be valid before the execution of an algorithm or a subroutine (input)
* **Postconditions**: assertions that must be valid after the execution of an algorithm or a subroutine (output)
## Asymptotic Complexity
#### Logarithm Rules
* log<sub>a</sub>(bc) = log<sub>a</sub>b + log<sub>a</sub>c
* log<sub>a</sub>b=log<sub>c</sub>b/log<sub>c</sub>a
* log<sub>a</sub> b<sup>c</sup> = c log<sub>a</sub> b
* a<sup>m</sup>a<sup>n</sup> = a<sup>m+n</sup>
* a<sup>mn</sup> = (a<sup>m</sup>)<sup>n</sup>
* a<sup>log<sub>a</sub> b</sup> = b
* lg b = ldb = log<sub>2</sub>b
* Notation: log<sub>a</sub> b = <sup>a</sup>log b
 
### Big-O notation
* Asymptotic upper bound
* Used for worst-case analysis
* f(n) and g(n) are functions over non-negative integers
* f(n) = O(g(n)) if and only if there exist constants c > 0 and n<sub>0</sub> >0 such that f(n) ≤ cg(n) for n ≥ n<sub>0</sub>


### Big-Ω notation
* Asymptotic lower bound
* Used for best-case analysis
* f(n) = Ω(g(n)) if and only if there exist constants c > 0 and n<sub>0</sub> >0 such that cg(n) ≤ f(n) for n≥n<sub>0</sub>


### Big Θ notation
* Asymptotic tight bound
* f(n) = Θ(g(n)) if and only if there exist constants c1 > 0, c2 >0,and n<sub>0</sub> > 0 such that c<sub>1</sub> g(n) ≤ f(n) ≤ c<sub>2</sub>g(n) for n ≥ n<sub>0</sub>
  * f(n) = Θ(g(n)) iff f(n) = O(g(n)) and f(n) = Ω(g(n))
* O(f(n)) is sometimes (ab)used as notation for Θ(f(n))
### Order of Growth
* f(n)=O(g(n))  ↔ f ≤ g
* f(n)=o(g(n))  ↔ f < g
* f(n)=Ω(g(n))  ↔ f ≥ g
* f(n)=ω(g(n))  ↔ f > g
* f(n)=Θ(g(n))  ↔ f = g
## Special case analysis
Special cases
* Data structure (array, list, file, etc.)
    * Empty, single element, completely filled
* Particular values, border of domain
    * Zero, empty string, negative numbers, etc.
* Calling of functions (procedures)
    * Entering function, termination of function
* Control and loop statements
    * Start of loop, end of loop, 1st iteration