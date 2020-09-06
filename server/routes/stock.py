"""This module manage stock route"""
from libraries import hooks
from controllers import stock as stock_ctr


@hooks.session_committer
def post_message(event, unused_context):
    """Post new message"""
    stock_ctr.send_stock(event)
    return {}
