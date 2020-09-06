"""This module manage conection controller"""
from libraries import hooks
from models import conection as conection_mdl


def insert_conection(event):
    """Insert conection id"""
    connection_id = event['requestContext']['connectionId']
    new_conection = {
        'connectionId': event['requestContext']['connectionId'], 
        'chatRoom': 'chatRoom1',
        'userEmail': hooks.SESSION['email']
    }
    conection_mdl.insert(new_conection)


def delete_conection(event):
    """delete conection id"""
    connection_id = event['requestContext']['connectionId']
    conection_mdl.delete(connection_id)
