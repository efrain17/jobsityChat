"""This module manage message model"""
from jobsitychat.libraries import hooks


def insert(message):
    """Insert a new message"""
    hooks.DMTABLE.put_item(
        Item={
            'PK': 'message',
            'SK': message['timestamp'],
            'TP': message['chatRoom'],
            'userName': message['userName'],
            'datatime': message['datatime'],
            'message': message['message']
        }
    )
