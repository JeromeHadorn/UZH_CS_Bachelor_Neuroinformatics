# Summary SL10 Minimum Spanning Trees & Single Source Shorted Paths
## Weighted Graphs
Weighted graph
* Graph G = $(V, E)$ where each edge $(u, v) ∈ E$ has a weight
$w(u, v)$ specifying its cost (or length)
* In other words, G is endowed with a weight function
$w: E → R$ that assigns real numbers to its edges
* Note: weighted graphs can be directed or undirected

Weighted algorithms
* Minimum spanning tree
    * Apply to undirected graphs
    * Prim-Jarnik
* Single-source shortest path
    * Apply to directed graphs
    * Bellman-Ford, Dijkstra

# Minimum Spanning Tree
A spannign tree $T$ of G is subgraph that contains all the vertices (connected graph) of G and that is a tree (thus, acyclic)
* \# of edges in a MST = $|V| - 1$

A minimum spanning tree of $(G,w)$ is a spanning tree $T$ of $G$ that minimizes $w(T) = \sum_{(u,v) \in T}^w(u,v)$

### Generic Algorithm
* Have to make $|V|-1$ choices (edges of the MST) to arrive at solution
```c
A = {};
while A does not form a spanning tree do
    Find edge e that is safe for A;
    A = A ∪ {e}
return A;
```
* After each choice, get a subproblem that is one vertex smaller than the original problem
    * At each step, want to determine cheaply a save edge (i.e., I that definitely belongs to an MST)
    * Greedy choice property: locally optimal (i.e., greedy) choice yields a globally optimal solution
### Greedy Choice Algorithm
* Let $G=(V,E)$ and $S \sub V$ be a cut of G
* That is, G is split into parts $S$ (not covered) and $V-S$ (covered)
* $(u,v)$ is a **light edge** if it is a min-weight edge of G that connects $S$ and $V-S$ (e.g. (c, d) is such a light edge)

### Prim-Jarnik Algorithm
* Vertex-based algorithm
* Grows a single minimum spanning tree $T$
* Set A covers part of T that is already computed
    * Uses a $pred$ field to indicate the predecessor
* Annotates all the vertices v outside of the set A
    * $v.k$: minimum weight of an edge that connects vertex v with a vertex in A ($v.k$ = $\infin$ if no such edge exists)
* The algorithm relies on a min-priority queue
    * init_min_pq, min_extract, and decrease_key
* The running time of the algorithm is $O(E log V )$

```c
Algo: PrimJarnik(G,w,s)
// Initialization
foreach v ∈ G.V do
    v.key = infinity;
    v.pred = NIL;

s.key = 0;
InitMinPriorityQueue(PQ,G.V); // All nodes are in our PQ (s is first) in our PQ

// E times in total (for each node all its adjacent nodes = all edges)
while PQ != {} do
    v = ExtractMin(PQ);
    foreach u ∈ v.adj do
        if u ∈ P Q && w(v, u) < u.key then
            u.key = w(v,u);
            u.pred = v;
            DecreaseKey(PQ,u,w(u,v))
```

**Max Weight Adaptation**
```c
MaxST(G,s) // Prim Algo with MaxPQ
    for v ∈ G.v { v.key = -1: v.pred = NIL;}
    s.key = 0;
    initMaxPQ(Q, G.v);
    u = extractMax(Q);
    for v ∈ u.adj
        if (v ∈ Q && BW(u,v) > v.key) then
            v.key = BW(u,v)
            modifyKey(Q,v) // propagates up in priority queue
            v.pred = u
```

**Running Time**
* Time = $V$ * T(ExtractMin) + O(E) * T(DecreaseKey)
* Depends on the implementation of the priority queue

| Q     	    | T(ExtractMin) 	| T(DecreaseKey) 	| Total 	|
|---------------|---	|---	|-----	|
| Array 	    | O(V) 	| O(1) 	| O(V^2)   	| O(V^2)
| Binary Heap   | O(log V)  	| O(log V)   	| O(E log V)    	|

