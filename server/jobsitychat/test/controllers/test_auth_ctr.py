"""This module test auth controller"""
# pylint: disable=E1101
from jobsitychat.controllers import auth


def test_authenticate(mocker):
    """Should allow"""
    mocker.patch.object(auth, 'get_policy')
    auth.authenticate('event')
    auth.get_policy.assert_called_with('event', 'Allow', 'session')


def test_get_policy():
    """Shoulf get a policy"""
    expected_policy = {
        'principalId': 'user',
        'policyDocument': {
            'Version': '2012-10-17',
            'Statement': [
                {
                    'Action': 'execute-api:Invoke',
                    'Effect': 'effect',
                    'Resource': 'event'
                }
            ]
        }
    }
    event = {'methodArn': 'event'}
    response = auth.get_policy(event, 'effect', 'session')
    assert response == expected_policy
