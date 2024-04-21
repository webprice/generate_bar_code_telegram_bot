# Generate Bar Code Telegram Bot

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Issues](https://img.shields.io/github/issues/webprice/generate_bar_code_telegram_bot.svg)](https://github.com/webprice/generate_bar_code_telegram_bot/issues)
[![Stars](https://img.shields.io/github/stars/webprice/generate_bar_code_telegram_bot.svg)](https://github.com/webprice/generate_bar_code_telegram_bot/stargazers)

## I'm alive!
Please visit me @ https://t.me/responseWithBarcodeBot

## Description

This project is a Telegram bot that generates barcodes based on user input. It is a fork of the [generate-qr-code-telegram-bot](https://github.com/webprice/generate-qr-code-telegram-bot) project and extends its functionality to create barcodes in addition to QR codes.

The bot allows users to send text messages and receive barcode images as responses. The bot supports Code128, and do not allow customizations. Limited to 64 chars.

## Features

- Generates barcodes from user-inputted messages
- Supports Code128 barcodes
- Customizable barcode appearance
- Easy-to-use Telegram bot interface

## Installation

To use this bot, follow the steps below:

1. Clone the repository:
    ```bash
    git clone https://github.com/webprice/generate_bar_code_telegram_bot.git
    cd generate_bar_code_telegram_bot
    ```

2. Set up a virtual environment and install dependencies:
    ```bash
    python -m venv .venv
    source .venv/bin/activate
    pip install -r requirements.txt
    ```

3. Configure the bot with your Telegram API token:
    - Create a `.env` file in the root directory and add your Telegram API token:
    ```plaintext
    TELEGRAM_API_TOKEN=your_token_here
    ```

4. Run the bot:
    ```bash
    python main.py
    ```

## Usage

1. Start the bot by sending the `/start` command in Telegram.
2. Send a message to the bot containing the text you want to convert to a barcode.
3. The bot will respond with an image of the generated barcode.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments

- The project is a fork of the [generate-qr-code-telegram-bot](https://github.com/webprice/generate-qr-code-telegram-bot) project.

Thank you for using the Generate Bar Code Telegram Bot! Let me know if you have any questions or feedback.
