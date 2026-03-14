import logging
from client import get_client

client = get_client()

def place_market_order(symbol, side, quantity):

    order = client.futures_create_order(
        symbol=symbol,
        side=side,
        type="MARKET",
        quantity=quantity
    )

    logging.info(f"Market order response: {order}")
    return order


def place_limit_order(symbol, side, quantity, price):

    order = client.futures_create_order(
        symbol=symbol,
        side=side,
        type="LIMIT",
        quantity=quantity,
        price=str(price),
        timeInForce="GTC"
    )

    logging.info(f"Limit order response: {order}")
    return order
