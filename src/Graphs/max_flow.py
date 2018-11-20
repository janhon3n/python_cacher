from Cacher import *
from .Graph import *
from .GraphDrawer import *

gd = GraphDrawer()

def create_residual_graph(graph):
    r_graph = Graph()
    for node in graph.nodes:
        r_graph.nodes.append(node.copy())

    for edge in graph.edges:
        r_node1 = r_graph.nodes[graph.nodes.index(edge.node1)]
        r_node2 = r_graph.nodes[graph.nodes.index(edge.node2)]

        if edge.flow < edge.capacity:
            r_edge = Edge(r_node1, r_node2, capacity=(edge.capacity - edge.flow))
            r_edge.is_forward = True
            r_edge.original = edge
            r_graph.edges.append(r_edge)

        if edge.flow > 0:
            r_edge = Edge(r_node2, r_node1, capacity=edge.flow)
            r_edge.is_forward = False
            r_edge.original = edge
            r_graph.edges.append(r_edge)

    return r_graph


def find_path(graph):
    source = graph.get_source()
    def _find_path(path_so_far, node):
        for edge in graph.get_edges_from(node):
            if edge in path_so_far:
                continue
            new_node = edge.node2
            if isinstance(new_node, Sink):
                return path_so_far + [edge]
            else:
                path = _find_path(path_so_far + [edge], new_node)
                if path:
                    return path
        return None

    return _find_path([], source)


def ford_fulkerson(g):
    graph = g.copy()
    gd.draw(graph)
    r_graph = create_residual_graph(graph)
    path = find_path(r_graph)
    while path is not None:
        max_flow = min(e.capacity for e in path)
        for edge in path:
            edge.original.flow += max_flow if edge.is_forward else -max_flow
        r_graph = create_residual_graph(graph)
        path = find_path(r_graph)
        gd.draw(graph)
    return graph