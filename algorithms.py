from collections import deque

def Breadth_First_Search(graph, start_user_id):
    visited = set()
    queue = deque([start_user_id])
    while queue:
        user_id = queue.popleft()
        if user_id not in visited:
            visited.add(user_id)
            queue.extend(user for user in graph.users[user_id].friends if user.user_id not in visited)
    return visited

def dfs(graph, start_user_id, visited=None):
    if visited is None:
        visited = set()
    visited.add(start_user_id)
    for friend in graph.users[start_user_id].friends:
        if friend.user_id not in visited:
            dfs(graph, friend.user_id, visited)
    return visited

def Dijkstra(graph, start_user_id, end_user_id):
    from collections import deque
    distances = {user_id: float('inf') for user_id in graph.users}
    distances[start_user_id] = 0
    queue = deque([start_user_id])
    while queue:
        user_id = queue.popleft()
        for friend in graph.users[user_id].friends:
            if distances[friend.user_id] == float('inf'):
                distances[friend.user_id] = distances[user_id] + 1
                queue.append(friend.user_id)
    return distances[end_user_id]
