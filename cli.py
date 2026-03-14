import argparse
from orders import place_market_order, place_limit_order
from validators import validate_side, validate_order_type
from logging_config import setup_logger

# Setup logging
setup_logger()

# CLI arguments
parser = argparse.ArgumentParser(description="Binance Futures Testnet Trading Bot")

parser.add_argument("--symbol", required=True, help="Trading symbol e.g. BTCUSDT")
parser.add_argument("--side", required=True, help="BUY or SELL")
parser.add_argument("--type", required=True, help="MARKET or LIMIT")
parser.add_argument("--quantity", required=True, type=float)
parser.add_argument("--price", type=float, help="Required for LIMIT orders")

args = parser.parse_args()

# Validation
validate_side(args.side)
validate_order_type(args.type)

print("\nOrder Request Summary")
print("----------------------")
print("Symbol:", args.symbol)
print("Side:", args.side)
print("Type:", args.type)
print("Quantity:", args.quantity)

if args.type == "LIMIT":
    print("Price:", args.price)

try:

    if args.type == "MARKET":
        response = place_market_order(args.symbol, args.side, args.quantity)

    else:
        response = place_limit_order(args.symbol, args.side, args.quantity, args.price)

    print("\nOrder Response")
    print("----------------------")
    print("Order ID:", response.get("orderId"))
    print("Status:", response.get("status"))
    print("Executed Qty:", response.get("executedQty"))

except Exception as e:

    print("\nError placing order:", e)
