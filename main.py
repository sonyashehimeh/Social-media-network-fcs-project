
import networkx as nx
from graph import NetworkGraph
from user import User

def calculate_network_statistics(graph):
    number_of_users = len(graph.graph.nodes)
    num_edges = len(graph.graph.edges)
    density = nx.density(graph.graph)
    avg_friends = num_edges / number_of_users if number_of_users > 0 else 0
    return {
        "number_of_users": number_of_users,
        "num_edges": num_edges,
        "density": density,
        "avg_friends": avg_friends
    }

def recommended_friends(user, graph):
    if user.user_id not in graph.graph:
        return []
    
    friends_of_friends = set()
    for friend in graph.graph.neighbors(user.user_id):
        friends_of_friends.update(graph.graph.neighbors(friend))
    
    friends_of_friends.discard(user.user_id)
    friends_of_friends.difference_update(user.friends)
    
    return list(friends_of_friends)

def main():     # check notepad notes for menu
 
    graph = NetworkGraph()

    sally = User(1, "sally")
    samar = User(2, "samar")
    ali = User(3, "ali")

    graph.add_user(sally)
    graph.add_user(samar)
    graph.add_user(ali)

    graph.add_friend(ali, samar)
    graph.add_friend(samar, sally)
    graph.add_friend(ali, sally)

    print("Network Stats:", calculate_network_statistics(graph))
    print("Connections:", graph.connections())
    print("Friend recommended for sally:", recommended_friends(sally, graph))
    print("Breadth First Search for ali:", graph.Breadth_First_Search(ali))
    print("Depth 1st search for Ali:", graph.dfs(ali))

    graph.visualization()

'''
menu 
        print("\n1. Sign Up\n2. Add Freinds\n3. Remove Friends\n4. Display Users\n5. Network Visualization\n6. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            sign_up(social_network)
        elif choice == '2':
            user1_id = int(input("Enter your ID: "))
            user2_id = int(input("Enter friend's ID: "))

            add_relationship(social_network, user1_id, user2_id)
        elif choice == '3': user1_id = int(input("Enter your ID: "))
            user2_id = int(input("Enter friend's ID: "))
            remove_relationship(social_network, user1_id, user2_id)
        elif choice == '4':
            display_users(social_network)
        elif choice == '5':
            visualize_graph(social_network)
        else: if()
            choice == '6': print("exit")
            break
'''

if __name__ == "__main__":
    main()
    


