"""This module test hooks"""
# pylint: disable=E1101
from libraries import hooks
from libraries.exceptions import ValidationError


class MockCallback:
    """Mock for wrapper"""

    @staticmethod
    def callback(unused_event, unused_context):
        """Mocker for callback"""
        return 'function'

    @staticmethod
    def callback_except(unused_event, unused_context):
        """Mocker for callback_except"""
        raise ValidationError(
            message='my exception',
            data=[ {'error': 'data_error'} ]
        )


def test_session_committer(mocker):
    """Should run session commiter"""
    mocker.patch.object(hooks, 'connect_dynamodb')
    mocker.patch.object(hooks, 'set_session')
    mocker.spy(MockCallback, 'callback')
    event = {
        'requestContext': {
            'authorizer': {
                'user': '1'
            }
        },
        'stageVariables': {
            'enviroment': 'localhost',
            'table': 'dynamodb_table'
        }
    }
    wrapper = hooks.session_committer(MockCallback.callback)
    response = wrapper(event, 'context')
    # assert
    MockCallback.callback.assert_called_with(event, 'context')
    hooks.connect_dynamodb.assert_called_with()
    hooks.set_session.assert_called_with(event)
    assert isinstance(response, type('function'))


def test_session_committer_exception(mocker):
    """Should run session commiter"""
    mocker.patch.object(hooks, 'connect_dynamodb')
    mocker.patch.object(hooks, 'set_session')
    mocker.patch.object(hooks, 'response_error')
    mocker.spy(MockCallback, 'callback_except')
    hooks.response_error.return_value = 'response error'
    event = {
        'requestContext': {
            'authorizer': {
                'user': '1'
            }
        },
        'stageVariables': {
            'enviroment': 'localhost',
            'table': 'dynamodb_table'
        }
    }
    wrapper = hooks.session_committer(MockCallback.callback_except)
    response = wrapper(event, 'context')
    # assert
    MockCallback.callback_except.assert_called_with(event, 'context')
    hooks.connect_dynamodb.assert_called_with()
    hooks.set_session.assert_called_with(event)
    assert response == 'response error'


def test_connect_dynamodb(mocker):
    """Should set DMTABLE"""
    mocker.patch.object(hooks, 'DMTABLE')
    mocker.patch.object(hooks.dynamodb, 'get_table')
    mocker.patch.object(hooks.os, 'environ')
    hooks.dynamodb.get_table.return_value = 'dynamodb_table'
    hooks.os.environ = {
        'enviroment': 'localhost',
        'table': 'dynamodb_table'
    }
    hooks.connect_dynamodb()
    # asserts
    assert hooks.DMTABLE == 'dynamodb_table'
    hooks.dynamodb.get_table.assert_called_with(
        {
            'enviroment': 'localhost',
            'table': 'dynamodb_table'
        }
    )


def test_set_session(mocker):
    """Should set SESSION"""
    mocker.patch.object(hooks, 'SESSION')
    event = {
        'requestContext': {
            'authorizer': {
                'user': '1',
                'email': 'test@testing.com'
            }
        },
    }
    hooks.set_session(event)
    # asserts
    expected_session = {
        'user': '1',
        'email': 'test@testing.com'
    }
    assert hooks.SESSION == expected_session
