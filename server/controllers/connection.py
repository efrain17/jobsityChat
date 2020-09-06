"""This module manage connection controller"""
from libraries import hooks
from models import connection as connection_mdl


def insert_connection(event):
    """Insert connection id"""
    new_connection = {
        'connectionId': event['requestContext']['connectionId'],
        'chatRoom': 'chatRoom1',
        'userEmail': hooks.SESSION['email']
    }
    connection_mdl.insert(new_connection)


def delete_connection(event):
    """delete connection id"""
    connection_id = event['requestContext']['connectionId']
    connection_mdl.delete(connection_id)
