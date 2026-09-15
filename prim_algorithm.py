from graph_network import edges, nodes


def find_cheapest_connecting_edge(edges, visited):
    
    # Finds the shortest edge beetwen a visited node and an unvisited one.
    
    min_edge = None
    min_weight = float('inf')

    for edge in edges:
        node1, node2, weight = edge

        # Check if the nodes of the edge are already part of the tree or not
        is_node1_visited = node1 in visited
        is_node2_visited = node2 in visited

        # Exactly one node must be visited to connect a new node without forming a cycle
        if is_node1_visited != is_node2_visited:
            if weight < min_weight:
                min_weight = weight
                min_edge = edge

    return min_edge


def prim(nodes, edges):
    # Calculate the MST
    if not nodes or not edges:
        return []

    start_node = nodes[0]
    visited = set([start_node])
    mst = []

    # Continue until all nodes are included in the tree
    while len(visited) < len(nodes):
        cheapest_edge = find_cheapest_connecting_edge(edges, visited)

        if cheapest_edge is None:
            break  # Stop if the graph is disconnected

        # Add the shortest edge to the MST and update visited node
        mst.append(cheapest_edge)
        visited.add(cheapest_edge[0])
        visited.add(cheapest_edge[1])

    return mst


def calculate_total_weight(edges):

    return sum(edge[2] for edge in edges)


def run_prim():
    
    # Runs Prim's algorithm and prints the result.
    mst = prim(nodes, edges)
    total_weight = calculate_total_weight(mst)

    print("################################################")
    print("Prim Algorithm Result:")
    print("################################################")

    print("Minimum Spanning Tree:")
    for edge in mst:
        print(edge)

    print("Total weight: ", total_weight)

