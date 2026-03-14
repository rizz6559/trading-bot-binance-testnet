# Binance Futures Testnet Trading Bot

A simple Python CLI-based trading bot that places **MARKET** and **LIMIT** orders on the **Binance Futures Testnet (USDT-M)**.

This project demonstrates structured code design, CLI input handling, logging, and error handling while interacting with the Binance Futures Testnet API.

---

## Features

- Place **MARKET orders**
- Place **LIMIT orders**
- Supports both **BUY** and **SELL**
- Command Line Interface (CLI) for user input
- Input validation
- Logging of API responses and errors
- Clean modular code structure

---

## Project Structure

trading-bot-binance-testnet
│
├── cli.py                # CLI entry point
├── client.py             # Binance API client setup
├── orders.py             # Order execution logic
├── validators.py         # Input validation functions
├── logging_config.py     # Logging configuration
├── requirements.txt      # Project dependencies
├── README.md             # Project documentation
└── trading_bot.log       # Log file with API responses
