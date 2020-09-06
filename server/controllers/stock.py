"""This module manage stock controller"""
import json
from models import stock as stock_mdl
from controllers import message as message_ctr


def send_stock(event):
    """Send stock by message"""
    message = json.loads(event['body'])['message']
    stock_code = message[7:len(message)]
    stock_value = stock_mdl.get(stock_code)
    message = f'{stock_code} quote is ${stock_value} per share'
    message_ctr.send_to_everyone(event, message)
