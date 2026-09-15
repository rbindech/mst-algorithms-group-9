from graph_network import edges, nodes
starting_node = edges[0][0]
current_edges = []
neighbor_edges = []

def Next_Nodes(current_edges)
    for edge in edges:
        node1, node2, weight = edge
        if node1 in current_edges and node2 not in visited:
            neighbor_edges.append (node2)
  
        if node2 == current_node and node1 not in visited:
            neighbor_edges.append(node1)
          
def IsthereNeighboor(current_edges)
 for e               
