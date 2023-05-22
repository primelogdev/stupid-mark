import random
import sqlite3 
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# Функция для получения соединения с базой данных
def get_db_connection():
    return sqlite3.connect('messages.db')

# Обработчик команды /start
def start(update: Update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Привет! Добавь меня в группу, а чтобы я мог отвечать на все сообщения выдайте мне админку(можно без прав), а чтобы я отвечал только на сообщения в которых меня отметили, снимите админку!")

# Обработчик текстовых сообщений
def handle_message(update: Update, context):
    message = update.message.text

    if update.effective_chat.type == 'private':
        # Ответ на личное сообщение
        reply_text = "Чееееееееееел, добавь меня в чат бля!"
    else:
        # Ответ в групповом чате
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT message FROM messages ORDER BY RANDOM() LIMIT 1")
        result = cursor.fetchone()
        reply_text = result[0] if result else "Я не могу найти сообщение для ответа."
        conn.close()

    context.bot.send_message(chat_id=update.effective_chat.id, text=reply_text)

# Главная функция
def main():
    # Создание экземпляра бота и получение токена
    updater = Updater(token='токен', use_context=True)

    # Получение диспетчера для регистрации обработчиков
    dispatcher = updater.dispatcher

    # Регистрация обработчиков команды /start и текстовых сообщений
    dispatcher.add_handler(CommandHandler('start', start))
    dispatcher.add_handler(MessageHandler(Filters.text, handle_message))

    # Запуск бота
    updater.start_polling()

    # Остановка бота при нажатии Ctrl+C
    updater.idle()

if __name__ == '__main__':
    main()

