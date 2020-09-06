"""This module manage connection route"""
from jobsitychat.libraries import hooks
from jobsitychat.controllers import connection as connection_ctr


@hooks.session_committer
def insert_connection(event, unused_context):
    """Insert new connection"""
    connection_ctr.insert_connection(event)
    return {}


@hooks.session_committer
def delete_connection(event, unused_context):
    """Insert new connection"""
    connection_ctr.delete_connection(event)
    return {}
