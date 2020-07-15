# Summary: SL09-Graphs
A **graph** G = (V, E) consists of
* a finite set of **vertices** V
* a set of edges E ⊆ V × V
* An **edge** e = (u, v) is a pair of vertices
* Generally assume **directed graphs** where edges are
directed (go from one node to another node)
* **Undirected graphs**:
    * edges are unordered pairs {u, v}
    * V = {a, b, c, d} & E = {{a, b}, {a, c}, {b, c}, {c, d}}


* Vertex v is **adjacent** to vertex u iff (u, v) ∈ E
* The **degree** of a vertex is defined as follows
    * number of adjacent vertices (undirected graph)
    * number of incoming and outgoing edges (directed graph)
        * **in-degree**: number of incoming edges
        * **out-degree**: number of outgoing edges
* A **path** of length $k$ is a sequence $h_{v0}$, . . . , $v_{ki}$ of vertices
such that, for all i ∈ {1, . . . , k}, $v_{i}$
is adjacent to $v_{i−1}$


**Simple path**: path <v0, . . . , vk> with vi != vj for i != j
**Cycle**: a simple path <v0, . . . , vk>, except that vk = v0
**Connected graph**: every pair of vertices is connected by a
path
**Subgraph**: subset of vertices and edges that forms a graph
**Connected component**: maximal connected subgraph
**Tree**: connected graph with n vertices and n − 1 edges
**Forest**: collection of trees

### Graph Representation
Represent graph by an adjacency matrix M(|V | × |V |)
* M[x, y] = 1 if there is an edge e = (x, y) in the graph
* M[x, y] = 0 if there is no edge e = (x, y) in the graph

Space requirements: $Θ(|V|^{2})$


(Connected) $|V|-1$ <= $|E|$ <= $|V|^{2}$ (Fully connected)$

**Consider an adjacency list representation of a directed graph. How long does it take to compute the in- and out-degree of a
vertex?**
Directed Graph:
* out-degree: E/V on average ~ $O(V)$ ~ scan 1 adjacency list
* in-degree: scan all adj. lists ~ E ~ $O(|v|^{2})$

Undirected Graph:
* $O(V)$ in both cases since in-degree = out-degree (scan 1 adjacency list)

## Graph Search
Coloring is used to color vertices during a traversal. The colors
allow to infer properties about the graph.
* Color changes during traversal
* Vertex v is white (i.e., v.col = W)
    * Means that v is undiscovered
* Vertex v is gray (i.e., v.col = G)
    * Means that v has been discovered but not all adjacent
vertices have been explored
* Vertex v is black (i.e., v.col = B)
    * Means that v has been discovered and all the adjacent vertices have been explored
    * In other words, the adjacency list of v was examined
completely


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
Algo: BFS(G,s)


foreach v ∈ G.V do
    v.col = W; v.dist = ∞; v.pred = NIL // All Nodes are White

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
            u.col = G; u.dist = v.dist+1; u.pred = v; Enqueue(Q,u)
    v.col = B;
```

**Size of Q in the general Case**
f = fanout (= nr of adjacent nodes)
d = depth of tree
\# of nodes at level d = $f^{d}$ (Exponential growth in d; / bounded by || V)


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



# DFS versus BFS
BFS visits **all vertices that are reachable** from s
* returns a single search tree
* might not visit all nodes
* considers all directions (paths)
* finds optimal (shortest) path
* expensive (chess)
* is used selectively (on small subproblems)
* O(V + E)

DFS visits **all vertices** in the given graph G
* may return several search trees
* visits all nodes
* pursues one direction (path)
* can get “lost” (maze)
* cheap and practical
* O(V + E)

The difference (visiting all nodes versus visiting reachable nodes) comes from the applications that make use of BFS and DFS

Note: the behavior of the graph search algorithms (i.e., to search the entire graph or only part of it) could easily be changed

## Edge classification
* Tree edge (gray node to white node)
    * Edges in depth-first (DF) forest
* Back edge (gray node to gray node)
    * Edges from descendant to ancestor in DF tree
    * Self-loops are a special case of back edges
* Forward edge (gray node to black node)
    * Non-tree edges from ancestor to descendant in DF tree
* Cross edge (gray node to black node)
    * Remaining edges of graph, i.e., edges between trees or
subtrees
* In DFS, the color of the vertex decides the type of the edge
* It is thus impossible to distinguish forward and cross edges
* Most algorithms do not distinguish between these two
types
* Tree and back edges are important (e.g., to detect loops)

# Topological Sorting
Definition of DAG
* A directed acyclic graph (DAG) is a directed graph
without cycles
* DAGs are used to indicate precedence among events (x
must happen before y)
* An example would be a parallel execution of code
* One gets a total order using topological sorting

DAG theorem
* A directed graph G is acyclic iff DFS of G has no back edges
* Thus, DFS can be used to check if a graph is a DAG

Proof of theorem
* Suppose there is a back edge (u, v)
    * Then v is an ancestor of u in depth-first forest
    * Hence, there is a path from v to u in the graph
    * Such a path together with (u, v) yields a cycle
* Suppose there is a cycle c in G
    * Let v be the first vertex in c to be discovered
    * Let u be a predecessor of vertex v in cycle c
    * Upon discovering v the path from v to u is white
    * Visiting this path makes u become a descendant of v
    * It follows that edge (u, v) is a back edge


**Sorting of DAGs**
* Topological sorting is used to sort DAGs
* A topological sort of a DAG is a linear ordering of all its vertices s.t., for any edge (u, v) in the DAG, u appears before v in the ordering

```c
Algo: TopologicalSort(G)
Call DFS(G) to compute v.etime for each v;
As each vertex v is finished:
insert v at the beginning of a linked list;
Return the linked list of vertices
```


**Correctness**
* DAG and (u, v) ∈ E imply u.etime > v.etime
* When the edge (u, v) is explored, u is gray
* So, one can distinguish the following cases
* v.col = G: (u, v) is a back edge (cycle, contradiction)
* v.col = B: v is already finished, so v.etime < u.etime
* v.col = W: v becomes a descendant of u, so v will be
finished before u and v.etime < u.etime
* The definition of topological sort is satisfied

**Running time**
* Total running time of topological sort is O(|V | + |E|)
* Running time of DFS plus |V | insertions into linked list