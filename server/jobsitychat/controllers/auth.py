"""This module manage auth controller"""
import json
import boto3


def authenticate(event):
    """Get policy auth"""
    return get_policy(event, 'Allow', 'session')


def get_policy(event, effect, session):
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
