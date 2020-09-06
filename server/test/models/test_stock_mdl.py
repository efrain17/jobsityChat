"""This module test stock model"""
# pylint: disable=E1101
from models import stock


def test_get_stock(mocker):
    """Sould get a message"""
    mocker.spy(stock.requests, 'get')
    expected_url = 'https://stooq.com/q/l/?s=aapl.us&f=sd2t2ohlcv&h&e=csv'
    response = stock.get('aapl.us')
    # asserts
    assert isinstance(response, float)
    stock.requests.get.assert_called_with(expected_url)


def test_get_stock_wrong_code(mocker):
    """Sould get N/D"""
    mocker.spy(stock.requests, 'get')
    expected_url = 'https://stooq.com/q/l/?s=SDFG&f=sd2t2ohlcv&h&e=csv'
    response = stock.get('SDFG')
    # asserts
    assert response == 'N/D'
    stock.requests.get.assert_called_with(expected_url)
