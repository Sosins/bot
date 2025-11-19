import telebot

token = "YOUR_TELEGRAM_BOT_TOKEN"
bot = telebot.TeleBot(token)

secret_number = 5

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "سلام! یک عدد بین ۱ تا ۱۰ حدس بزن.")

@bot.message_handler(func=lambda m: True)
def game(message):
    try:
        guess = int(message.text)
        if guess == secret_number:
            bot.reply_to(message, "آفرین! درست حدس زدی 🎉")
        else:
            bot.reply_to(message, "نه! دوباره امتحان کن.")
    except:
        bot.reply_to(message, "فقط عدد بفرست.")

bot.polling(none_stop=True)
