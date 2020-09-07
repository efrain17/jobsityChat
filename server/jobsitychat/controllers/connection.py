"""This module manage connection controller"""
import boto3
from jobsitychat.models import connection as connection_mdl


def insert_connection(event):
    """Insert connection id"""
    access_token = event['queryStringParameters']['Authorizer']
    client = boto3.client('cognito-idp')
    user = client.get_user(AccessToken=access_token)
    connection_id = event['requestContext']['connectionId']
    new_connection = {
        'connectionId': connection_id,
        'chatRoom': 'chatRoom1',
        'userName': user['Username']
    }
    connection_mdl.insert(new_connection)


def delete_connection(event):
    """delete connection id"""
    connection_id = event['requestContext']['connectionId']
    connection_mdl.delete(connection_id)
