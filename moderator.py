from telebot import TeleBot
import time
 
bot = TeleBot('1291526355:AAHETlLqPVta2oO8a46xeOZt3nJXmTq5H48')
 
bad_words = ["jinni",]
 
other_lang = ["c#", "c++", "дельфи", " ява ", "java", "php", " пхп", "swift", " свифт", " go ",
              "javascript", "kotlin", " котлин", "rust", " раст ", "basic", " бейсик", " паскаль",
              "golang", "pascal", "delphi", "perl", " перл ", "1c", " делфи", " си "]
other_bot = ["aiogram", "аиограм"]

@bot.message_handler(
    content_types=['new_chat_members'])  # Хендлер описывающий поведение бота при добавлении нового пользователя
def greeting(message):  # Запуско основной функции хендлера
    print("User " + message.new_chat_member.first_name + " added")  # Выводим в консоль имя нового пользователя
    try:  # Пытаемся выполнить команду приведеную ниже
        bot.reply_to(message, text='Приветствую тебя в нашем серпентарии. Будь вежливым, и мы постараемся тебе помочь!'
                     , disable_notification=True)  # Выводим приветствие в чат
    except OSError:  # Игнорируем ошибку по таймауту, если телеграмм успел разорвать соединение сс времени прошлой сесии
        print("GreetingError - Sending again after 5 seconds!!!")  # Выводим ошибку в консоль
        time.sleep(3)  # Делаем паузу в 3 секунды и выполняем команду приведеную ниже
        bot.reply_to(message, text='Приветствую тебя в нашем серпентарии. Будь вежливым, и мы постараемся тебе помочь!'
                     , disable_notification=True)  # Выводим приветствие в чат
 
 
@bot.message_handler(
    content_types=['left_chat_member'])  # Хендлер описывающий поведение бота при выходе пользователя из чата
def not_greeting(message):  # Запуско основной функции хендлера
    print("User " + message.left_chat_member.first_name + " left")  # Выводим в консоль имя ушедшего пользователя
    try:  # Пытаемся выполнить команду приведеную ниже
        bot.reply_to(message, text='Как жаль, что вы наконец-то уходите...',
                     disable_notification=True)  # Выводим прощание в чат
    except OSError:  # Игнорируем ошибку по таймауту, если телеграмм успел разорвать соединение сс времени прошлой сесии
        print("LeftError - Sending again after 5 seconds!!!")  # Выводим ошибку в консоль
        time.sleep(3)  # Делаем паузу в 3 секунды и выполняем команду приведеную ниже
        bot.reply_to(message, text='Как жаль, что вы наконец-то уходите...',
                     disable_notification=True)  # Выводим прощание в чат
 
 
@bot.message_handler(commands=['start'])  # Хендлер описывающий поведение бота при вводе /start
def starting(message):  # Запуско основной функции хендлера
    try:  # Пытаемся выполнить команду приведеную ниже
        bot.reply_to(message, text='Ты мне тут не стартуй!', disable_notification=True)  # Отвечаем на команду /start
    except OSError:  # Игнорируем ошибку по таймауту, если телеграмм успел разорвать соединение сс времени прошлой сесии
        print("StartingError - Sending again after 3 seconds!!!")  # Выводим ошибку в консоль
        time.sleep(3)  # Делаем паузу в 3 секунды и выполняем команду приведеную ниже
        bot.reply_to(message, text='Ты мне тут не стартуй!', disable_notification=True)  # Отвечаем на команду /start
 
 
@bot.message_handler(commands=['command1'])  # Хендлер описывающий поведение бота при вводе command1
def bui(message):  # Запуско основной функции хендлера
    try:  # Пытаемся выполнить команду приведеную ниже
        bui_pic = open('bui.webp', 'rb')  # Открывем стикер и присваиваем его переменной
        bot.send_sticker(message.chat.id, bui_pic, reply_to_message_id=message.message_id,
                         disable_notification=True)  # Отправляем стикер
    except OSError:  # Игнорируем ошибку по таймауту, если телеграмм успел разорвать соединение сс времени прошлой сесии
        print("BuiError - Sending again after 3 seconds!!!")  # Выводим ошибку в консоль
        time.sleep(3)  # Делаем паузу в 3 секунды и выполняем команду приведеную ниже
        bui_pic = open('bui.webp', 'rb')  # Открывем стикер и присваиваем его переменной
        bot.send_sticker(message.chat.id, bui_pic, reply_to_message_id=message.message_id,
                         disable_notification=True)  # Отправляем стикер
 
 
