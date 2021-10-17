"""Models."""


class User(object):
    """User model."""

    def __init__(self, _id, email=None, posts=None, albums=None, todos=None):
        """Init user.

        Args:
            id: int
            email: str
            posts: list of posts by this user
            albums: list of albums by this user
            todos: list of todos by this user
        """
        self.id = _id
        self.email = email
        self.posts = posts
        self.albums = albums
        self.todos = todos

    def get_content(self):
        """Get all content by this user.

        Returns:
            dictionary with all content
        """
        return {
            'posts': self.posts,
            'albums': self.albums,
            'todos': self.todos,
        }
