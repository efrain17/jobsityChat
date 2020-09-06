"""This module test connection controller"""
# pylint: disable=E1101
from controllers import connection


def test_insert_connection(mocker):
    """Sould insert a connection"""
    mocker.patch.object(connection.connection_mdl, 'insert')
    event = {
        'requestContext': {
            'connectionId': 123
        }
    }
    connection.insert_connection(event)
    # asserts
    connection.connection_mdl.insert.assert_called_with(
        {
            'connectionId': 123,
            'chatRoom': 'chatRoom1',
            'userEmail': 'test@testing.com'
        }
    )


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
