class User:

    def __init__(self, username, name, email):
        self.username = username
        self.name = name
        self.email = email

    def introduce_yourself(self, guest_name):
        print("Hi {}, I'm {}! Contact me at {} .".format(guest_name, self.name, self.email))

    def __repr__(self):
        return "User(username='{}', name='{}', email='{}')".format(self.username, self.name, self.email)
    
    def __str__(self):
        return self.__repr__()


anurag = User('Anurag', 'Timilsina', 'anurag@email.com')
parasar = User('Parasar', 'Bikram KC', 'parasar@email.com')
nikolson = User('Nikolson', 'Chauhan', 'nikolson@email.com')
saugat = User('Saugat', 'KC', 'saugat@email.com')

users = [anurag, parasar, nikolson, saugat]


class UserDatabase:
    def __init__(self):
        self.users = []

    def insert(self, user):
        i = 0
        while i < len(self.users):
            if self.users[i].username > user.username:
                break
            i += 1

        self.users.insert(i, user)

    def find(self, username):
        for user in self.users:
            if user.username == username:
                return user

    def update(self, user):
        target = self.find(user.username)
        target.name, target.email = user.name, user.email

    def list_all(self):
        return self.users


database = UserDatabase()

database.insert(anurag)
database.insert(parasar)
database.insert(nikolson)
database.insert(saugat)

user = database.find('Nikolson')
print(user)

database.update(User(username='Anurag', name='Anurag Timilsina', email='anurag.timilsina@gmail.com'))
user = database.find('Anurag')
print(user)

database.list_all()

ben = User('Ben', 'Tenison', 'ben@plummer.com')

database.insert(ben)
print(database.list_all())

'''
    Thus, the time complexities of the various operations are:

        Insert: O(N)
        Find: O(N)
        Update: O(N)
        List: O(1)
'''

# import jovian
# jovian.commit(project='python-binary-search_trees')
