"""This module manage message controller"""
import boto3
from libraries import utilities
from libraries import hooks
from models import message as message_mdl
from models import connection as connection_mdl


def insert(message):
    """Insert a new message"""
    now = utilities.now()
    new_message = {
        'timestamp': str(now['timestamp']),
        'userEmail': hooks.SESSION['email'],
        'chatRoom': 'chatRoom1',
        'datatime': now['datatime'],
        'message': message
    }
    message_mdl.insert(new_message)


def send_to_everyone(event, message):
    """Send a message to everyone"""
    connections = connection_mdl.get_all()
    domain = event['requestContext']['domainName']
    stage = event['requestContext']['stage']
    endpoint_url = f'https://{domain}/{stage}'
    api_gateway = boto3.client('apigatewaymanagementapi', endpoint_url=endpoint_url)
    for _connection in connections:
        api_gateway.post_to_connection(
            Data=message,
            ConnectionId=_connection['connectionId']
        )
