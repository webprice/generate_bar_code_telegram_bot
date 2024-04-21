from dotenv import load_dotenv
import os

load_dotenv()


class Settings():
    BARCODE_TELEGRAM_BOT_TOKEN: str = os.environ.get("BARCODE_TELEGRAM_BOT_TOKEN")
    GITHUB_REPO_URL: str = os.environ.get("GITHUB_REPO_URL")
    OWNER_TELEGRAM_ID: str = os.environ.get("OWNER_TELEGRAM_ID")
    OWNER_WEBSITE_URL: str = os.environ.get("OWNER_WEBSITE_URL") if os.environ.get("OWNER_WEBSITE_URL") else "https://hrekov.com/"
    BARCODE_TEXT_LENGTH: int = int(os.environ.get("BARCODE_TEXT_LENGTH")) if os.environ.get("BARCODE_TEXT_LENGTH") else 64
    BARCODE_IMAGE_BOX_SIZE: int = int(os.environ.get("BARCODE_IMAGE_BOX_SIZE")) if os.environ.get("BARCODE_IMAGE_BOX_SIZE") else 512
    BARCODE_TELEGRAM_BOT_URL: str = os.environ.get("BARCODE_TELEGRAM_BOT_URL") if os.environ.get("BARCODE_TELEGRAM_BOT_URL") else "https://t.me/responseWithBarcodeBot"
    APP_PORT: int = int(os.environ.get("APP_PORT")) if os.environ.get("APP_PORT") else 8001

settings = Settings()