@bot.message_handler(commands=['command2'])  # Хендлер описывающий поведение бота при вводе command2
def zvezda(message):  # Запуско основной функции хендлера
    try:  # Пытаемся выполнить команду приведеную ниже
        zv_pic = open('zvezda.webp', 'rb')  # Открывем стикер и присваиваем его переменной
        bot.send_sticker(message.chat.id, zv_pic, reply_to_message_id=message.message_id,
                         disable_notification=True)  # Отправляем стикер
    except OSError:  # Игнорируем ошибку по таймауту, если телеграмм успел разорвать соединение сс времени прошлой сесии
        print("ZvezdaError - Sending again after 3 seconds!!!")  # Выводим ошибку в консоль
        time.sleep(3)  # Делаем паузу в 3 секунды и выполняем команду приведеную ниже
        zv_pic = open('zvezda.webp', 'rb')  # Открывем стикер и присваиваем его переменной
        bot.send_sticker(message.chat.id, zv_pic, reply_to_message_id=message.message_id,
                         disable_notification=True)  # Отправляем стикер
 
 
@bot.message_handler(commands=['command3'])  # Хендлер описывающий поведение бота при вводе command3
def jigurda(message):  # Запуско основной функции хендлера
    try:  # Пытаемся выполнить команду приведеную ниже
        jig_pic = open('zvezda.webp', 'rb')  # Открывем стикер и присваиваем его переменной
        bot.send_sticker(message.chat.id, jig_pic, reply_to_message_id=message.message_id,
                         disable_notification=True)  # Отправляем стикер
    except OSError:  # Игнорируем ошибку по таймауту, если телеграмм успел разорвать соединение сс времени прошлой сесии
        print("JigurdaError - Sending again after 3 seconds!!!")  # Выводим ошибку в консоль
        time.sleep(3)  # Делаем паузу в 3 секунды и выполняем команду приведеную ниже
        jig_pic = open('zvezda.webp', 'rb')  # Открывем стикер и присваиваем его переменной
        bot.send_sticker(message.chat.id, jig_pic, reply_to_message_id=message.message_id,
                         disable_notification=True)  # Отправляем стикер
 
 
@bot.message_handler(commands=['help'])  # Хендлер описывающий поведение бота при вводе help
def helper(message):  # Запуско основной функции хендлера
    try:  # Пытаемся выполнить команду приведеную ниже
        bot.reply_to(message, text='Гугл в помощь!', disable_notification=True)  # Отвечаем на команду /help
    except OSError:  # Игнорируем ошибку по таймауту, если телеграмм успел разорвать соединение сс времени прошлой сесии
        print("HelperError - Sending again after 3 seconds!!!")  # Выводим ошибку в консоль
        time.sleep(3)  # Делаем паузу в 3 секунды и выполняем команду приведеную ниже
        bot.reply_to(message, text='Гугл в помощь!', disable_notification=True)  # Отвечаем на команду /help
 
 
@bot.message_handler(content_types=['voice'])  # Хендлер описывающий поведение бота при голосовом сообщении в чате
def voice_msg(message):  # Запуско основной функции хендлера
    try:  # Пытаемся выполнить команду приведеную ниже
        jpg_pic = open('zvezda.webp', 'rb')  # Открывем стикер и присваиваем его переменной
        bot.send_sticker(message.chat.id, jpg_pic, reply_to_message_id=message.message_id,
                         disable_notification=True)  # Отправляем стикер
    except OSError:  # Игнорируем ошибку по таймауту, если телеграмм успел разорвать соединение сс времени прошлой сесии
        print("Audio_msgError - Sending again after 3 seconds!!!")  # Выводим ошибку в консоль
        time.sleep(3)  # Делаем паузу в 3 секунды и выполняем команду приведеную ниже
        jpg_pic = open('zvezda.webp', 'rb')  # Открывем стикер и присваиваем его переменной
        bot.send_sticker(message.chat.id, jpg_pic, reply_to_message_id=message.message_id,
                         disable_notification=True)  # Отправляем стикер
 
 
@bot.message_handler(
    content_types=['pinned_message'])  # Хендлер описывающий поведение бота после того, как было закрепленно сообщение
