from graph_network import edges, nodes


def sort_edges_descending(edges):
    """
    Sorts the edges by decreasing weight.

    Reverse-Delete starts by trying to remove the most expensive edges first.
    """
    return sorted(edges, key=lambda edge: edge[2], reverse=True)


def dfs(current_edges, current_node, target_node, visited):
    """
    Checks whether there is a path from current_node to target_node
    using depth-first search.

    The graph is undirected, so each edge can be explored in both directions.
    """
    if current_node == target_node:
        return True

    visited.add(current_node)

    for edge in current_edges:
        node1, node2, weight = edge

        # Explore the edge from node1 to node2.
        if node1 == current_node and node2 not in visited:
            if dfs(current_edges, node2, target_node, visited):
                return True

        # Explore the same edge in the opposite direction.
        if node2 == current_node and node1 not in visited:
            if dfs(current_edges, node1, target_node, visited):
                return True

    return False


def can_remove_edge(edge_to_remove, current_edges):
    """
    Tests whether an edge can be removed without disconnecting the graph.

    An edge can be removed if its two endpoints are still connected
    through another path after removing it.
    """
    start_node = edge_to_remove[0]
    target_node = edge_to_remove[1]

    edges_without_removed_edge = [
        edge for edge in current_edges
        if edge != edge_to_remove
    ]

    visited = set()

    return dfs(
        edges_without_removed_edge,
        start_node,
        target_node,
        visited
    )


def reverse_delete(nodes, edges):
    """
    Applies the Reverse-Delete algorithm to find a minimum spanning tree.

    The algorithm processes edges from the highest weight to the lowest.
    If removing an edge does not disconnect the graph, the edge is deleted.
    Otherwise, it is kept.
    """
    current_edges = edges.copy()
    sorted_edges = sort_edges_descending(edges)

    for edge in sorted_edges:
        if can_remove_edge(edge, current_edges):
            current_edges.remove(edge)

    return current_edges


def calculate_total_weight(edges):
    """
    Calculates the total weight of a list of edges.
    """
    return sum(edge[2] for edge in edges)


def run_reverse_delete():
    """
    Runs the Reverse-Delete algorithm and prints the result.
    """
    mst = reverse_delete(nodes, edges)
    total_weight = calculate_total_weight(mst)

    print("################################################")
    print("Reverse-Delete Algorithm Result:")
    print("################################################")

    print("Minimum Spanning Tree:")
    for edge in mst:
        print(edge)

    print("Total weight: ", total_weight)