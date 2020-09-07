"""This module manage message route"""
from jobsitychat.controllers import auth as auth_ctr


def authenticate(event, unused_context):
    """Get authentication"""
    return auth_ctr.authenticate(event)
