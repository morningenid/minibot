import telebot

token = '347016628:AAFC-37e9_oXN4RaWepmDZCUS4zJ7cWNOVQ'
bot = telebot.TeleBot(token)

@bot.message_handler(content_types=["text"])
def repeat_all_messages(message): 
    bot.send_message(message.chat.id, message.text)


if __name__ == "__main__":
    bot.polling(none_stop=True)

repeat_all_messages ()
