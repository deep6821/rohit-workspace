"""
Time complexity:
----------------
The time complexity is O(n) because we visit n vertices.

Space complexity:
-----------------
The space complexity is O(n) because the HashMap requires n space to store all the vertices
"""
from random import shuffle


class Node:
    def __init__(self, d):
        self.data = d
        self.friends = []


def clone_rec(root, nodes_completed):
    if root is None:
        return None

    new_node = Node(root.data)
    nodes_completed[root] = new_node

    for p in root.friends:
        x = nodes_completed.get(p)
        if x is None:
            new_node.friends += [clone_rec(p, nodes_completed)]
        else:
            new_node.friends += [x]
    return new_node


def clone(root):
    nodes_completed = {}
    return clone_rec(root, nodes_completed)


# this is un-directed graph i.e.
# if there is an edge from x to y
# that means there must be an edge from y to x
# and there is no edge from a node to itself
# hence there can maximim of (nodes * nodes - nodes) / 2 edgesin this graph
def create_test_graph_directed(nodes_count, edges_count):
    vertices = []
    for i in range(0, nodes_count):
        vertices += [Node(i)]

    all_edges = []
    for i in range(0, nodes_count):
        for j in range(i + 1, nodes_count):
            all_edges.append([i, j])

    shuffle(all_edges)

    for i in range(0, min(edges_count, len(all_edges))):
        edge = all_edges[i]
        vertices[edge[0]].friends += [vertices[edge[1]]]
        vertices[edge[1]].friends += [vertices[edge[0]]]

    return vertices


def print_graph(vertices):
    for n in vertices:
        print(str(n.data), end=": {")
        for t in n.friends:
            print(str(t.data), end=" ")
        print()


def print_graph_rec(root, visited_nodes):
    if root is None or root in visited_nodes:
        return

    visited_nodes.add(root)

    print(str(root.data), end=": {")
    for n in root.friends:
        print(str(n.data), end=" ")
    print("}")

    for n in root.friends:
        print_graph_rec(n, visited_nodes)


def print_graph(root):
    visited_nodes = set()
    print_graph_rec(root, visited_nodes)


vertices = create_test_graph_directed(7, 18)
print_graph(vertices[0])
cp = clone(vertices[0])

print("\nAfter copy.")
print_graph(cp)
