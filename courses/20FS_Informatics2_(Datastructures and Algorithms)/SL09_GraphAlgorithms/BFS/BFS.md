##  Breadth-first search (BFS)
A **breadth-first search** (BFS) starts at vertex s and visits all vertices reachable from s
* In doing so BFS defines a **spanning tree** (a tree that
includes all vertices).

BFS is like walking in a labyrinth with a string and
exploring the **entire** neighborhood first (going in all directions)

The starting vertex s is assigned distance 0

In the first round the string is unrolled 1 unit
* All vertices that are one edge away from the starting vertex
s are visited and assigned distance 1


In the second round the string is unrolled 2 units
* All vertices that are two edges away from the starting
vertex s are visited and assigned distance 2
* Thus, all the vertices that can be reached by unrolling the string 2 units are assigned distance 2

This continues until every reachable vertex has been
assigned a distance

The label of any vertex $v$ corresponds to the length of the shortest path from $s$ to $v$

```c
Pseudo:
----------------------
create a queue Q 
mark v as visited and put v into Q 
while Q is non-empty 
    remove the head u of Q 
    mark and enqueue all (unvisited) neighbours of u
------------------------
Algo: BFS(G,s)


foreach v ∈ G.V do
    v.col = W;
    v.dist = ∞;
    v.pred = NIL // All Nodes are White

s.col = G; s.dist = 0; // Start Node becomes gray

/*
Initialization
Quere Q ehere shorter paths are before longer paths
(Priority queue, min-heap)
*/
InitQueue(Q); // Empty Queue
Enqueue(Q,s);

while Q ≠ ∅ do
    v = Dequeue(Q); // Removes First (= aka shortest) path
    foreach u ∈ v.adj do 
        if u.col==W then
            u.col = G;
            u.dist = v.dist+1;
            u.pred = v;
            Enqueue(Q,u);
    v.col = B;
```

**Size of Q in the general Case**
f = fanout (= nr of adjacent nodes)
d = depth of tree
\# of nodes at level d = $f^{d}$ (Exponential growth in d; / bounded by |V|)


**Does the ordering of adjacency lists affect the distances from the starting node computed by BFS?** No


**Does the ordering of adjacency lists affect the BFS tree?** BFS tree is affected



### BFS running time
* Given a graph G = (V, E)
    * Initializing the vertices takes time O(|V |)
    * Vertices are enqueued if their color is white
        * Assuming that en- and dequeueing takes time O(1), the total cost of this operation is O(|V |)
    * The adjacency list of a vertex is scanned when the vertex is dequeued
        * Since the sum of the lengths of all the adjacency lists is O(|E|), the cost of scanning is O(|E|)
* Total running time: O(|V | + |E|) (linear in the size of the adjacency list representation of G)



**Assume a graph G = (V, E):**
* BFS discovers **all vertices reachable** from a source vertex s.
* BFS computes **the shortest distance** to all reachable
vertices.
* BFS computes a **breadth-first tree** that contains every
reachable vertex.
* For any vertex v reachable from s, the path from s to v in the breadth-first tree corresponds to a **shortest path** in G.