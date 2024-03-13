import random
from googletrans import Translator
import telebot


lang_list = ("en", "ru", "be", "hy", "ka", "he", "el", "de", "fr", "it", "pl", "uk", "es", "pt", "hu", "ja", "cs", "ar")


TOKEN = "*********************"


bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(message.chat.id, "Переводчик с русского на рандомный")


@bot.message_handler(content_types=["text"])
def trans(message):
    text = message.text
    while True:
        rand_num = random.randint(0, 17)
        break
    translating = Translator()
    result = translating.translate(text, src="ru", dest=lang_list[rand_num])
    print(result.text)
    bot.send_message(message.chat.id, result.text)


bot.infinity_polling()
