"""This module manage connection controller"""
import json
import boto3
from jobsitychat.models import connection as connection_mdl
from jobsitychat.models import message as message_mdl


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
    send_last_mesages(event, connection_id)


def delete_connection(event):
    """delete connection id"""
    connection_id = event['requestContext']['connectionId']
    connection_mdl.delete(connection_id)


def send_last_mesages(event, connection_id):
    """Send last 50 messages"""
    messages = message_mdl.get_all_last()
    domain = event['requestContext']['domainName']
    stage = event['requestContext']['stage']
    endpoint_url = f'https://{domain}/{stage}'
    api_gateway = boto3.client(
        'apigatewaymanagementapi', 
        endpoint_url=endpoint_url
    )
    for message in messages:
        message_data = {
            'message': message['message'],
            'userName': message['userName']
        }
        api_gateway.post_to_connection(
            Data=json.dumps(message_data),
            ConnectionId=connection_id
        )
