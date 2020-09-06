"""This module manager the message routes"""
# pylint: disable=E1101
import mock


def mock_session_committer_message(func):
    """Mock sessionn committer"""
    def wrapper(*args, **kwargs):
        """run wrapper"""
        return func(*args, **kwargs)
    return wrapper

with mock.patch('jobsitychat.libraries.hooks.session_committer', mock_session_committer_message):
    from jobsitychat.routes import message


def test_post_message(mocker):
    """Should response success"""
    mocker.patch.object(message.message_ctr, 'post_message')
    response = message.post_message('event', 'context')
    message.message_ctr.post_message.assert_called_with('event')
    assert response == {}
