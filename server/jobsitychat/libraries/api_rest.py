"""This module has rest methods"""
import simplejson as json


def rest_response(reponse_data):
    """Response status 200"""
    data = {
        'response': reponse_data
    }
    return {
        'statusCode': 200,
        'body': json.dumps(data, ignore_nan=True),
        'headers': {'Content-Type': 'application/json'}
    }


def response_error(reponse_data):
    """Response status 200"""
    data = {
        'message': reponse_data['message'],
        'data': reponse_data['data']
    }
    return {
        'statusCode': reponse_data['code'],
        'body': json.dumps(data, ignore_nan=True),
        'headers': {'Content-Type': 'application/json'}
    }
