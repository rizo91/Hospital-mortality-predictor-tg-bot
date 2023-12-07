import string

from telegram.ext import ApplicationBuilder, filters, \
                         CallbackQueryHandler, CommandHandler, MessageHandler
from handlers import *


with open('token.txt') as token_file:
    TOKEN = token_file.read()

bot = ApplicationBuilder().token(TOKEN).build()
bot.add_handler(CommandHandler("start", start))
bot.add_handler(MessageHandler(filters.TEXT, event_loop))
bot.add_handler(CallbackQueryHandler(event_loop))
bot.run_polling()
