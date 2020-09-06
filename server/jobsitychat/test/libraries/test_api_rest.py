"""This module test role_manager rest library"""
# pylint: disable=E1101
from jobsitychat.libraries import api_rest


def test_rest_response():
    """Should get response 200"""
    response = api_rest.rest_response({'test': 'hello', 'test2': None})
    expected = {
        'statusCode': 200,
        'body': '{"response": {"test": "hello", "test2": null}}',
        'headers': {'Content-Type': 'application/json'}
    }
    assert response == expected


def test_response_error():
    """Should get response 200"""
    reponse_data = {
        'message': 'hello',
        'code': 422,
        'data': [{'test': 'hello', 'test1': None}]
    }
    response = api_rest.response_error(reponse_data)
    expected = {
        'statusCode': 422,
        'body': '{"message": "hello", "data": [{"test": "hello", "test1": null}]}',
        'headers': {'Content-Type': 'application/json'}
    }
    assert response == expected
