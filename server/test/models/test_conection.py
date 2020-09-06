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
