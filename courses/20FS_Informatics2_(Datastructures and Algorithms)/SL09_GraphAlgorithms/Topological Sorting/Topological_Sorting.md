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