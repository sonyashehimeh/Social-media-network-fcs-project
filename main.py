from graph import Graph
from user import User
import visualization as vz

def menu():
    network = Graph()
    while True:
        print("1. Sign Up") # to create account
        print("2. Add Friend")
        print("3. Remove Friend")
        print("4. Remove Account") # to delete users account
        print("5. Visualize Network")
        print("6. Exit")

        #create menu 
        choice = input("Enter choice: ")

        if choice == "1":
            user_id = input("Enter user ID: ")
            name = input("Enter name: ")
            user = User(user_id, name)
            network.add_user(user)
            print(f"User {name} added.")

        elif choice == "2":
            user1_id = input("Enter your user ID: ")
            user2_id = input("Enter friend's user ID: ")
            network.add_frnds(user1_id, user2_id)
            print(f"Friend {user2_id} added to user {user1_id}.")

        elif choice == "3":
            user1_id = input("Enter your user ID: ")
            user2_id = input("Enter friend's user ID to remove: ")
            network.remove_frnds(user1_id, user2_id)
            print(f"Friend {user2_id} removed from user {user1_id}.")

        elif choice == "4":
            user_id = input("Enter user ID to remove: ")
            network.remove_user(user_id)
            print(f"User {user_id} removed.")

        elif choice == "5":
            vz.visualize_network(network)
        
        elif choice == "6": #print("exit")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    menu()
