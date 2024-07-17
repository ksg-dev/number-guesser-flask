## Advanced Python Decorator Functions

class User:
    def __init__(self, name):
        self.name = name
        self.is_logged_in = False


def create_blog_post(user):
    print(f"This is {user.name}'s new blog post.")

