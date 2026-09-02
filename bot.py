import os
import json
import threading
from flask import Flask
import telebot

# 1. ФОНОВЫЙ ВЕБ-СЕРВЕР ДЛЯ RENDER
app = Flask('')

@app.route('/')
def home():
    return "Бот работает!"

def run():
    # Render автоматически передаст нужный порт
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)

# Запуск Flask в отдельном потоке
threading.Thread(target=run, daemon=True).start()


# 2. НАСТРОЙКА БОТА
# Берем токен из переменных окружения Render для безопасности
TOKEN = os.environ.get("BOT_TOKEN", "7736359345:AAHeJie9mMVx09GG3rH9fLbacVAW57sYzII")
bot = telebot.TeleBot(TOKEN)

# Загрузка данных один раз при старте
with open("materials.json", "r", encoding="utf-8") as f:
    data = json.load(f)
    code_to_name = data.get("code_to_name", {})
    name_to_code = data.get("name_to_code", {})

# Обработка команды /start
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Отправь мне код или название материала, и я найду его для тебя.")

# Обработка всех текстовых сообщений
@bot.message_handler(func=lambda message: message.text is not None)
def handle_message(message):
    query = message.text.strip().lower()
    results = []

    # Поиск по коду
    for code, name in code_to_name.items():
        if query in code.lower():
            results.append(f"{code} — {name}")

    # Поиск по названию
    for name, code in name_to_code.items():
        entry = f"{code} — {name}"
        if query in name.lower() and entry not in results:
            results.append(entry)

    # Ответ пользователю
    if results:
        MAX_MESSAGE_LENGTH = 4000
        response = "\n".join(results)
        for i in range(0, len(response), MAX_MESSAGE_LENGTH):
            bot.send_message(message.chat.id, response[i:i+MAX_MESSAGE_LENGTH])
    else:
        bot.send_message(message.chat.id, "Ничего не найдено.")


# 3. БЕЗКОНЕЧНЫЙ ЗАПУСК БОТА (В САМОМ КОНЦЕ)
if __name__ == "__main__":
    print("Бот запущен...")
    # На хостингах лучше использовать infinity_polling вместо polling
    bot.infinity_polling()