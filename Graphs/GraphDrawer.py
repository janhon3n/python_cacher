from graphics import *
from .Graph import *

class GraphDrawer:
    def __init__(self):
        self.win = GraphWin("Graphs", 1000, 1000)
        self.win.setCoords(0,0,1000,1000)
        self.y_spacing = 200
        self.x_spacing = 150
        self.y_shift_ratio = 8

        self.node_radius = 10


    def draw(self, graph):
        def is_solo(node):
            return isinstance(node, Sink) or isinstance(node, Source)

        node_columns = []
        for node in graph.nodes:
            free_column_index = None
            for column_index, column in enumerate(node_columns):
                not_compatible = False
                for n in column:
                    if graph.have_common_edge(node, n) or (is_solo(node) or is_solo(n)):
                        not_compatible = True
                        break
                if not not_compatible:
                    free_column_index = column_index
                    break

            if free_column_index is None:
                node_columns.append([node])
            else:
                node_columns[free_column_index].append(node)


        graph_height = (max(len(column) for column in node_columns) + 1) * self.y_spacing
        graph_width = (len(node_columns) + 1) * self.x_spacing

        for i, column in enumerate(node_columns):
            x = (i+1) * self.x_spacing + (self.win.width - graph_width) / 2
            y_shift = (i+1) * (i+1) * self.y_shift_ratio % self.y_spacing
            for j, node in enumerate(column):
                y = (j+1) * self.y_spacing + (self.win.height - graph_height) / 2 + y_shift
                circ = Circle(Point(x, y), self.node_radius)
                if isinstance(node, Source):
                    circ.setFill("lightblue")
                if isinstance(node, Sink):
                    circ.setFill("red")
                circ.draw(self.win)
                node.draw_position = Point(x, y)

        for edge in graph.edges:
            line = Line(edge.node1.draw_position, edge.node2.draw_position)
            text = Text(Point(
                (edge.node1.draw_position.x + edge.node2.draw_position.x) / 2,
                (edge.node1.draw_position.y + edge.node2.draw_position.y) / 2,
            ), str(edge.flow) + " / " + str(edge.capacity))
            text.draw(self.win)
            line.draw(self.win)

    def exit(self):
        self.win.getMouse()
        self.win.close()