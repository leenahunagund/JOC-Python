import networkx as nx
import matplotlib.pyplot as plt

''' G=nx.Graph()
l=[1,2,3]
G.add_nodes_from(l)
G.add_node(1)
G.add_node(2)
G.add_node(3)
G.add_edge(1, 2)
#G.add_edge(2, 1)
G.add_edge(2, 3)
G.add_edge(1, 3)
#G.add_edge(3, 1)
#G.add_edge(3, 2)
print(G.edges())'''
# G=nx.complete_graph(10)
#G= nx.complete_graph(20)
G=nx.gnp_random_graph(20,0.5)
nx.draw_networkx(G)
plt.show()