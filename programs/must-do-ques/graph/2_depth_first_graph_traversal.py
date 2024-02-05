"""
Explanation:
------------
The depth-first graph algorithm uses the idea of backtracking. We exhaustively
search all the nodes by going ahead, if possible, or else by backtracking.

Here, the word ‘backtrack’ means to move forward as long as there are no more
nodes in the current path, then move backward on the same path to find nodes to
traverse.

In the following solution, we have used a stack to implement depth-first graph
traversal.

Note: As previously discussed for breadth-first traversal, before running the
algorithm, all |V| vertices must be marked as not-visited.

Time complexity:
----------------
Let EE be the set of all edges in the graph. The algorithm makes two calls to
DFS for each edge {u,v} in E: one time when the algorithm visits the neighbors
of u and one time when it visits the neighbors of v.

Hence, the time complexity of the algorithm is O(V + E).
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


def dfs(my_graph, source):
    """
    Function to print a DFS of graph
    :param graph: The graph
    :param source: starting vertex
    :return: returns the traversal in a string
    """

    # Mark all the vertices as not visited
    visited = [False] * (len(my_graph.graph))

    # Create a stack for DFS
    stack = []

    # Result string
    result = ""

    # Push the source
    stack.append(source)

    while stack:

        # Pop a vertex from stack
        source = stack.pop()

        if not visited[source]:
            result += str(source)
            visited[source] = True

        # Get all adjacent vertices of the popped vertex source.
        # If a adjacent has not been visited, then push it
        while my_graph.graph[source] is not None:
            data = my_graph.graph[source].vertex
            if not visited[data]:
                stack.append(data)
            my_graph.graph[source] = my_graph.graph[source].next

    return result


# Main to test the above program
if __name__ == "__main__":
    V = 5
    g = Graph(V)
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 3)
    g.add_edge(1, 4)

    print(dfs(g, 0))
