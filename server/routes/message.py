"""This module manage message route"""
from libraries import hooks
from controllers import message as message_ctr


@hooks.session_committer
def post_message(event, unused_context):
    """Post new message"""
    message_ctr.post_message(event)
    return 'success'
