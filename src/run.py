from Graphs.Graph import *
from Graphs.GraphDrawer import *
from Graphs.max_flow import *


g = Graph()
g.nodes.append(Source())
for i in range(0, 4):
    g.nodes.append(Node())

g.nodes.append(Sink())

print(len(g.edges))
g.add_edges([
    (0, 1, 5), (0, 2, 2), (1, 3, 2), (2, 4, 4), (3, 4, 1), (3, 5, 2), (4, 5, 5)       
])

ford_fulkerson(g)
