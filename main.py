from graph import Graph
from user import User
import visualization as vz

def menu():
    network = Graph()
    while True:
        print("1. Sign Up") # to create account
        print("2. Add a Friend")
        print("3. Remove a Friend")
        print("4. Remove Account") # to delete users account
        print("5. Network Visualizing ")
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
            userNum1_id = input("Enter your user ID: ")
            userNum2_id = input("Enter a friend's user ID: ")
            network.add_frnds(userNum1_id, userNum2_id)
            print(f"Friend {userNum2_id} added to user {userNum1_id}.")

        elif choice == "3":
            userNum1_id = input("Enter your user ID: ")
            userNum2_id = input("Enter a friend's user ID to remove: ")
            network.remove_frnds(userNum1_id, userNum2_id)
            print(f"Friend {userNum2_id} removed from user {userNum1_id}.")

        elif choice == "4":
            user_id = input("Enter user ID to remove: ")
            network.remove_user(user_id)
            print(f"User {user_id} removed.")

        elif choice == "5":
            vz.visualization_of_network(network)
        
        elif choice == "6": #print("exit")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    menu()
