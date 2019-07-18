class UserModel:
    def __init__(self,name,password,id = None):
        self.id = id
        self.name = name
        self.password = password