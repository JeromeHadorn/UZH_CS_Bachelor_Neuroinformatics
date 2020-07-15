#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

struct node {
  int data;
  struct node* next;
};

struct Graph {
  int numVertices;
  bool* visited;
  // We need int** to store a two dimensional array.
  // Similary, we need struct node** to store an array of Linked lists
  struct node** adjLists;
};

struct Graph* createGraph(int vertices) {
  struct Graph* graph = malloc(sizeof(struct Graph));
  graph->numVertices = vertices;
  graph->adjLists = malloc(vertices * sizeof(struct node*));
  graph->visited = malloc(vertices * sizeof(bool));
  int i;
  for (i = 0; i < vertices; i++) {
    graph->adjLists[i] = NULL;
    graph->visited[i] = false;
  }
  return graph;
}

struct node* createNode(int v) {
  struct node* newNode = malloc(sizeof(struct node));
  newNode->data = v;
  newNode->next = NULL;
  return newNode;
}

void addEdge(struct Graph* graph, int src, int dest) {
  // Add edge from src to dest
  struct node* newNode = createNode(dest);
  newNode->next = graph->adjLists[src];
  graph->adjLists[src] = newNode;

  // Add edge from dest to src
  newNode = createNode(src);
  newNode->next = graph->adjLists[dest];
  graph->adjLists[dest] = newNode;
}

//queue functions
int del(struct node** head, int* element){
	if (*head == NULL)
		return 1;
	*element = (*head)->data;
	struct node* temp;
	temp = *head;
	*head = (*head)->next;
	free(temp);
	return 0;
}
int add(struct node** head, int element){
	if ((*head) == NULL){
		*head = (struct node*)malloc(sizeof(struct node));
		(*head)->next = NULL;
		(*head)->data = element;
		return 0;
	}
	struct node* temp = *head;
	while (temp->next != NULL){
		temp = temp->next;
	}
	temp->next = (struct node*)malloc(sizeof(struct node));
	if (temp->next == NULL)
		return 1;
	temp = temp->next;
	temp->data = element;
	temp->next = NULL;
	return 0;
}

bool isSubgraphCyclic(struct Graph* graph, int s){
	int V = graph->numVertices;
	int parent[V];
	int i = 0;
	for (i=0; i<V; i++) {
		parent[i] = -1;
	}
    struct node *Queue = NULL;
    add(&Queue, s);
    graph->visited[s] = true;
    while (Queue != NULL) {
        int u = Queue->data;
        del(&Queue, &u);

		struct node* tmp = graph->adjLists[u];
        while (tmp != NULL) {
			if (!graph->visited[tmp->data]) {
				graph->visited[tmp->data] = true;
				add(&Queue, tmp->data);
				parent[tmp->data] = u;
			}
			else if (parent[u] != tmp->data) {
				return true;
			}
			tmp = tmp->next;
		}
    }
	return false;
}

// Function to check cyclic in case of of disconnected graph
bool isGraphCyclic(struct Graph* graph) 
{ 
	int V = graph->numVertices;
    int i = 0; 
    for (i = 0; i < V; i++) {
		if (!graph->visited[i] && isSubgraphCyclic(graph, i)) 
            return true;
	} 
    return false; 
} 

void BFS(struct Graph* graph, int vertex){
    // Initialization 1


    // or Initialization 2
    
}


int main() {
  struct Graph* graph = createGraph(5);
  addEdge(graph, 0, 1);
  addEdge(graph, 0, 2);
  addEdge(graph, 1, 2);
  addEdge(graph, 0, 3);
  addEdge(graph, 3, 4);
  
  if (isGraphCyclic(graph)) {
	  printf("True");
  }
  else {
	  printf("False");
  }

  return 0;
}
