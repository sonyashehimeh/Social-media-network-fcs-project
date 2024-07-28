import networkx as nx
import matplotlib.pyplot as plt
from graph import Graph

def visualize_graph(graph):
    G = nx.Graph()
    for user_id, user in graph.users.items():
        G.add_node(user_id, label=user.name)
        for friend in user.friends:
            G.add_edge(user_id, friend.user_id)
    pos = nx.spring_layout(G)

    plt.show()
