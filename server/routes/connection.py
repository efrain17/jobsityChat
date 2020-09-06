"""This module manage connection route"""
from libraries import hooks
from controllers import connection as connection_ctr


@hooks.session_committer
def insert_connection(event, unused_context):
    """Insert new connection"""
    connection_ctr.insert_connection(event)
    return 'success'


@hooks.session_committer
def delete_connection(event, unused_context):
    """Insert new connection"""
    connection_ctr.delete_connection(event)
    return 'success'
