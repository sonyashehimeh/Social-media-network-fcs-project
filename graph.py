class Graph:
    def __init__(self):
       
        self.adjacency_list = {} # created empty lisyt

    def add_user(self, user): #adding user 
        if user.user_id not in self.adjacency_list:
            self.adjacency_list[user.user_id] = []

    def remove_user(self, user_id): #removint user 
        if user_id in self.adjacency_list:
            del self.adjacency_list[user_id]
            for friends in self.adjacency_list.values():
                if user_id in friends:
                    friends.remove(user_id)

    def add_frnds(self, user1_id, user2_id):
        if user1_id in self.adjacency_list and user2_id in self.adjacency_list:
            self.adjacency_list[user1_id].append(user2_id) # user2 added to frnds of user1
            self.adjacency_list[user2_id].append(user1_id)  #same here

    def remove_frnds(self, user1_id, user2_id):
        if user1_id in self.adjacency_list and user2_id in self.adjacency_list:
            if user2_id in self.adjacency_list[user1_id]: #removing frnds
                self.adjacency_list[user1_id].remove(user2_id)
            if user1_id in self.adjacency_list[user2_id]:
                self.adjacency_list[user2_id].remove(user1_id)

    def bfs(self, start_user_id):
        visited = set()
        queue = [start_user_id]
        traversal = []

        while queue:
            user_id = queue.pop(0)
            if user_id not in visited:
                visited.add(user_id)
                
                traversal.append(user_id)
                queue.extend(self.adjacency_list[user_id])
        
        return traversal

    def dfs(self, start_user_id):
        visited = set()
        
        stack = [start_user_id]
        traversal = []

        while stack:
            user_id = stack.pop()
            if user_id not in visited:
                visited.add(user_id)
                traversal.append(user_id)
                stack.extend(self.adjacency_list[user_id])
        
        return traversal

    def dijkstra_algo(self, start_user_id, end_user_id):
        
        distances = {user: float('inf') for user in self.adjacency_list}
        
        
        distances[start_user_id] = 0
        priority_queue = [(0, start_user_id)]
        
        while priority_queue:
            current_distance, current_user = heapq.heappop(priority_queue)
    
            
            for neighbor in self.adjacency_list[current_user]:
                distance = current_distance + 1  # Assuming unweighted graph
               
               
                if distance < distances[neighbor]:
                    
                    distances[neighbor] = distance
                    heapq.heappush(priority_queue, (distance, neighbor))
        
        return distances[end_user_id]

    def connected_elements(self):
        visited = set()
        elements = []

        for user in self.adjacency_list:
            if user not in visited:
                element = self.dfs(user)
                visited.update(element)
                elements.append(element)
        
        return elements
