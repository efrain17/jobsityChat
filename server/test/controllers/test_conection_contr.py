"""This module test conection controller"""
# pylint: disable=E1101
from controllers import conection


def test_insert_conection(mocker):
    """Sould insert a conection"""
    mocker.patch.object(conection.conection_mdl, 'insert')
    event = {
        'requestContext': {
            'connectionId': 123
        }
    }
    conection.insert_conection(event)
    # asserts
    conection.conection_mdl.insert.assert_called_with(
        {
            'connectionId': 123,
            'chatRoom': 'chatRoom1',
            'userEmail': 'test@testing.com'
        }
    )


def test_delete_conection(mocker):
    """Sould delete a conection"""
    mocker.patch.object(conection.conection_mdl, 'delete')
    event = {
        'requestContext': {
            'connectionId': 123
        }
    }
    conection.delete_conection(event)
    # asserts
    conection.conection_mdl.delete.assert_called_with(123)
