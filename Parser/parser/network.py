"""Making requests to server."""

import requests
from user import User

# base url to users data
users_url = 'https://jsonplaceholder.typicode.com/users'


def get_ids_by(emails):
    """Make request to server to find user ids by their emails.

    Args:
        emails: list of emails

    Returns:
        list of user ids
    """
    users_json = requests.get(users_url).json()
    return [
        user['id']
        for user in users_json
        if user['email'] in emails
    ]


def download_user_by(user_id, email):
    """Make request to server to get user data.

    Args:
        user_id: int
        email: str

    Returns:
        user with all desirable data
    """
    posts_url = '{0}/{1}/posts'.format(users_url, user_id)
    albums_url = '{0}/{1}/albums'.format(users_url, user_id)
    todos_url = '{0}/{1}/todos'.format(users_url, user_id)

    return User(
        user_id,
        email,
        requests.get(posts_url).json(),
        requests.get(albums_url).json(),
        requests.get(todos_url).json(),
    )
