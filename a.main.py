from telegram.ext import Updater, CommandHandler
from config import TOKEN

def start(update, context):
    update.message.reply_text('Olá! Eu sou o Sexta-feira Futebol Bot.')

def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    updater.start_polling()
    updater.idle()

if name == 'main':
    main()
