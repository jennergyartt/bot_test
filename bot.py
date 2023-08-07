from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from config import TOKEN

# Функция-обработчик для команды /start
def start(update, context):
    user = update.effective_user
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text=f"Hi, {user.first_name}!")

def help(update, context):
    user = update.effective_user
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text=f"help, {user.first_name}!")

# Функция-обработчик для обычных текстовых сообщений
def echo(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text=update.message.text)

def main():
    # Создаем объект Updater и передаем ему токен бота
    updater = Updater(token=TOKEN, use_context=True)

    # Получаем диспетчер для регистрации обработчиков команд и сообщений
    dp = updater.dispatcher

    # Добавляем обработчик команды /start
    dp.add_handler(CommandHandler("start", start))

    # Добавляем обработчик обычных текстовых сообщений
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))

    # Запускаем бота
    updater.start_polling()

    # Останавливаем бота при нажатии Ctrl+C
    updater.idle()

if __name__ == '__main__':
    main()
