# Summary: Chapter 10 Graphs

Such drawings are called graphs. The dots are called vertices (plural of vertex) and the lines between vertices are called edges.

In general, a graph consists of a **set of vertices** and a **set of edges connecting pairs of vertices**.

vertex set = {v1, v2, v3, v4, v5, v6}
edge set = {e1, e2, e3, e4, e5, e6, e7}

**Directed graphs** are graphs where edges have a direction:


Directed edges are called arrows and defined as ordered pairs of vertices instead of sets of vertices.

**Complete graphs** are graphs where all pair combinations of vertices are connected by edges.

The **degree** of a vertex v is the number of edges that end (or start) at v.

The **total degree** of a graph is the sum of the degrees of all its vertices.

The **total degree of a graph** is always twice the number of edges (Handshake Theorem).


## Trails, Paths, and Circuits
* **Trails**: routes that do not have a repeated edge,
* **Paths**: trails that do not have repeated vertices,
* **Circuits**: trails that start and end at the same vertex.
* **Simple circuits**: circuits that only pass through each vertex only once, except for the start and end vertices.

## Connectedness
* A graph is connected if it is possible to travel from any vertex to any other vertex along a sequence of adjacent edges of the graph.

* A graph G is not connected if, and only if, there are two vertices that are not connected by any walk.

## Euler Circuits
is a circuit that
* contains every vertex and every edge of G
* atleast on edge
* starts and ends at the same vertex, uses every vertex of G at least once, and uses every edge of G exactly once.

If g has an Eular circuit then every vertex of the graph has positive even degree.

## Hamiltonian Circuits
A Hamiltonian circuit for a graph G is a circuit that passes through all the vertices of G only once (except for the start and end vertices)

A Hamiltonian circuit does not need to include all edges, and hence may not be an Euler circuit.


However, if a graph G contains a Hamiltonian circuit H, then:
1. H must be connected
2. H must contain all vertices
3. The number of edges of H must equal the number of its vertices
4. Every vertex of H must have degree 2

If a graph G does not have a subgraph H with these properties, then G does not have a Hamiltonian circuit.

## Matrix Representation

An undirected graph can be similarly represented by an adjacency matrix. (mirrored)

## Isomorphisms of Graphs
Two graphs that are the same except for the labeling of their vertices and edges are called isomorphic (i.e., "same form").

## Rooted Trees
A rooted tree is a tree in which one vertex is designated the root. There is a unique path from the root to any other vertex v. The height of the tree is the maximum level of the tree.


A **binary tree** is a rooted tree where each vertex has at most two children.


## Spanning Trees and Shortest Paths
A Spanning tree for a graph G is a subgraph of G that contains every vertex of G and is a tree.


* Every connected graph as a spanning tree
* Any two spanning trees for a graph have the same number of edges

## Minimum Spanning Trees
A graph whose edges are labeled with numbers (weights) is called a weighted graph.

A minimum-weight spanning tree, or simply a minimum spanning tree, is a spanning tree for which the sum of the weights of all the edges is as small as possible.


## Kruskal Algorithm

Input: Connected weighted graph G = (V,E)
1. Initialize T := (V,∅) and m := 0
2. while (m < n - 1)
    2a. Find an edge e ∈ E of least weight
    2b. Delete e from E
    2c. if adding e to the edge set of T does not produce a circuit
        then add e to the edge set of T and set m := m + 1 
end while

Output: T

## Prim's Algorithm
Input: Connected weighted G = (V,E)
1. Pick a vertex v of G, remove v from V, and let T := ({v},∅)
2. for i := 1 to n 􏰀 1
    2a. Find an edge e of G such that (1) e connects T to one of the vertices in V, and (2) e has the least weight of all edges connecting T to V. Let w be the endpoint of e that is in V.
    2b. Add e and w to the edge and vertex sets of T
    2c. Delete w from V.

    *end*

Output: T


It can be shown that Kruskal and Prim always return a minimum spanning tree. The algorithms are thus correct.