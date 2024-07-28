class User:
    def __init__(self, user_id, name):
        self.user_id = user_id
        self.name = name
        self.friends = set()
    
    def add_friend(self, friend):
        if isinstance(friend, User):
            self.friends.add(friend)
            friend.friends.add(self)

    def remove_friend(self, friend):
        if isinstance(friend, User):
            self.friends.discard(friend)
            friend.friends.discard(self)
    
  