from Graphs.Graph import *
from Graphs.GraphDrawer import *

g = Graph()
g.nodes.append(Source())
for i in range(0, 4):
    g.nodes.append(Node())

g.nodes.append(Sink())

for i in range(0, 10):
    g.add_edges([
        (0, 1), (0, 2), (1, 3), (2, 3), (2, 4), (3, 5), (4, 5)       
    ])

drawer = GraphDrawer()
drawer.draw(g)

drawer.exit()
