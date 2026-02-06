from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# Вставь сюда токен от BotFather
TOKEN = "123456789:AAAbbbCCCdddEEEfffGGG"

# Команда /start
def start(update: Update, context: CallbackContext):
    update.message.reply_text("Привет! Я твой тестовый бот 😎")

# Повторяем любое сообщение пользователя
def echo(update: Update, context: CallbackContext):
    update.message.reply_text(f"Ты написал: {update.message.text}")

# Настройка бота
updater = Updater(TOKEN)
updater.dispatcher.add_handler(CommandHandler("start", start))
updater.dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))

# Запуск бота
updater.start_polling()
updater.idle()
