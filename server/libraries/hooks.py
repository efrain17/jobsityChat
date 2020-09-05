"""This module control the hooks, connections and session variables"""
# pylint: disable=C0103, W0603
from libraries import dynamodb
from libraries.api_rest import response_error
from libraries.exceptions import ValidationError


DMTABLE = None
SESSION = None


def session_committer(func):
    """Start conections and close after run function"""
    def wrapper(event, context):
        try:
            connect_dynamodb(event)
            set_session(event)
            return func(event, context)
        except ValidationError as custom_exception:
            return response_error(str(custom_exception))
    return wrapper


def connect_dynamodb(event):
    """Cliente instance for dynamodb table"""
    global DMTABLE
    DMTABLE = dynamodb.get_table(event['stageVariables'])


def set_session(event):
    """Set variable session"""
    global SESSION
    SESSION = event['requestContext']['authorizer']
