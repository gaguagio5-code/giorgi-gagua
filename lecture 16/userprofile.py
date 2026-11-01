class User:
    status = "active"
    def __init__(self, username, email, age):
        self.username = username
        self.email = email
        self.age = age
    def get_info(self):
        print(f"Username: {self.username}")
        print(f"Email: {self.email}")
        print(f"Age: {self.age}")

user1 = User("john_doe", "john@example.com", 30)
print(f"User1 Status: {user1.status}")
user2 = User("jane_smith", "jane@example.com", 25)
print(f"User2 Status: {user2.status}")

print("\nUser Information:")
for user in [user1, user2]:
    user.get_info()
    print()
