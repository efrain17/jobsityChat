"""Configuration for testing"""
from libraries import hooks


DMTABLE = 'JobsityChatTest'


def pytest_configure(unused_config):
    """"Initial configuration"""
    event = {
        'stageVariables': {
            'enviroment': 'localhost',
            'table': DMTABLE
        },
        'requestContext': {
            'authorizer': {
                'user': 1,
                'email': 'testdb@testing.com'
            }
        }
    }
    hooks.SESSION = event['requestContext']['authorizer']
    hooks.DMTABLE = hooks.dynamodb.get_table(event['stageVariables'])
