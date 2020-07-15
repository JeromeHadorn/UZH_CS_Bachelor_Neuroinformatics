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

void BellmanFord(struct Graph* graph, int src) 
{ 
    int V = graph->V; 
    int E = graph->E; 
    int dist[V]; 
  
    // Step 1: Initialize distances from src to all other vertices 
    // as INFINITE 
    for (int i = 0; i < V; i++) 
        dist[i] = INT_MAX; 
        dist[src] = 0; 
  
    // Step 2: Relax all edges |V| - 1 times. A simple shortest 
    // path from src to any other vertex can have at-most |V| - 1 
    // edges 
    for (int i = 1; i <= V - 1; i++) { 
        for (int j = 0; j < E; j++) { 
            int u = graph->edge[j].src; 
            int v = graph->edge[j].dest; 
            int weight = graph->edge[j].weight; 
            if (dist[u] != INT_MAX && dist[u] + weight < dist[v]) 
                dist[v] = dist[u] + weight; 
        } 
    } 
  
    // Step 3: check for negative-weight cycles.  The above step 
    // guarantees shortest distances if graph doesn't contain 
    // negative weight cycle.  If we get a shorter path, then there 
    // is a cycle. 
    for (int i = 0; i < E; i++) { 
        int u = graph->edge[i].src; 
        int v = graph->edge[i].dest; 
        int weight = graph->edge[i].weight; 
        if (dist[u] != INT_MAX && dist[u] + weight < dist[v]) { 
            printf("Graph contains negative weight cycle"); 
            return; // If negative cycle is detected, simply return 
        } 
    } 
  
    printArr(dist, V); 
  
    return; 
} 
```