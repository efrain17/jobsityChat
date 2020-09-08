"""This module manage auth controller"""
import boto3


def authenticate(event):
    """Get policy auth"""
    access_token = event['queryStringParameters']['Authorizer']
    client = boto3.client('cognito-idp')
    try:
        client.get_user(AccessToken=access_token)
    except Exception as exception:
        if 'NotAuthorizedException' in str(exception)[19:41]:
            return get_policy(event, 'Deny')
        raise exception
    return get_policy(event, 'Allow')


def get_policy(event, effect):
    """Response allow"""
    return {
        'principalId': 'user',
        'policyDocument': {
            'Version': '2012-10-17',
            'Statement': [
                {
                    'Action': 'execute-api:Invoke',
                    'Effect': effect,
                    'Resource': event['methodArn']
                }
            ]
        }
    }
