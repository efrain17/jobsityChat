"""This module manage message controller"""
import json
import boto3
from libraries import utilities
from libraries import hooks
from models import message as message_mdl
from models import connection as connection_mdl


def insert_message(message):
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

def post_message(event):
    """Controller message"""
    message = json.loads(event['body'])['message']
    if message[0:7] == '/stock=':
        client = boto3.client('lambda')
        payload = {
            'requestContext': event['requestContext'],
            'body': event['body']
        }
        response = client.invoke(
            FunctionName='jobsityChat-dev-postMessageStock',
            InvocationType='Event',
            Payload=json.dumps(payload),
        )
    else:
        insert_message(message)
        send_to_everyone(event, message)
