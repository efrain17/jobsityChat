"""This module test message controller"""
# pylint: disable=E1101
import json
from jobsitychat.controllers import message


class MockClient():
    """Mock for Client"""

    @staticmethod
    def post_to_connection(**params):
        """Mock function"""
        return params

    @staticmethod
    def invoke(**params):
        """Mock invoke"""
        return params


def test_insert_message(mocker):
    """Sould insert a message"""
    mocker.patch.object(message.message_mdl, 'insert')
    mocker.patch.object(message.utilities, 'now')
    message.utilities.now.return_value = {
        'timestamp': 1607774522.645,
        'datatime': '2020-09-05 17:30:30'
    }
    new_message = 'hi!! this is a message'
    message.insert_message(new_message, 'userName')
    # asserts
    message.message_mdl.insert.assert_called_with(
        {
            'timestamp': '1607774522.645',
            'userName': 'userName',
            'chatRoom': 'chatRoom1',
            'datatime': '2020-09-05 17:30:30',
            'message': 'hi!! this is a message'
        }
    )


def test_send_to_everyone(mocker):
    """Should send a message to everyone"""
    mocker.patch.object(message.connection_mdl, 'get_all')
    mocker.patch.object(message.boto3, 'client')
    mocker.spy(MockClient, 'post_to_connection')
    message.boto3.client.return_value = MockClient
    message.connection_mdl.get_all.return_value = [
        {
            'connectionId': 123
        }
    ]
    event = {
        'requestContext': {
            'domainName': 'domain',
            'stage': 'dev'
        }
    }
    message.send_to_everyone(event, 'message', 'userName')
    # asserts
    message.connection_mdl.get_all.assert_called_with()
    message.boto3.client.assert_called_with(
        'apigatewaymanagementapi',
        endpoint_url='https://domain/dev'
    )
    MockClient.post_to_connection.assert_called_with(
        Data='{"message": "message", "userName": "userName"}',
        ConnectionId=123
    )


def test_post_message(mocker):
    """Should post message"""
    mocker.patch.object(message, 'insert_message')
    mocker.patch.object(message, 'send_to_everyone')
    mocker.patch.object(message.connection_mdl, 'get')
    message.connection_mdl.get.return_value = {
        'userName': 'userName'
    }
    event = {
        'requestContext': {
            'connectionId': 'connectionId'
        },
        'body': '{"message": "message"}'
    }
    message.post_message(event)
    # asserts
    message.insert_message.assert_called_with('message', 'userName')
    message.send_to_everyone.assert_called_with(event, 'message', 'userName')
    message.connection_mdl.get.assert_called_with('connectionId')


def test_post_message_stock(mocker):
    """Should post message stock"""
    mocker.patch.object(message, 'insert_message')
    mocker.patch.object(message, 'send_to_everyone')
    mocker.patch.object(message.boto3, 'client')
    mocker.spy(MockClient, 'invoke')
    message.boto3.client.return_value = MockClient
    event = {
        'requestContext': {
            'stage': 'dev'
        },
        'body': '{"message": "/stock=appl.us"}'
    }
    payload = {
        'requestContext': {
            'stage': 'dev'
        },
        'body': '{"message": "/stock=appl.us"}'
    }
    message.post_message(event)
    # asserts
    message.insert_message.assert_not_called()
    message.send_to_everyone.assert_not_called()
    MockClient.invoke.assert_called_with(
        FunctionName='jobsityChat-dev-postMessageStock',
        InvocationType='Event',
        Payload=json.dumps(payload)
    )


def test_post_message_send_last_messages(mocker):
    """Should post message stock"""
    mocker.patch.object(message, 'insert_message')
    mocker.patch.object(message, 'send_to_everyone')
    mocker.patch.object(message.boto3, 'client')
    mocker.patch.object(message, 'send_last_messages')
    mocker.spy(MockClient, 'invoke')
    message.boto3.client.return_value = MockClient
    event = {
        'requestContext': {
            'stage': 'dev',
            'connectionId': 'connectionId'
        },
        'body': '{"action": "sendLastMessages"}'
    }
    message.post_message(event)
    # asserts
    message.insert_message.assert_not_called()
    message.send_to_everyone.assert_not_called()
    message.boto3.client.assert_not_called()
    message.send_last_messages.assert_called_with(event, 'connectionId')



def test_send_last_messages(mocker):
    """should send last 50 messages"""
    mocker.patch.object(message.message_mdl, 'get_all_last')
    mocker.patch.object(message.boto3, 'client')
    mocker.spy(MockClient, 'post_to_connection')
    message.boto3.client.return_value = MockClient
    message.message_mdl.get_all_last.return_value = [
        {
            'message': 'message',
            'userName': 'testName'
        }
    ]
    event = {
        'requestContext': {
            'domainName': 'domain',
            'stage': 'dev'
        }
    }
    message.send_last_messages(event, 'connectionId')
    # asserts
    message.message_mdl.get_all_last.assert_called_with()
    MockClient.post_to_connection.assert_called_with(
        Data='{"message": "message", "userName": "testName"}',
        ConnectionId='connectionId'
    )
