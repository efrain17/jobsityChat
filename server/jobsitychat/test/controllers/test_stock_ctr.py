"""This module test stock controller"""
# pylint: disable=E1101
from jobsitychat.controllers import stock


def test_send_stock(mocker):
    """Sould insert a stock"""
    mocker.patch.object(stock.stock_mdl, 'get')
    mocker.patch.object(stock.message_ctr, 'send_to_everyone')
    stock.stock_mdl.get.return_value = 93.42
    event = {
        'body': '{"message": "/stock=appl.us"}'
    }
    expected_message = 'appl.us quote is $93.42 per share'
    stock.send_stock(event)
    # asserts
    stock.stock_mdl.get.assert_called_with('appl.us')
    stock.message_ctr.send_to_everyone.assert_called_with(event, expected_message)
