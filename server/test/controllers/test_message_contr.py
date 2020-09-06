"""This module test message controller"""
# pylint: disable=E1101
from controllers import message


class MockClient():
    """Mock for Client"""

    def post_to_connection(**params):
        """Mock function"""
        return True


def test_insert_message(mocker):
    """Sould insert a message"""
    mocker.patch.object(message.message_mdl, 'insert')
    mocker.patch.object(message.utilities, 'now')
    message.utilities.now.return_value = {
        'timestamp': 1607774522.645,
        'datatime': '2020-09-05 17:30:30'
    }
    new_message = 'hi! this is a message'
    message.insert_message(new_message)
    # asserts
    message.message_mdl.insert.assert_called_with(
        {
            'timestamp': '1607774522.645',
            'userEmail': 'test@testing.com',
            'chatRoom': 'chatRoom1',
            'datatime': '2020-09-05 17:30:30',
            'message': 'hi! this is a message'
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
    message.send_to_everyone(event, 'message')
    # asserts
    message.connection_mdl.get_all.assert_called_with()
    message.boto3.client.assert_called_with(
        'apigatewaymanagementapi',
        endpoint_url='https://domain/dev'
    )
    MockClient.post_to_connection.assert_called_with(
        Data='message',
        ConnectionId=123
    )


def test_post_message(mocker):
    """Should post message"""
    mocker.patch.object(message, 'insert_message')
    mocker.patch.object(message, 'send_to_everyone')
    event = {
        'requestContext': 'requestContext',
        'body': 'message'
    }
    message.post_message(event)
    # asserts
    message.insert_message.assert_called_with('message')
    message.send_to_everyone.assert_called_with(event, 'message')
