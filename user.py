class User:
    def __init__(self, user_id, name):
        self.user_id = user_id
        self.name = name
        self.frnds = []
        
    def add_frnd(self, frnd_id):
        if frnd_id not in self.frnds:
            self.frnds.append(frnd_id)

    def remove_frnd(self, frnd_id):
        if frnd_id in self.frnds:
            self.frnds.remove(frnd_id)
