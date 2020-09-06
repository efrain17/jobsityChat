"""This module control the hooks, connections and session variables"""
# pylint: disable=C0103, W0603
import os
from jobsitychat.libraries import dynamodb
from jobsitychat.libraries.api_rest import response_error
from jobsitychat.libraries.exceptions import ValidationError


DMTABLE = None
SESSION = None


def session_committer(func):
    """Start conections and close after run function"""
    def wrapper(event, context):
        try:
            connect_dynamodb()
            set_session(event)
            return func(event, context)
        except ValidationError as custom_exception:
            return response_error(str(custom_exception))
    return wrapper


def connect_dynamodb():
    """Client instance for dynamodb table"""
    global DMTABLE
    DMTABLE = dynamodb.get_table(os.environ)


def set_session(unused_event):
    """Set variable session"""
    global SESSION
    SESSION = {
        'user': '1',
        'email': 'test@testing.com'
    }
