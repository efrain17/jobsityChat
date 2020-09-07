"""This module manage auth controller"""
import boto3


def authenticate(event):
    """Get policy auth"""
    access_token = event['queryStringParameters']['Authorizer']
    client = boto3.client('cognito-idp')
    response = client.get_user(AccessToken=access_token)
    if response:
        return get_policy(event, 'Allow')
    return get_policy(event, 'Deny')


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
