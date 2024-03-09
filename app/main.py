from telegram import (
    Update,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    CallbackQuery,
    error
)
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    ContextTypes,
    CallbackQueryHandler,
)
from app import settings
from app.keyboard_builder import generate_keyboard
import json

from utils import CurrenciesService

cs = CurrenciesService('r6dtufctrc')

async def prepare_currencies(currencies: list[dict]) -> str:
    msg = 'currencies: \n\n'
    
    for currency in currencies:
        value = currency.get('Value')
        name = currency.get('CharCode')
        msg += f'{name}: {round(value,2)} RUB \n'
        
    return msg

async def command_start(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
) -> None:
    await update.message.reply_text(
        "Please choose:",
        reply_markup=await generate_keyboard(),
    )


async def command_news(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
) -> None:
    await update.message.reply_text("News")


async def command_currencies(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
) -> None:
    await update.message.reply_text("Currencies")


async def callback_news(
    query: CallbackQuery,
) -> None:
    try: 
        await query.edit_message_text(
            "news",
            reply_markup=await generate_keyboard(),
        )
    except error.BadRequest:
        pass

async def callback_currencies(
    query: CallbackQuery,
) -> None:
    try: 
        raw_currencies = await cs.get_currencies()
        msg = await prepare_currencies(raw_currencies)
        await query.edit_message_text(
            msg,
            reply_markup=await generate_keyboard(),
        )
    except error.BadRequest:
        pass
    


async def callbacks(
    update: Update, context: ContextTypes
) -> None:
    query = update.callback_query
    await query.answer()
    match query.data:
        case "request_news":
            await callback_news(query)
        case "request_currencies":
            await callback_currencies(query)
    # await query.edit_message_text(text=f"Selected option: {query.data}")


def main() -> None:
    app = (
        ApplicationBuilder()
        .token(settings.TG_BOT_TOKEN)
        .build()
    )

    app.add_handler(
        CommandHandler("start", command_start)
    )
    app.add_handler(
        CommandHandler("news", command_news)
    )
    app.add_handler(
        CommandHandler(
            "currencies", command_currencies
        )
    )
    app.add_handler(
        CallbackQueryHandler(callbacks)
    )

    app.run_polling()


if __name__ == "__main__":
    main()
