"""This module manager the stock routes"""
# pylint: disable=E1101
import mock


def mock_session_committer(func):
    """Mock sessionn committer"""
    def wrapper(*args, **kwargs):
        """run wrapper"""
        return func(*args, **kwargs)
    return wrapper

with mock.patch('libraries.hooks.session_committer', mock_session_committer):
    from routes import stock


def test_post_message(mocker):
    """Should response success"""
    mocker.patch.object(stock.stock_ctr, 'send_stock')
    response = stock.post_message('event', 'context')
    stock.stock_ctr.send_stock.assert_called_with('event')
    assert response == {}
