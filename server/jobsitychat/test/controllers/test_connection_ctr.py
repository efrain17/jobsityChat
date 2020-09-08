"""This module test connection controller"""
# pylint: disable=E1101, W0613
from jobsitychat.controllers import connection


class MockClient():
    """Mock for Client"""

    @staticmethod
    def get_user(**params):
        """Mock function"""
        return {
            'Username': 'userTest',
            'UserAttributes': [
                {
                    'Name': 'email',
                    'Value': 'test@mail.com'
                },
                {
                    'Name': 'phone',
                    'Value': '123'
                },
            ],
        }


def test_insert_connection(mocker):
    """Sould insert a connection"""
    mocker.patch.object(connection.connection_mdl, 'insert')
    mocker.patch.object(connection.boto3, 'client')
    mocker.spy(MockClient, 'get_user')
    connection.boto3.client.return_value = MockClient
    event = {
        'requestContext': {
            'connectionId': 123
        },
        'queryStringParameters': {
            'Authorizer': 444
        }
    }
    connection.insert_connection(event)
    # asserts
    connection.connection_mdl.insert.assert_called_with(
        {
            'connectionId': 123,
            'chatRoom': 'chatRoom1',
            'userName': 'test@mail.com'
        }
    )
    connection.boto3.client.assert_called_with('cognito-idp')
    MockClient.get_user.assert_called_with(AccessToken=444)


def test_delete_connection(mocker):
    """Sould delete a connection"""
    mocker.patch.object(connection.connection_mdl, 'delete')
    event = {
        'requestContext': {
            'connectionId': 123
        }
    }
    connection.delete_connection(event)
    # asserts
    connection.connection_mdl.delete.assert_called_with(123)