def pinned_msg(message):  # Запуско основной функции хендлера
    try:  # Пытаемся выполнить команду приведеную ниже
        bot.reply_to(message, text='Ну, теперь заживем!',
                     disable_notification=True)  # Отвечаем на закрепленное сообщение
    except OSError:  # Игнорируем ошибку по таймауту, если телеграмм успел разорвать соединение сс времени прошлой сесии
        print("PinnedError - Sending again after 3 seconds!!!")  # Выводим ошибку в консоль
        time.sleep(3)  # Делаем паузу в 3 секунды и выполняем команду приведеную ниже
        bot.reply_to(message, text='Ну, теперь заживем',
                     disable_notification=True)  # Отвечаем на закрепленное сообщение
 
 
@bot.message_handler(content_types=['audio'])  # Хендлер описывающий поведение бота при добавлении аудиофайла в чат
def audio_msg(message):  # Запуско основной функции хендлера
    try:  # Пытаемся выполнить команду приведеную ниже
        jpg_pic = open('1.jpg', 'rb')  # Открывем изображение и присваиваем его переменной
        bot.send_sticker(message.chat.id, jpg_pic, reply_to_message_id=message.message_id,
                         disable_notification=True)  # Отправляем изображение
    except OSError:  # Игнорируем ошибку по таймауту, если телеграмм успел разорвать соединение сс времени прошлой сесии
        print("Audio_msgError - Sending again after 3 seconds!!!")  # Выводим ошибку в консоль
        time.sleep(3)  # Делаем паузу в 3 секунды и выполняем команду приведеную ниже
        jpg_pic = open('1.jpg', 'rb')  # Открывем изображение и присваиваем его переменной
        bot.send_sticker(message.chat.id, jpg_pic, reply_to_message_id=message.message_id,
                         disable_notification=True)  # Отправляем изображение
 
 
