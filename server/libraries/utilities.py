"""Manage utilities as calculations and time"""
from datetime import datetime


def now():
    """Get timestamp and datatime"""
    time = datetime.now()
    return {
        'timestamp': time.timestamp(),
        'datatime': time.strftime('%Y-%m-%d %H:%M:%S')
    }
