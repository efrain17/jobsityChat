"""This module test auth controller"""
# pylint: disable=E1101
import pytest
from jobsitychat.controllers import auth


class MockClient():
    """Mock for Client"""

    @staticmethod
    def get_user(**params):
        """Mock function"""
        return params


def test_authenticate_allow(mocker):
    """Should allow"""
    mocker.patch.object(auth, 'get_policy')
    mocker.patch.object(auth.boto3, 'client')
    mocker.spy(MockClient, 'get_user')
    auth.boto3.client.return_value = MockClient
    event = {
        'queryStringParameters': {
            'Authorizer': 1234
        }
    }
    auth.authenticate(event)
    auth.get_policy.assert_called_with(event, 'Allow')
    MockClient.get_user.assert_called_with(AccessToken=1234)
    auth.boto3.client.assert_called_with('cognito-idp')


def test_authenticate_deny(mocker):
    """Should deny"""
    exception = Exception('An error occurred (NotAuthorizedException)')
    mocker.patch.object(auth, 'get_policy')
    mocker.patch.object(auth.boto3, 'client')
    mocker.patch.object(MockClient, 'get_user', side_effect=exception)
    MockClient.get_user.return_value = None
    auth.boto3.client.return_value = MockClient
    event = {
        'queryStringParameters': {
            'Authorizer': 1234
        }
    }
    auth.authenticate(event)
    auth.get_policy.assert_called_with(event, 'Deny')
    MockClient.get_user.assert_called_with(AccessToken=1234)


def test_authenticate_exeption(mocker):
    """Should deny"""
    exception = Exception('exeption')
    mocker.patch.object(auth, 'get_policy')
    mocker.patch.object(auth.boto3, 'client')
    mocker.patch.object(MockClient, 'get_user', side_effect=exception)
    MockClient.get_user.return_value = None
    auth.boto3.client.return_value = MockClient
    event = {
        'queryStringParameters': {
            'Authorizer': 1234
        }
    }
    with pytest.raises(Exception):
        auth.authenticate(event)
    auth.get_policy.assert_not_called()
    MockClient.get_user.assert_called_with(AccessToken=1234)


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
    response = auth.get_policy(event, 'effect')
    assert response == expected_policy
