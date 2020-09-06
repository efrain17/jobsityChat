"""This module manager the auth routes"""
# pylint: disable=E1101
import mock


def mock_session_committer_auth(func):
    """Mock sessionn committer"""
    def wrapper(*args, **kwargs):
        """run wrapper"""
        return func(*args, **kwargs)
    return wrapper

with mock.patch('jobsitychat.libraries.hooks.session_committer', mock_session_committer_auth):
    from jobsitychat.routes import auth


def test_post_message(mocker):
    """Should response policy"""
    mocker.patch.object(auth.auth_ctr, 'authenticate')
    auth.auth_ctr.authenticate.return_value = 'policy'
    response = auth.authenticate('event', 'context')
    auth.auth_ctr.authenticate.assert_called_with('event')
    assert response == 'policy'
