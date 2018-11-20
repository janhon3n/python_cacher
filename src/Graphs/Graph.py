class Node:
    def __init__(self, value=0):
        self.value = value

    def copy(self):
        if isinstance(self, Source):
            return Source(value=self.value)
        if isinstance(self, Sink):
            return Sink(value=self.value)
        return Node(value=self.value)


class Edge:
    def __init__(self, node1, node2, capacity=10, directed=True):
        self.node1 = node1
        self.node2 = node2
        self.capacity = capacity
        self.directed = directed
        self.flow = 0

class Graph:
    def __init__(self):
        self.nodes = []
        self.edges = []

    def add_edges(self, tuples):
        for t in tuples:
            edge = Edge(self.nodes[t[0]], self.nodes[t[1]])
            if len(t) >= 3:
                edge.capacity = t[2]
            self.edges.append(edge)
        print(len(self.edges))

    def have_common_edge(self, node1, node2):
        for edge in self.edges:
            if (edge.node1 is node1 and edge.node2 is node2) or (edge.node2 is node1 and edge.node1 is node2):
                return True
        return False

    def get_sink(self):
        for node in self.nodes:
            if isinstance(node, Sink):
                return node
        raise Exception('No sink in graph')
        
    def get_source(self):
        for node in self.nodes:
            if isinstance(node, Source):
                return node
        raise Exception('No source in graph')

    def get_edges_from(self, node):
        for edge in self.edges:
            if edge.node1 is node:
                yield edge

    def copy(self):
        g = Graph()
        for n in self.nodes:
            g.nodes.append(n.copy())

        for e in self.edges:
            n1_index = self.nodes.index(e.node1)
            n2_index = self.nodes.index(e.node2)
            g.edges.append(Edge(g.nodes[n1_index], g.nodes[n2_index], capacity=e.capacity, directed=e.directed))
        return g

class Source(Node):
    pass

class Sink(Node):
    pass
