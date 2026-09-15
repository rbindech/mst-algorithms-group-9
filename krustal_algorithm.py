from graph_network import edges, nodes

def find_set(node, sets):
    for s in sets:
        if node in s:
            return s
    return None

def kruskal(nodes, edges):
    mst = []
    # each node starts in its own set
    components = [{node} for node in nodes]

    # sort edges by weight
    sorted_edges = sorted(edges, key=lambda edge: edge[2])

    for edge in sorted_edges:
        u, v, weight = edge
        set_u = find_set(u, components)
        set_v = find_set(v, components)

        # if the two nodes are not already connected (no cycle)
        if set_u != set_v:
            components.remove(set_u)
            components.remove(set_v)
            components.append(set_u.union(set_v))  # fusion of the two sets
            mst.append(edge)

            if len(mst) == len(nodes) - 1:
                break

    return mst


def calculate_total_weight(edges):
    weight = 0
    for edge in edges :
        weight += edge[2]
    return weight


def run_kruskal():
    mst = kruskal(nodes, edges)
    total_weight = calculate_total_weight(mst)

    print("################################################")
    print("Kruskal's Algorithm Result:")
    print("################################################")
    print("Minimum Spanning Tree:")
    for edge in mst:
        print(edge)
    print("Total weight: ", total_weight)

run_kruskal()
