from datetime import datetime
class User(object):
    def __init__(self, first_name, last_name, email):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.posts = []
        self.following = []

    def add_post(self, post):
        post.user = self
        self.posts.append(post)

    def get_timeline(self):
        timeline = []
        for user in self.following:
            timeline.extend(user.posts)
        return sorted(timeline, key=lambda post: post.created_at, reverse=True)

    def follow(self, other):
        self.following.append(other)
        
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
