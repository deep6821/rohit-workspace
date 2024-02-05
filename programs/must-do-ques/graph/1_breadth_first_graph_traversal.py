"""
Explanation:
------------
In this algorithm, we begin from a selected node (it can be a root node) and
traverse the graph layer wise (one level at a time).

All neighbor nodes (those connected to the source node) are explored, then, we
move to the next level of neighbor nodes.

Simply, as the name breadth-first suggests, we traverse the graph by moving
horizontally, visiting all the nodes of the current layer, and moving to the
next layer.

Avoid visiting the same nodes again:
------------------------------------
A graph may contain cycles, which will lead to visiting the same node again and
again, while we traverse the graph. To avoid processing the same node again,
we can use a boolean array that marks visited arrays.

*** The queue follows the First In First Out (FIFO) queuing method. Therefore,
neighbors of the node will be visited in the order in which they were inserted
in the queue, i.e. the node that was inserted first will be visited first and
so on. ***

Time complexity:
----------------
The time complexity of BFS can be computed as the total number of iterations
performed by the while loop in the code above.

Let E be the set of all edges in the connected component visited by the
algorithm. For each edge u,v in E the algorithm makes two while loop
iteration steps: one time when the algorithm visits the neighbors of uu and one
time when it visits the neighbors of v.

Hence, the time complexity is O(|V| + |E|).
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


def bfs(my_graph, source):
    """
    Function to print a BFS of graph
    :param graph: The graph
    :param source: starting vertex
    :return:
    """

    # Mark all the vertices as not visited
    visited = [False] * (len(my_graph.graph))

    # Create a queue for BFS
    queue = []

    # Result string
    result = ""

    # Mark the source node as visited and enqueue it
    queue.append(source)
    visited[source] = True

    while queue:

        # Dequeue a vertex from queue and print it
        source = queue.pop(0)
        result += str(source)

        # Get all adjacent vertices of the dequeued vertex source. If a
        # adjacent has not been visited, then mark it visited and enqueue it
        while my_graph.graph[source] is not None:
            data = my_graph.graph[source].vertex
            if not visited[data]:
                queue.append(data)
                visited[data] = True
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

    print(bfs(g, 0))
