"""This module manage connection model"""
from jobsitychat.libraries import hooks


def insert(connection):
    """Insert a new connection"""
    hooks.DMTABLE.put_item(
        Item={
            'PK': 'connection',
            'SK': connection['connectionId'],
            'TP': connection['chatRoom'],
            'connectionId': connection['connectionId'],
            'userName': connection['userName']
        }
    )


def get(connection_id):
    """Delete connection by id"""
    response = hooks.DMTABLE.get_item(
        Key={
            'PK': 'connection',
            'SK': connection_id
        },
        AttributesToGet=[
            'PK',
            'SK',
            'TP',
            'connectionId',
            'userName'
        ]
    )
    try:
        return response['Item']
    except KeyError:
        return {}



def delete(connection_id):
    """Delete connection by id"""
    hooks.DMTABLE.delete_item(
        Key={
            'PK': 'connection',
            'SK': connection_id
        }
    )


def get_all():
    """Get all connections"""
    response = hooks.DMTABLE.query(
        Select='SPECIFIC_ATTRIBUTES',
        ProjectionExpression='PK, SK, TP, connectionId, userName',
        KeyConditionExpression='PK = :partition',
        ExpressionAttributeValues={
            ':partition': 'connection'
        }
    )
    return response['Items']
