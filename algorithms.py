import heapq #heap queue algo

class Graph:
    def __init__(self):
        self.adjacency_list = {}

   # for users
    
    def remove_user(self, user_id):
        if user_id in self.adjacency_list:
            del self.adjacency_list[user_id]
            for frnds in self.adjacency_list.values():
                if user_id in frnds:
                    frnds.remove(user_id)\

    def add_user(self, user):
        if user.user_id not in self.adjacency_list:
            self.adjacency_list[user.user_id] = []

    

    #now for frnds

    def remove_frnds(self, userNum1_id, userNum2_id):
        if userNum1_id in self.adjacency_list and userNum2_id in self.adjacency_list:
            if userNum2_id in self.adjacency_list[userNum1_id]:
                self.adjacency_list[userNum1_id].remove(userNum2_id)
            if userNum1_id in self.adjacency_list[userNum2_id]:
                self.adjacency_list[userNum2_id].remove(userNum1_id)

    def add_frnds(self, userNum1_id, userNum2_id):
        if userNum1_id in self.adjacency_list and userNum2_id in self.adjacency_list:
            self.adjacency_list[userNum1_id].append(userNum2_id)
            self.adjacency_list[userNum2_id].append(userNum1_id)

    

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


    def connected_elements(self):
        visited = set()
        #alreadyvisited = []
        elements = []

        for user in self.adjacency_list:
            if user not in visited:
                element = self.dfs(user)
                visited.update(element)
                elements.append(element)
        
        return elements

   def dijkstra_algo(self, start_user_id, end_user_id):
        distances = {user: float('inf') for user in self.adjacency_list}
        distances[start_user_id] = 0
        priority_queue = [(0, start_user_id)]
        
        while priority_queue:
            current_distance, current_user = heapq.heappop(priority_queue)
           
           
            for neighbor in self.adjacency_list[current_user]:
                distance = current_distance + 1  # Assuming if unweighted graph

                if distance < distances[neighbor]:

                    distances[neighbor] = distance
                    heapq.heappush(priority_queue, (distance, neighbor))
        
        return distances[end_user_id]