# Single-source shortest path (SSSP)

**Shortest paths**
* Generalize directed graphs to weighted setting
* Directed graph $(V, E)$, weight function $w : E \to R$
* Definition of weight of a path p = <v0, v1,...,vk>
* $w(p) = \sum_{i=0}^{k-1}w(vi, vi+1)$
* Shortest path = a path of minimum weight (cost)
* Single-source shortest path (SSSP) problem
    * Shortest path from source vertex $s$ to any other vertex
    * Other problems: single pair, all pairs, unweighted (BFS)

**Optimal substructure**
* The subpaths of shortest paths are shortest paths

**Negative weights**
* Negative weights are OK, as long as there are no negative-weight cycles
    * Otherwise, could get paths of arbitrary small “length”

**Paths and cycles**
* Shortest paths cannot have cycles
    * Otherwise, improve shortest path by removing cycles
    * No shortest path can have length greater than $|V|-1$

**Relaxation**
* For each vertex $v$ in the graph, maintain $v.dist$, the estimate of the shortest path from $s$
    * At the start, $v.dist$ is initialized to $\infin$ and $s.dist$ to 0
* Relaxing an edge $(u, v)$ means testing whether one can improve the shortest path to $v$ found so far by going through $u$
```c
Algo: Relax(u,v,w)
if v.dist > u.dist + w(u, v) then
    v.dist = u.dist + w(u,v);
    v.pred = u
```

In which sequence do we consider relax edges?

## Bellmann-Ford Algorithm
* Solves single-source shortest path problem for the case where edge weights may be negative
* Returns boolean value indicating whether there is a negative-weight cycle reachable from source vertex $s$.
* If there is such a cycle then no solution exists
* Employs relaxation, progressively decreasing v.dist
* The running time of the algorithm is $O(|E| · |V |)$

```c
Algo: BellmanFord(G,w,s)
//Initalization
foreach v ∈ G.V do
    v.dist = infinity;
    v.pred = NIL;

for i = 1 to |G.V|-1 do 
    // Because of negative weight edges there is no good order to consider the edges => we relax all edges |v|-1 times
    foreach (u, v) ∈ G.E do
        Relax(u,v,w); // cost : |V| * |E|

foreach (u, v) ∈ G.E do
    // If we can relax more than there is a negative weight cycle => use it to check for negative weight cycles.
    if v.dist > u.dist + w(u, v) then
        return FALSE;

return TRUE;
```

## SSSP IN DAGS
* Finding shortest paths in a DAG is much easier
* Topological sort determines order of relaxations
Algorithm:
1. sort G topologically
2. consider each vertex in topological sort order
3. relax each edge leaving the vertex
* We have one relaxation per edge, which gives a runtime of O(V + E) (V times faster than Bellman-Ford)
* Note: in a DAG there is no negative-weight cycle


## DIJKSTRA’S ALGORITHM
* Solves single-source shortest path problem for the case where edge weights are nonnegative
* Greedy, similar to Prim-Jarnik algorithm for MST
    * Uses a priority queue, changes dist instead of k
* In some respect also similar to breadth-first search
* v.dist does not change further once the vertex v is removed from the (priority) queue
* The running time of the algorithm is O(|E| lg |V |) (connected: O(|V| lg |V|), fully connected O(|V|^2 log |V|))
* It is thus lower than the running time of Bellman-Ford O(|V|^3)
 

```c
Algo: Dijkstra(G,w,s)
//Initalization
foreach v ∈ G.V do
    v.dist = infin;
    v.pred = NIL;

s.dist = 0;
InitMinPQ(PQ,G.V); // |V| elements in PQ s comes first

while PQ != {} do
    v = ExtractMin(PQ); // cost log(|V|) (heapify)
    foreach u ∈ v.adj do 
        Relax(u,v,w);
        DecreaseKey(PQ,u,u.dist) //cost: log(|V|) (move up in PQ)

=> O(|E| * log(|V|))
```