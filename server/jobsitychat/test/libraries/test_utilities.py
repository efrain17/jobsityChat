"""This module test utilities"""
from datetime import datetime
from jobsitychat.libraries import utilities


def test_now():
    """Should get datetime"""
    time = datetime.now()
    expected = {
    	'timestamp': time.timestamp(),
    	'datatime': time.strftime('%Y-%m-%d %H:%M:%S')
    }
    date_time = utilities.now()
    #assert
    assert int(date_time['timestamp']) == int(expected['timestamp'])
    assert date_time['datatime'] == expected['datatime']
    assert isinstance(date_time['timestamp'], float)
