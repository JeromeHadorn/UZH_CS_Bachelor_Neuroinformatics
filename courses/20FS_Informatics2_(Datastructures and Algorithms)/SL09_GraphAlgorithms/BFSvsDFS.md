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

## DFS may return several search trees
DFS (Depth-First Search) does not evaluate path costs. Therefore, there is no tie-breaker. DFS merely returns the first successful path it encounters. The particular path depends entirely on the order in which the continuation paths are ordered at each node. Thus, DFS on this graph can return any of the nine possible solutions.

For instance, assume the graph is connected with this ordering:

Node   edges to ...
 A       B C
 B       C D
 C       D A B
 D       F B C G E
 F       G D
 G       E F
 E       D G

Then the traversal is trivially A-B-C-D-F-G (first reference at each node). Other edge orderings will result in other solutions being returned.

Similarly, BFS may result in either of the 4-node solutions being returned.