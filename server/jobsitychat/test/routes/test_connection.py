"""This module manager the connection routes"""
# pylint: disable=E1101
import mock


def mock_session_committer_connection(func):
    """Mock sessionn committer"""
    def wrapper(*args, **kwargs):
        """run wrapper"""
        return func(*args, **kwargs)
    return wrapper

with mock.patch('jobsitychat.libraries.hooks.session_committer', mock_session_committer_connection):
    from jobsitychat.routes import connection


def test_insert_connection(mocker):
    """Should response success"""
    mocker.patch.object(connection.connection_ctr, 'insert_connection')
    response = connection.insert_connection('event', 'context')
    connection.connection_ctr.insert_connection.assert_called_with('event')
    assert response == {}


def test_delete_connection(mocker):
    """Should response success"""
    mocker.patch.object(connection.connection_ctr, 'delete_connection')
    response = connection.delete_connection('event', 'context')
    connection.connection_ctr.delete_connection.assert_called_with('event')
    assert response == {}
