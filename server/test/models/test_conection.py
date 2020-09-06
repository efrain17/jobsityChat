"""This module test conection model"""
from models import conection


def test_insert_conection(mocker):
    """Sould insert a conection"""
    mocker.spy(conection.hooks.DMTABLE, 'put_item')
    new_conection = {
        'connectionId': '12345',
        'userEmail': 'test@testing.com',
        'chatRoom': 'chatRoom1'
    }
    conection.insert(new_conection)
    conection.hooks.DMTABLE.put_item.assert_called_with(
        Item={
            'PK': 'conection',
            'SK': '12345',
            'TP': 'chatRoom1',
            'connectionId': '12345',
            'userEmail': 'test@testing.com',
        }
    )


def test_get_all(mocker):
    """Shoult get all conections"""
    mocker.spy(conection.hooks.DMTABLE, 'query')
    expected = {
        'PK': 'conection',
        'SK': '12345',
        'TP': 'chatRoom1',
        'connectionId': '12345',
        'userEmail': 'test@testing.com'
    }
    response = conection.get_all()
    # asserts
    conection.hooks.DMTABLE.query.assert_called_with(
        Select='SPECIFIC_ATTRIBUTES',
        ProjectionExpression='PK, SK, TP, connectionId, userEmail',
        KeyConditionExpression='PK = :partition',
        ExpressionAttributeValues={
            ':partition': 'conection'
        }
    )
    assert response[0] == expected
