"""This module is dynamodb client"""
import boto3


def get_client(enviroment, dynamodb_dns):
    """Get client boto3"""
    endpoint_url = dynamodb_dns if (enviroment == 'localhost') else None
    return boto3.client(
        'dynamodb',
        region_name='us-west-2',
        endpoint_url=endpoint_url
    )


def get_resource(enviroment, dynamodb_dns):
    """Get resource table"""
    endpoint_url = dynamodb_dns if (enviroment == 'localhost') else None
    return boto3.resource(
        'dynamodb',
        region_name='us-west-2',
        endpoint_url=endpoint_url
    )


def get_autorizer_table(params):
    """Get authorizer table boto3"""
    resource = get_resource(params['enviroment'], params['dynamodb_dns'])
    return resource.Table(params['authorizer_table'])
