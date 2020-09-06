"""This module manage stock controller"""
import json
from jobsitychat.models import stock as stock_mdl
from jobsitychat.controllers import message as message_ctr


def send_stock(event):
    """Send stock by message"""
    message = json.loads(event['body'])['message']
    stock_code = message[7:len(message)]
    stock_value = stock_mdl.get(stock_code)
    if stock_value == 'N/D':
        message = f'stock code {stock_code} is wrong'
    else:
        message = f'{stock_code} quote is ${stock_value} per share'
    message_ctr.send_to_everyone(event, message)
