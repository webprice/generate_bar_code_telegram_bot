import asyncio
from settings import settings

from generate_bar_code_telegram_bot.bar_code.core import generate_barcode
from typing import Optional

import logging

logger = logging.getLogger(__name__)

def parse_update_message(update) -> Optional[str]:
    if not update.message.text:
        return None

    elif len(update.message.text) > settings.BARCODE_TEXT_LENGTH: #256
        return None

    else:
        return update.message.text


def handle_start_message(update, context):
    welcome_message = ("⚡Welcome to the Barcode code generator bot! \n\n "
                       "🦜Send me a message and I will generate a Barcode code for you. "
                      "You can also send me a link and I will generate a Barcode code for the link.\n\n"
                      f"⚫Bot source code:\n 👉{settings.GITHUB_REPO_URL}.\n\n"
                      f"⚫For any issues, feature requests, support and feedback visit my website:\n 👉{settings.OWNER_WEBSITE_URL}")

    update.message.reply_text(welcome_message, disable_web_page_preview=True)
    return


def handle_barcode_start_message(update, context):
    welcome_message = ("⚡⚡⚡Welcome to the Barcode code generator bot! \n\n "
                       "🦜Send me a message and I will generate a Barcode code for you. "
                      "You can also send me a link and I will generate a Barcode code for the link.\n\n"
                      f"⚫Bot source code:\n 👉{settings.GITHUB_REPO_URL}.\n\n"
                      f"⚫For any issues, feature requests, support and feedback visit my website:\n 👉{settings.OWNER_WEBSITE_URL}")

    update.message.reply_text(welcome_message, disable_web_page_preview=True)
    return

def handle_message(update, context):
    logger.info("update: %s", update)

    try:
        coverted = update.to_dict() #otherwise shadowing from builtins

    except Exception as e:
        logger.error("Error converting update to dict: %s", e)
        update.message.reply_text("Error processing your request")
        return

    if settings.OWNER_TELEGRAM_ID:
        if int(coverted["message"]["from"]["id"]) != int(settings.OWNER_TELEGRAM_ID):
            print(f'{coverted["message"]["from"]["id"]} - not authorized to use this bot')
            update.message.reply_text("You are not authorized to use this bot")
            return

    update.message.reply_text("Processing your request, please wait...")
    message = parse_update_message(update)
    if not message:
        update.message.reply_text("Error processing your request(Invalid message. Length should be less than 64 characters)")
        return

    try:
        buffer = asyncio.run(generate_barcode(message))
    except Exception as e:
        logger.error("Error generating Barcode code: %s", e)
        update.message.reply_text("Error processing your request")
        return

    if buffer is None:
        error_message = ("Error processing your request"
                                  f"⚫Bot source code: \n👉{settings.GITHUB_REPO_URL}. "
                                  f"⚫For any issues, feature requests, support and feedback: \n👉{settings.GITHUB_REPO_URL}")
        update.message.reply_text(error_message, disable_web_page_preview=True)
        return

    response_msg = ("🦜Barcode code generated successfully! Scan the Barcode code below to view the message.\n\n"
                    f"⚫Bot source code: \n👉{settings.GITHUB_REPO_URL}.\n "
                    f"⚫For any issues, feature requests, support and feedback: \n👉{settings.GITHUB_REPO_URL}")

    update.message.reply_photo(buffer, caption=response_msg)

    return