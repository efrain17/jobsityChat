"""This module manage message model"""
from libraries import hooks


def insert(message):
    """Insert a new message"""
    hooks.DMTABLE.put_item(
        Item={
            'PK': message['timestamp'],
            'SK': message['userEmail'],
            'TP': message['chatRoom'],
            'datatime': message['datatime'],
            'message': message['message']
        }
    )
