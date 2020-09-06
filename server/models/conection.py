"""This module manage conection model"""
from libraries import hooks


def insert(conection):
    """Insert a new conection"""
    hooks.DMTABLE.put_item(
        Item={
            'PK': 'conection',
            'SK': conection['connectionId'],
            'TP': conection['chatRoom'],
            'connectionId': conection['connectionId'],
            'userEmail': conection['userEmail']
        }
    )


def delete(conection_id):
    """Delete conection by id"""
    hooks.DMTABLE.delete_item(
        Key={
            'PK': 'conection',
            'SK': conection_id
        }
    )


def get_all():
    """Get all conections"""
    response = hooks.DMTABLE.query(
        Select='SPECIFIC_ATTRIBUTES',
        ProjectionExpression='PK, SK, TP, connectionId, userEmail',
        KeyConditionExpression='PK = :partition',
        ExpressionAttributeValues={
            ':partition': 'conection'
        }
    )
    return response['Items']