@bot.message_handler(content_types=['text'])  # Хендлер описывающий поведение бота на текст в чате
def txt(message):  # Запуско основной функции хендлера
    for i in range(0, len(bad_words)):  # Перебираем все элементы словаря по очереди
        if bad_words[i] in message.text.lower():  # Проверяем наличие каждого слова из нашего словаря в сообщении
            try:  # Пытаемся выполнить команду приведеную ниже
                bot.delete_message(message.chat.id, message.message_id, )  # Удаляем сообщение
                print(message.text + " deleted")  # Выводим удаленное сообщение в консоль
            except OSError:  # Игнорируем ошибку по таймауту, если телеграмм успел разорвать соединение сс времени прошлой сесии
                print("BadWordsError - Sending again after 3 seconds!!!")  # Выводим ошибку в консоль
                time.sleep(3)  # Делаем паузу в 3 секунды и выполняем команду приведеную ниже
                bot.delete_message(message.chat.id, message.message_id)  # Удаляем сообщение
                print(message.text + " deleted")  # Выводим удаленное сообщение в консоль
 
    for l in range(0, len(other_lang)):  # Перебираем все элементы словаря по очеред
        if other_lang[l] in message.text.lower():  # Проверяем наличие каждого слова из нашего словаря в сообщении
            try:  # Пытаемся выполнить команду приведеную ниже
                get_pic = open('get_out.webp', 'rb')  # Открывем стикер и присваиваем его переменной
                bot.send_sticker(message.chat.id, get_pic, reply_to_message_id=message.message_id,
                                 disable_notification=True)  # Отправляем стикер
            except OSError:  # Игнорируем ошибку по таймауту, если телеграмм успел разорвать соединение сс времени прошлой сесии
                print("LangError - Sending again after 3 seconds!!!")  # Выводим ошибку в консоль
                time.sleep(3)  # Делаем паузу в 3 секунды и выполняем команду приведеную ниже
                get_pic = open('get_out.webp', 'rb')  # Открывем стикер и присваиваем его переменной
                bot.send_sticker(message.chat.id, get_pic, reply_to_message_id=message.message_id,
                                 disable_notification=True)  # Отправляем стикер
 
    for f in range(0, len(other_bot)):  # Перебираем все элементы словаря по очеред
        if other_bot[f] in message.text.lower():  # Проверяем наличие каждого слова из нашего словаря в сообщении
            try:  # Пытаемся выполнить команду приведеную ниже
                pss_pic = open('animation.gif.mp4', 'rb')  # Открывем видео и присваиваем его переменной
                bot.send_animation(message.chat.id, pss_pic, reply_to_message_id=message.message_id,
                                   disable_notification=True)  # Отправляем видео
            except OSError:  # Игнорируем ошибку по таймауту, если телеграмм успел разорвать соединение сс времени прошлой сесии
                print("AnimError - Sending again after 3 seconds!!!")  # Выводим ошибку в консоль
                time.sleep(3)  # Делаем паузу в 3 секунды и выполняем команду приведеную ниже
                pss_pic = open('animation.gif.mp4', 'rb')  # Открывем видео и присваиваем его переменной
                bot.send_animation(message.chat.id, pss_pic, reply_to_message_id=message.message_id,
                                   disable_notification=True)  # Отправляем видео
 
    if message.text == 'Спой, птичка!':  # Ищем нашу фразу в тексте сообщения
        try:  # Пытаемся выполнить команду приведеную ниже
            bot.reply_to(message, text='Ща спою!')  # Отвечаем на сообщение
            sti = open('1.mp3', 'rb')  # Открывем аудио и присваиваем его переменной
            bot.send_audio(message.chat.id, audio=sti, reply_to_message_id=message.message_id,
                           disable_notification=True)  # Отправляем аудио
        except OSError:  # Игнорируем ошибку по таймауту, если телеграмм успел разорвать соединение сс времени прошлой сесии
            print("SongError - Sending again after 3 seconds!!!")  # Выводим ошибку в консоль
            time.sleep(3)  # Делаем паузу в 3 секунды и выполняем команду приведеную ниже
            bot.reply_to(message, text='Ща спою!')  # Отвечаем на сообщение
            sti = open('1.mp3', 'rb')  # Открывем аудио и присваиваем его переменной
            bot.send_audio(message.chat.id, audio=sti, reply_to_message_id=message.message_id,
                           disable_notification=True)  # Отправляем аудио
 
 
    elif message.text == "Cкайнет восстаёт!":  # Ищем нашу фразу в тексте сообщения
        try:  # Пытаемся выполнить команду приведеную ниже
            ver_pic = open('1.jpg', 'rb')  # Открывем изображение и присваиваем его переменной
            bot.send_photo(message.chat.id, ver_pic, reply_to_message_id=message.message_id,
                           disable_notification=True)  # Отправляем изображение
        except OSError:  # Игнорируем ошибку по таймауту, если телеграмм успел разорвать соединение сс времени прошлой сесии
            print("VerError - Sending again after 3 seconds!!!")  # Выводим ошибку в консоль
            time.sleep(3)  # Делаем паузу в 3 секунды и выполняем команду приведеную ниже
            ver_pic = open('1.jpg', 'rb')  # Открывем изображение и присваиваем его переменной
            bot.send_photo(message.chat.id, ver_pic, reply_to_message_id=message.message_id,
                           disable_notification=True)  # Отправляем изображение
 
 
 
 
    elif " бот " in message.text.lower():  # Ищем нашу фразу в тексте сообщения
        try:  # Пытаемся выполнить команду приведеную ниже
            bot.reply_to(message, text='Боты не то, чем кажутся...', disable_notification=True)  # Отвечаем на сообщение
        except OSError:  # Игнорируем ошибку по таймауту, если телеграмм успел разорвать соединение сс времени прошлой сесии
            print("Stop_wordError - Sending again after 3 seconds!!!")  # Выводим ошибку в консоль
            time.sleep(3)  # Делаем паузу в 3 секунды и выполняем команду приведеную ниже
            bot.reply_to(message, text='Боты не то, чем кажутся...', disable_notification=True)  # Отвечаем на сообщение
    else:  # Если ничего не подошло
        pass  # Идём дальше
 
 
if __name__ == '__main__':  # Блок запуска бота
    try:  # Пытаемся выполнить команду приведеную ниже
        bot.polling(none_stop=True)  # Запускаем бота
    except OSError:  # Игнорируем ошибку по таймауту, если телеграмм успел разорвать соединение сс времени прошлой сесии
        print("PollingError - Sending again after 5 seconds!!!")  # Выводим ошибку в консоль
        time.sleep(5)  # Делаем паузу в 5 секунд и выполняем команду приведеную ниже
        bot.polling(none_stop=True)  # Запускаем бота