"""This module manage message controller"""
import json
import boto3
from jobsitychat.libraries import utilities
from jobsitychat.libraries import hooks
from jobsitychat.models import message as message_mdl
from jobsitychat.models import connection as connection_mdl


def insert_message(message, user_name):
    """Insert a new message"""
    now = utilities.now()
    new_message = {
        'timestamp': str(now['timestamp']),
        'userName': user_name,
        'chatRoom': 'chatRoom1',
        'datatime': now['datatime'],
        'message': message
    }
    message_mdl.insert(new_message)


def send_to_everyone(event, message, user_name):
    """Send a message to everyone"""
    connections = connection_mdl.get_all()
    domain = event['requestContext']['domainName']
    stage = event['requestContext']['stage']
    endpoint_url = f'https://{domain}/{stage}'
    api_gateway = boto3.client('apigatewaymanagementapi', endpoint_url=endpoint_url)
    message_data = {
        'message': message,
        'userName': user_name
    }
    for _connection in connections:
        api_gateway.post_to_connection(
            Data=json.dumps(message_data),
            ConnectionId=_connection['connectionId']
        )


def post_message(event):
    """Controller message"""
    message = json.loads(event['body'])['message']
    if message[0:7] == '/stock=':
        stage = event['requestContext']['stage']
        client = boto3.client('lambda')
        payload = {
            'requestContext': event['requestContext'],
            'body': event['body']
        }
        client.invoke(
            FunctionName=f'jobsityChat-{stage}-postMessageStock',
            InvocationType='Event',
            Payload=json.dumps(payload),
        )
    else:
        connection = connection_mdl.get(event['requestContext']['connectionId'])
        insert_message(message, connection['userName'])
        send_to_everyone(event, message, connection['userName'])
