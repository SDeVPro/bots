import telebot
bot = telebot.TeleBot('1291526355:AAHETlLqPVta2oO8a46xeOZt3nJXmTq5H48')
keyboard1 = telebot.types.ReplyKeyboardMarkup(True,True)
keyboard1.row('Salom','Xayr','Salomat','Omonmisiz','Chuvak')

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id,"Salom siz! /start tugmasini bosdingiz!", reply_markup=keyboard1)

@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text.lower() == 'salom':
        bot.send_message(message.chat.id,'Salom chuvak')
    elif message.text.lower()=='xayr':
        bot.send_message(message.chat.id, 'Uydilaga salom!')
    elif message.text.lower()=='salomat':
        bot.send_message(message.chat.id, 'Uydila uydami')
    elif message.text.lower()=='omonmisiz':
        bot.send_message(message.chat.id, 'pul kam ukam')
    elif message.text.lower() == 'chuvak':
        video = open('video.mp4', 'rb')
        bot.send_video(message.chat.id, video)
        file_id = 'AAAaaaZZZzzz'
        bot.send_video(message.chat.id, file_id)


bot.polling()