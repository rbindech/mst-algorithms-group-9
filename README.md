# Minimum Spanning Tree Algorithms

## Identity

Informatics ITS Graph Theory class  
Group 9

Group members:

- Calixte Berthier - Prim's Algorithm
- Emmanuel Santini - Kruskal's Algorithm
- Rida Bindech - Reverse-Delete Algorithm

## Project Description

This project solves a Minimum Spanning Tree problem on a weighted undirected graph.

A Minimum Spanning Tree, or MST, is a subset of edges that connects all nodes in the graph with the minimum possible total weight, without creating any cycle.

In this project, three MST algorithms are implemented:

1. Prim's Algorithm
2. Kruskal's Algorithm
3. Reverse-Delete Algorithm

The project also includes a failure simulation, where a node or an edge cannot be traversed. After the failure, the algorithms are run again on the updated graph to check whether a new MST can still be generated.

## Graph Representation

The graph is represented using two main variables:

```python
nodes = ["A", "B", "C", "D", "E", "F", "G"]

edges = [
    ("A", "B", 7),
    ("A", "C", 6),
    ("A", "G", 5),
    ("A", "F", 10),
    ("B", "C", 5),
    ("B", "D", 7),
    ("B", "E", 9),
    ("C", "E", 9),
    ("C", "F", 7),
    ("D", "E", 5),
    ("E", "F", 5),
    ("F", "G", 6),
]
```

Each edge is represented as:

(node1, node2, weight)

Since the graph is undirected, an edge such as `("A", "B", 4)` means that node `A` is connected to node `B` with weight `4`, and the connection can be traversed in both directions.

This representation was chosen because it is simple and convenient for MST algorithms. Kruskal's Algorithm and Reverse-Delete Algorithm directly operate on sorted edge lists, while Prim's Algorithm can also use the same structure to find candidate edges.

## Algorithms Explanation

### Prim's Algorithm

Prim's Algorithm starts from one selected node and grows the Minimum Spanning Tree step by step.

At each step, the algorithm chooses the cheapest edge that connects a node already inside the tree to a node outside the tree. This process continues until all nodes are included in the tree.

In short:

1. Start from one node.
2. Find the cheapest edge connecting the current tree to a new node.
3. Add this edge and the new node to the tree.
4. Repeat until all nodes are connected.

### Kruskal's Algorithm

Kruskal's Algorithm sorts all edges by increasing weight.

It then adds the cheapest edges one by one, as long as adding the edge does not create a cycle. The algorithm stops when all nodes are connected.

In short:

1. Sort all edges from the smallest weight to the largest weight.
2. Take the cheapest available edge.
3. Add it only if it does not create a cycle.
4. Repeat until the MST contains `number_of_nodes - 1` edges.

### Reverse-Delete Algorithm

Reverse-Delete Algorithm works in the opposite direction compared to Kruskal's Algorithm.

It starts with the full graph and sorts all edges by decreasing weight. Then, it tries to remove the most expensive edges first.

For each edge:

- if removing the edge does not disconnect the graph, the edge is removed;
- if removing the edge disconnects the graph, the edge is kept.

At the end, the remaining edges form a Minimum Spanning Tree.

In short:

1. Start with the full graph.
2. Sort all edges from the largest weight to the smallest weight.
3. Try to remove each edge.
4. Keep the edge only if removing it disconnects the graph.
5. Return the remaining graph as the MST.

## Prerequisites

This project uses Python.

Required version:

Python 3.x

No external library is required.

## Project Structure

project/
  graph_network.py
  prim_algorithm.py
  kruskal_algorithm.py
  reverse_delete_algorithm.py
  main.py
  README.md

Description:

- `graph_network.py`: contains the graph input, including nodes and edges.
- `prim_algorithm.py`: contains the implementation of Prim's Algorithm.
- `kruskal_algorithm.py`: contains the implementation of Kruskal's Algorithm.
- `reverse_delete_algorithm.py`: contains the implementation of Reverse-Delete Algorithm.
- `main.py`: runs all algorithms and displays the results.

## How to Run

Open a terminal in the project folder and run:

```bash
python main.py
```

or:

```bash
python3 main.py
```

depending on your Python installation.


## Sample Run Result

```
################################################
Prim's Algorithm MST:
################################################
///

################################################
Kruskal's Algorithm Result:
################################################
Minimum Spanning Tree:
('A', 'G', 5)
('B', 'C', 5)
('D', 'E', 5)
('E', 'F', 5)
('A', 'C', 6)
('F', 'G', 6)
Total weight:  32
################################################
Reverse-Delete Algorithm MST:
################################################
Minimum Spanning Tree:
('A', 'C', 6)
('A', 'G', 5)
('B', 'C', 5)
('D', 'E', 5)
('E', 'F', 5)
('F', 'G', 6)
Total weight:  32
```

The order of the selected edges is different depending on the algorithm. However, the total weight and the minimum spanning tree are the same.

## Failure Simulation

The homework also requires a simulation where a node or an edge fails and cannot be traversed.

### Edge Failure

To simulate an edge failure, the failed edge is removed from the graph before running the algorithms.

- With Kruskal's algorithm, the failed edge is simply removed from the edge list before sorting. If the graph is still connected, it still outputs the new MST. But if the removed edge was a cut edge, the graph is split into two disconnected parts. So the algorithm will exhausts all valid edges and returns a single list of edges containing the edges of both trees together (a minimum spanning forest).

- With Prim algorithm, ###

- With Reverse Delete algorithm, it still gives the minimum spanning tree of this new network. 
If enough edges are deleted to the point the graph is no more connected, it still gives the "minimum spanning forest", which mean it gives the minimum spanning trees inside this non connected graph.

### Node Failure

To simulate a node failure, the failed node and all edges connected to it are removed from the graph.

- With Kruskal's algorithm, the failed node is excluded from the node list, and any edge connected to it is removed from the edge list before the sorting. If the remaining graph is still connected, the algorithm returns the new MST, if removing the node splits the remaining graph into disconnected parts (a cut vertex), the algorithm connects all possible vertices within each part and returns a single flat list of edges representing a minimum spanning forest.

- With Prim algorithm, ###

- With Reverse Delete algorithm, it simply acts like if the failed node doesn't exist but it still gives the minimum spanning tree of this new graph network.

## Notes

- The input graph is assumed to be connected before the failure simulation.
- The graph is assumed to be undirected and weighted.
- If multiple MSTs exist with the same total weight, the algorithms may return different sets of edges while still being correct.

## AI Tools Usage Disclosure

AI tools were used to help understand the algorithms, write comments, and prepare the README/report explanation.

The implementation was structured, reviewed, adapted, and tested by the group members.
