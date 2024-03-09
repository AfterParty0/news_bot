from telegram import (
    Update,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
)
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    ContextTypes,
    CallbackQueryHandler,
)
from app import settings


async def generate_keyboard():
    keyboard = [
        [
            InlineKeyboardButton(
                "Send news",
                callback_data="request_news",
            ),
            InlineKeyboardButton(
                "Send currencies",
                callback_data="request_currencies",
            ),
        ]
    ]
    return InlineKeyboardMarkup(keyboard)
