import networkx as nx
import matplotlib.pyplot as plt

def visualization_of_network(graph):
    G = nx.Graph()
    for user, frnds in graph.adjacency_list.items():
        for frnd in frnds:
            G.add_edge(user, frnd)
    
    nx.draw(G, with_labels=True)
    plt.show()
