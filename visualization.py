import networkx as nx
import matplotlib.pyplot as plt

def visualize_network(graph):
    G = nx.Graph()
    for user, friends in graph.adjacency_list.items():
        for friend in friends:
            G.add_edge(user, friend)
    
    nx.draw(G, with_labels=True)
    plt.show()
