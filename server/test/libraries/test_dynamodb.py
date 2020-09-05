"""This module test dynamodb conection"""
# pylint: disable=E1101
from libraries import dynamodb


def test_get_client(mocker):
    """should have the connection"""
    mocker.patch.object(dynamodb, 'boto3')
    dynamodb.boto3.client.return_value = 'dynamodb client'
    client = dynamodb.get_client('localhost', 'http://localhost:8000')
    dynamodb.boto3.client.assert_called_with(
        'dynamodb',
        region_name='us-west-2',
        endpoint_url='http://localhost:8000'
    )
    assert client == 'dynamodb client'


def test_get_client_none(mocker):
    """should have the connection"""
    mocker.patch.object(dynamodb, 'boto3')
    dynamodb.boto3.client.return_value = 'dynamodb client'
    client = dynamodb.get_client('dev', 'http://localhost:8000')
    dynamodb.boto3.client.assert_called_with(
        'dynamodb',
        region_name='us-west-2',
        endpoint_url=None
    )
    assert client == 'dynamodb client'


def test_get_resource(mocker):
    """should have the resourse"""
    mocker.patch.object(dynamodb, 'boto3')
    dynamodb.boto3.resource.return_value = 'dynamodb resource'
    resource = dynamodb.get_resource('localhost', 'http://localhost:8000')
    dynamodb.boto3.resource.assert_called_with(
        'dynamodb',
        region_name='us-west-2',
        endpoint_url='http://localhost:8000'
    )
    assert resource == 'dynamodb resource'


def test_get_resource_none(mocker):
    """should have the resourse"""
    mocker.patch.object(dynamodb, 'boto3')
    dynamodb.boto3.resource.return_value = 'dynamodb resource'
    resource = dynamodb.get_resource('dev', 'http://localhost:8000')
    dynamodb.boto3.resource.assert_called_with(
        'dynamodb',
        region_name='us-west-2',
        endpoint_url=None
    )
    assert resource == 'dynamodb resource'


def test_get_table(mocker):
    """Should get table"""
    params = {
        'enviroment': 'localhost',
        'table': 'JobsityChatTest',
        'dynamodb_dns': 'http://localhost:8000'
    }
    mocker.patch.object(dynamodb, 'get_resource')
    mocker.spy(MockTable, 'Table')
    dynamodb.get_resource.return_value = MockTable
    table = dynamodb.get_table(params)
    # assert
    assert table.table_name == 'JobsityChatTest'
    MockTable.Table.assert_called_with('JobsityChatTest')
    dynamodb.get_resource.assert_called_with('localhost', 'http://localhost:8000')


class MockTable:
    """Mock for MockTable"""

    class Table:
        """Mock for table"""

        def __init__(self, table_name):
            """Mocks for init"""
            self.table_name = table_name
