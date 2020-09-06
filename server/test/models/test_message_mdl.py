"""This module test message model"""
from models import message


def test_insert_message(mocker):
    """Sould insert a message"""
    mocker.spy(message.hooks.DMTABLE, 'put_item')
    new_message = {
        'timestamp': '1607774522.665',
        'userEmail': 'test@testing.com',
        'chatRoom': 'chatRoom1',
        'datatime': '2020-09-05 17:30:30',
        'message': 'hi! this is a message'
    }
    message.insert(new_message)
    message.hooks.DMTABLE.put_item.assert_called_with(
        Item={
            'PK': 'message',
            'SK': '1607774522.665',
            'TP': 'chatRoom1',
            'userEmail': 'test@testing.com',
            'datatime': '2020-09-05 17:30:30',
            'message': 'hi! this is a message'
        }
    )
