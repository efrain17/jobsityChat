"""This module manager the conection routes"""
# pylint: disable=E1101
import mock


def mock_session_committer(func):
    """Mock sessionn committer"""
    def wrapper(*args, **kwargs):
        """run wrapper"""
        return func(*args, **kwargs)
    return wrapper

with mock.patch('libraries.hooks.session_committer', mock_session_committer):
    from routes import conection


def test_insert_conection(mocker):
    """Should response success"""
    mocker.patch.object(conection.conection_ctr, 'insert_conection')
    response = conection.insert_conection('event', 'context')
    conection.conection_ctr.insert_conection.assert_called_with('event')
    assert response == 'success'


def test_delete_conection(mocker):
    """Should response success"""
    mocker.patch.object(conection.conection_ctr, 'delete_conection')
    response = conection.delete_conection('event', 'context')
    conection.conection_ctr.delete_conection.assert_called_with('event')
    assert response == 'success'
