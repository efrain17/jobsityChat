"""This module test message controller"""
# pylint: disable=E1101
from controllers import message


def test_insert_message(mocker):
    """Sould insert a message"""
    mocker.patch.object(message.message_mdl, 'insert')
    mocker.patch.object(message.utilities, 'now')
    message.utilities.now.return_value = {
        'timestamp': 1607774522.645,
        'datatime': '2020-09-05 17:30:30'
    }
    new_message = 'hi! this is a message'
    message.insert(new_message)
    # asserts
    message.message_mdl.insert.assert_called_with(
        {
            'timestamp': '-1607774522.645',
            'userEmail': 'test@testing.com',
            'chatRoom': 'chatRoom1',
            'datatime': '2020-09-05 17:30:30',
            'message': 'hi! this is a message'
        }
    )
