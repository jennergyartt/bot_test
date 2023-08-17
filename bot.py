from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from config import TOKEN


def start(update, context):
    user = update.effective_user
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text=f"Hellow, {user.first_name}!")
# Функция-обработчик для команды /help
def help(update, context):
    user = update.effective_user
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text=f"help, {user.first_name}")

# Функция-обработчик для обычных текстовых сообщений
def echo(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text=update.message.text)

def main():
    updater = Updater(token=TOKEN, use_context=True)

    dp = updater.dispatcher

    # Добавляем обработчик команды /start
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", start))

    # Добавляем обработчик обычных текстовых сообщений
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))

    # Запускаем бота
    updater.start_polling()

    # Останавливаем бота при нажатии Ctrl+C
    updater.idle()

