class Node:
    def __init__(self, value=0):
        self.value = value

class Edge:
    def __init__(self, node1, node2, capacity=1, directed=True):
        self.node1 = node1
        self.node2 = node2
        self.capacity = capacity
        self.directed = directed
        self.flow = 0

class Graph:
    nodes = []
    edges = []

    def add_edges(self, tuples):
        for t in tuples:
            self.edges.append(Edge(self.nodes[t[0]], self.nodes[t[1]]))

    def have_common_edge(self, node1, node2):
        for edge in self.edges:
            if (edge.node1 is node1 and edge.node2 is node2) or (edge.node2 is node1 and edge.node1 is node2):
                return True
        return False


class Source(Node):
    pass

class Sink(Node):
    pass
