"""This module manage message controller"""
import json
import boto3
from jobsitychat.libraries import utilities
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
    body = json.loads(event['body'])
    message = body.get('message', '')
    task = body.get('task', None)
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
    elif task == 'sendLastMessages':
        connection_id = event['requestContext']['connectionId']
        send_last_messages(event, connection_id)
    else:
        connection = connection_mdl.get(event['requestContext']['connectionId'])
        insert_message(message, connection['userName'])
        send_to_everyone(event, message, connection['userName'])


def send_last_messages(event, connection_id):
    """Send last 50 messages"""
    messages = message_mdl.get_all_last()
    messages = sorted(messages, key=lambda k: float(k['SK']))
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
