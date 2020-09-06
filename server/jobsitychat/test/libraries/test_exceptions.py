"""This module test exception library"""
# pylint: disable=E1101
from jobsitychat.libraries.exceptions import ValidationError


def test_custom_excepetion_422():
    """Should get response 422"""
    expected = {
        'message': 'test',
        'code': 422,
        'data': None
    }
    instance_test = ValidationError('test')
    instance = instance_test.__str__()
    assert instance == repr(expected)


def test_custom_excepetion_500():
    """Should get response 500"""
    expected = {
        'message': 'test',
        'code': 500,
        'data': 'data'
    }
    instance_test = ValidationError(message='test', code=500, data='data')
    instance = instance_test.__str__()
    assert instance == repr(expected)
