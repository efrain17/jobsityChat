"""This module manage message model"""
from jobsitychat.libraries import hooks


def insert(message):
    """Insert a new message"""
    hooks.DMTABLE.put_item(
        Item={
            'PK': 'message',
            'SK': message['timestamp'],
            'TP': message['chatRoom'],
            'userEmail': message['userEmail'],
            'datatime': message['datatime'],
            'message': message['message']
        }
    )
