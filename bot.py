import telebot
from telebot import types

# Замените 'YOUR_TOKEN' на токен вашего бота
TOKEN = '7874039130:AAERMZOEPdps7hBOn_E6V9TANs6VGHJEA_Q'
bot = telebot.TeleBot(TOKEN)

# Функция для отображения главного меню
def show_menu(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Смартфоны")
    item2 = types.KeyboardButton("Планшеты")
    item3 = types.KeyboardButton("Аксессуары")
    markup.add(item1, item2, item3)

    bot.send_message(message.chat.id, "Выберите категорию телефонов:", reply_markup=markup)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.send_message(message.chat.id, "Привет! Я бот, который поможет вам с выбором телефонов. Нажмите /menu, чтобы начать.")

@bot.message_handler(commands=['menu'])
def menu(message):
    show_menu(message)

@bot.message_handler(func=lambda message: True)
def handle_option(message):
    if message.text == "Смартфоны":
        bot.send_message(message.chat.id, "Вы выбрали Смартфоны! Вот несколько популярных моделей:\n1. iPhone 14\n2. Samsung Galaxy S23\n3. Google Pixel 7")
    elif message.text == "Планшеты":
        bot.send_message(message.chat.id, "Вы выбрали Планшеты! Вот несколько популярных моделей:\n1. iPad Pro\n2. Samsung Galaxy Tab S8\n3. Microsoft Surface Pro 8")
    elif message.text == "Аксессуары":
        bot.send_message(message.chat.id, "Вы выбрали Аксессуары! Вот несколько популярных аксессуаров:\n1. Наушники AirPods\n2. Чехлы для телефонов\n3. Зарядные устройства")
    else:
        bot.send_message(message.chat.id, "Пожалуйста, выберите категорию телефонов из меню или введите /menu.")

# Запуск бота
bot.polling()