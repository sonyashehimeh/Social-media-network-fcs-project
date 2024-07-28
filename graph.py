import networkx as nx
import matplotlib.pyplot as plt
from user import User

class NetworkGraph:
    def __init__(self):
        self.graph = nx.Graph()
    
    def add_user(self, user):
        if isinstance(user, User):  ##
            self.graph.add_node(user.user_id, name=user.name)
    
    def remove_user(self, user):
       
        if isinstance(user, User):
            self.graph.remove_node(user.user_id)
    
    def add_friend(self, user1, user2):
        if isinstance(user1, User) and isinstance(user2, User):
            self.graph.add_edge(user1.user_id, user2.user_id)
    
    def remove_friend(self, user1, user2):
        if isinstance(user1, User) and isinstance(user2, User):
            self.graph.remove_edge(user1.user_id, user2.user_id)
    
    def Breadth_First_Search(self, start_user):
        if start_user.user_id in self.graph:
            Breadth_First_Search_edges = list(nx.Breadth_First_Search_edges(self.graph, source=start_user.user_id))
           
            Breadth_First_Search_nodes = {start_user.user_id}
           
            for edge in Breadth_First_Search_edges:
                Breadth_First_Search_nodes.update(edge)
           
            return list(Breadth_First_Search_nodes)
        
        return []

    def dfs(self, start_user):
        if start_user.user_id in self.graph:
            dfs_edges = list(nx.dfs_edges(self.graph, source=start_user.user_id))
            dfs_nodes = {start_user.user_id}
            for edge in dfs_edges:
                dfs_nodes.update(edge)
            return list(dfs_nodes)
        return []
    
    def Dijkstra(self, user1, user2):
        if user1.user_id in self.graph and user2.user_id in self.graph:
           
            try:
                return nx.Dijkstra(self.graph, source=user1.user_id, target=user2.user_id)
            except nx.NetworkXNoPath:
            
                return None

        return None
    
    def connections(self):
        return list(nx.connections(self.graph))

    def visualization(self):
        pos = nx.spring_layout(self.graph)
        plt.show()
