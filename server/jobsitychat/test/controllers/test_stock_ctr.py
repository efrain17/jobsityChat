"""This module test stock controller"""
# pylint: disable=E1101
from jobsitychat.controllers import stock


def test_send_stock(mocker):
    """Sould send a stock"""
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


def test_send_stock_not_found(mocker):
    """Sould send a stock not found"""
    mocker.patch.object(stock.stock_mdl, 'get')
    mocker.patch.object(stock.message_ctr, 'send_to_everyone')
    stock.stock_mdl.get.return_value = 'N/D'
    event = {
        'body': '{"message": "/stock=XYZ"}'
    }
    expected_message = 'stock code XYZ is wrong'
    stock.send_stock(event)
    # asserts
    stock.stock_mdl.get.assert_called_with('XYZ')
    stock.message_ctr.send_to_everyone.assert_called_with(event, expected_message)
