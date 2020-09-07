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


def get_all_last():
    """Get last 50 messages"""
    response = hooks.DMTABLE.query(
        Select='SPECIFIC_ATTRIBUTES',
        Limit=50,
        ScanIndexForward=False,
        ProjectionExpression='PK, SK, TP, userName, datatime, message',
        KeyConditionExpression='PK = :partition',
        ExpressionAttributeValues={
            ':partition': 'message'
        }
    )
    return response['Items']
