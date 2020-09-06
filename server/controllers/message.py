"""This module manage message controller"""
from libraries import utilities
from libraries import hooks
from models import message as message_mdl


def insert(message):
    """Insert a new message"""
    now = utilities.now()
    new_message = {
        'timestamp': str(now['timestamp']),
        'userEmail': hooks.SESSION['email'],
        'chatRoom': 'chatRoom1',
        'datatime': now['datatime'],
        'message': message
    }
    message_mdl.insert(new_message)
