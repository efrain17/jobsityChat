"""Configuration for testing"""
from libraries import hooks


DMTABLE = 'jobsityChatTest'


def pytest_configure(config):
    """"Initial configuration"""
    event = {
        'stageVariables': {
            'enviroment': 'localhost',
            'table': DMTABLE,
            'dynamodb_dns': 'http://localhost:8000'
        },
        'requestContext': {
            'authorizer': {
                'user': 1,
                'email': 'test@testing.com'
            }
        }
    }
    hooks.SESSION = event['requestContext']['authorizer']
    hooks.DMTABLE = hooks.dynamodb.get_table(event['stageVariables'])
