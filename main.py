
import uvicorn
import logging
from settings import settings

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

def barcode_app():
    from generate_bar_code_telegram_bot.telegram_bot.barcode_core import run_bot
    print(f"Starting {settings.BARCODE_TELEGRAM_BOT_URL} barcode generator")
    run_bot()

def main():
    uvicorn.run("main:barcode_app", host="0.0.0.0", port=settings.APP_PORT, log_level="info", reload=True)

if __name__ == '__main__':
    main()