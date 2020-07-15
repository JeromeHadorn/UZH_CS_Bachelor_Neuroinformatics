## Depth-first search (DFS)
A **depth-first search** (DFS) is like walking in a labyrinth with a string and following one path to the end:
* Start at vertex v, tie the end of the string to v and paint v gray.
* Set v as the current vertex and consider an arbitrary edge (v, u). (go in one direction)
* If the chosen edge leads to a non-white vertex u then return to v.
* Otherwise, unroll the string, move to u, paint u gray, set u as current vertex, and repeat the previous steps


**Properties**
* Eventually, one will get to a point where all edges from u lead to non-white vertices.
* Then, one backtracks by rolling up the string until one gets back to a previously visited vertex $v$.
* $v$ thus becomes the new current vertex and one can repeat the previous steps.


**DFS annotations**
* A DFS can be used to annotate vertices and edges with
additional information:
    * start time stime (when the vertex was visited first)
    * end time etime (when the vertex was visited last)
    * edge classification (tree, forward, back, or cross edge)
* Such annotations reveal useful information about the
graph that can be used by advanced algorithms.

**DFS time stamping**
* Vertex $v$ is white before $v.stime$, gray between $v.stime$ and $v.etime$, and black after $v.etime$.
* Gray vertices form a linear chain and the traversal of the
nodes works like a stack (LIFO).

```c
Algo: DFS(G) //Processes the entire graph
foreach v ∈ G.V do
    v.col = W; v.pred = NIL
time = 0;
foreach v ∈ G.V do
    if v.col==W then DFS-Tree(G,v);
```

```c
Algo: DFS-Tree(G,s) // Corresponds to BFS (searches all reachable nodes; search sequence is different)
s.col = G; // Start Node is Gray
time = time+1; s.time = time; // time is a discrete counter
foreach u ∈ s.adj do
    if u.col==W then
        u.pred = s;
        DFS-Tree(G,u) // Implemented through recursion or a stack
s.col = B; time = time+1; s.etime = time;
```


Some observations
* DFS guarantees that every vertex is visited
* Each call of DFS-Tree adds a new tree to depth-first forest
* After termination, every vertex has a start and end time


## DFS running time
* Given a graph G = (V, E)
    * Each loop in DFS takes time O(|V |), excluding the time to execute DFS-Tree
    * DFS-Tree is called once for every vertex
        * It is only invoked on white vertices
        * It paints the vertex gray immediately
    * Each time, DFS-Tree explores an adjacency list
    * Hence, the overall cost of DFS-Tree is O(|E|)
* Total running time: O(|V | + |E|) (linear in the size of the adjacency list representation of G)

