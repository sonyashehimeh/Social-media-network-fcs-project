class User:
    def __init__(self, user_id, name):
        self.user_id = user_id
        self.name = name
        self.friends = []
        
    def add_friend(self, friend_id):
        if friend_id not in self.friends:
            self.friends.append(friend_id)

    def remove_friend(self, friend_id):
        if friend_id in self.friends:
            self.friends.remove(friend_id)
