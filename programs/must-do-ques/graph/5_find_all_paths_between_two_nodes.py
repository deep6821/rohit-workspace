"""
Explanation:
------------
If we traverse the graph from the source using any graph traversal algorithm,
we can tell whether such a traversal will lead us to the desired destination
or not.

All we need to solve this problem is to simply traverse from source to see if
we can reach our destination using recursion. If the destination value is
found, we print that path.

Time complexity:
----------------
It has the same time complexity as any graph traversal algorithm, so that will
be O(V + E).
"""


class AdjNode:
    """
    A class to represent the adjacency list of the node
    """

    def __init__(self, data):
        """
        Constructor
        :param data : vertex
        """
        self.vertex = data
        self.next = None


class Graph:
    """
    Graph Class ADT
    """

    def __init__(self, vertices):
        """
        Constructor
        :param vertices : Total vertices in a graph
        """
        self.V = vertices
        self.graph = [None] * self.V

    # Function to add an edge in an undirected graph
    def add_edge(self, source, destination):
        """
        add edge
        :param source: Source Vertex
        :param destination: Destination Vertex
        """

        # Adding the node to the source node
        node = AdjNode(destination)
        node.next = self.graph[source]
        print("node :", node.vertex)
        self.graph[source] = node

        # Adding the source node to the destination if undirected graph
        # Intentionally commented the lines
        # node = AdjNode(source)
        # node.next = self.graph[destination]
        # self.graph[destination] = node
        print("self.graph: --->", self.graph)
        # for i in self.graph:
        #     print(i.vertex)

    def print_graph(self):
        """
        A function to print a graph
        """
        for i in range(self.V):
            print("Adjacency list of vertex {}\n head".format(i), end="")
            temp = self.graph[i]
            while temp:
                print(" -> {}".format(temp.vertex), end="")
                temp = temp.next
            print(" \n")


import copy  # For deep copy if needed


def find_all_paths_recursive(graph, source, destination, visited, path, paths):
    """
    Finds all paths between source and destination in given graph
    :param graph: A directed graph
    :param source: Source Vertex
    :param destination: Destination Vertex
    :param visited: A list to mark visited vertices
    :param path: List to store one path to source from destination
    :param paths: 2D list to store all paths
    """

    # Mark the current node as visited and store in path
    visited[source] = True
    path.append(source)

    # If current vertex is same as destination, then print
    # stores the current path in 2D list (Deep copy)
    if source == destination:
        paths.append(copy.deepcopy(path))
    else:
        # If current vertex is not destination
        # Recur for all the vertices adjacent to this vertex
        while graph.graph[source] is not None:
            i = graph.graph[source].vertex

            if not visited[i]:
                find_all_paths_recursive(graph, i, destination, visited, path,
                                         paths)

            graph.graph[source] = graph.graph[source].next

    # Remove current vertex from path[] and mark it as unvisited
    path.pop()
    visited[source] = False


def find_all_paths(graph, source, destination):
    """
    Finds all paths between source and destination in given graph
    :param graph: A directed graph
    :param source: Source Vertex
    :param destination: Destination Vertex
    """
    # Mark all the vertices as not visited
    visited = [False] * (graph.V)

    # Create a list to store paths
    paths = []
    path = []

    # Call the recursive helper function to find all paths
    find_all_paths_recursive(graph, source, destination, visited, path, paths)
    return paths


# Main program to test above function
if __name__ == "__main__":
    g = Graph(6)
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 3)
    g.add_edge(1, 4)
    g.add_edge(3, 5)
    g.add_edge(4, 5)
    g.add_edge(2, 5)

    source = 0
    destination = 5

    paths = find_all_paths(g, source, destination)
    print(paths)
