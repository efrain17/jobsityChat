"""This module test connection model"""
from jobsitychat.models import connection


def test_insert_connection(mocker):
    """Sould insert a connection"""
    mocker.spy(connection.hooks.DMTABLE, 'put_item')
    new_connection = {
        'connectionId': '12345',
        'userName': 'testName',
        'chatRoom': 'chatRoom1'
    }
    connection.insert(new_connection)
    connection.hooks.DMTABLE.put_item.assert_called_with(
        Item={
            'PK': 'connection',
            'SK': '12345',
            'TP': 'chatRoom1',
            'connectionId': '12345',
            'userName': 'testName',
        }
    )


def test_delete_connection(mocker):
    """Should delete connection"""
    mocker.spy(connection.hooks.DMTABLE, 'delete_item')
    connection_id = '123456'
    connection.delete(connection_id)
    # asserts
    connection.hooks.DMTABLE.delete_item.assert_called_with(
        Key={
            'PK': 'connection',
            'SK': '123456'
        }
    )


def test_get_connection(mocker):
    """Should get connection"""
    mocker.spy(connection.hooks.DMTABLE, 'get_item')
    connection_id = '12345'
    expected = {
        'PK': 'connection',
        'SK': '12345',
        'TP': 'chatRoom1',
        'connectionId': '12345',
        'userName': 'testName',
    }
    response = connection.get(connection_id)
    # asserts
    connection.hooks.DMTABLE.get_item.assert_called_with(
        Key={
            'PK': 'connection',
            'SK': '12345'
        },
        AttributesToGet=[
            'PK',
            'SK',
            'TP',
            'connectionId',
            'userName'
        ]
    )
    assert response == expected


def test_get_connection_not_found(mocker):
    """Should get empty dictionary"""
    mocker.spy(connection.hooks.DMTABLE, 'get_item')
    connection_id = 'XYZ'
    response = connection.get(connection_id)
    # asserts
    assert response == {}


def test_get_all(mocker):
    """Shoult get all connections"""
    mocker.spy(connection.hooks.DMTABLE, 'query')
    expected = {
        'PK': 'connection',
        'SK': '12345',
        'TP': 'chatRoom1',
        'connectionId': '12345',
        'userName': 'testName'
    }
    partition = 'connection'
    response = connection.get_all()
    # asserts
    connection.hooks.DMTABLE.query.assert_called_with(
        Select='SPECIFIC_ATTRIBUTES',
        ProjectionExpression='PK, SK, TP, connectionId, userName',
        KeyConditionExpression='PK = :partition',
        ExpressionAttributeValues={
            ':partition': partition
        }
    )
    assert response[0] == expected
