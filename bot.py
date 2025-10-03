from telebot import TeleBot

# توکن از Environment Variable خونده میشه
TOKEN ="7779922952:AAEQ1gb9RUgJTw0PrnVQfGyazbw_LxX5QIQ"

# اگر توکن خالی بود خطا بده

bot = TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "سلام داداش! ربات روی Render وصل شد 😎")

@bot.message_handler(commands=['help'])
def help_command(message):
    bot.reply_to(message, "این ربات آماده کاره! /start رو تست کن.")

# ربات همیشه آنلاین با polling
bot.polling(none_stop=True, timeout=60)

