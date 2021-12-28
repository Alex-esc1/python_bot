import config
import telebot
import time

bot = telebot.TeleBot(config.token)        #Вставляете токен своего бота

@bot.message_handler(commands=['spec'])        #При написании в боте команды /spec будет начинаться рассылка
def spaw(message):

    request = 0
    handle = open("1.txt", "r")    #Тут путь к txt с id-шниками клиентов
    for line in handle:
        try:
            TEXT = open("text.txt", 'r', encoding="utf-8") #Тут путь к txt с сообщениями для клиентов (выборка по строчная 1 строка сообщения = 1-й строке ID клиента)
            bot.send_message(line, TEXT, parse_mode='html')
            request = request + 1
            time.sleep(0.5)
            print("Сообщение отправлено")    #Если сообщение отправлено в консоль будет выводиться "Сообщение отправлено"
            if request % 30 == 0:
                request = 0
        except:
            pass
    handle.close()

@bot.message_handler(content_types=["text"])
def repeat_all_messages(message):
    x = bot.send_message(message.chat.id, "Бот не отвечает, подождите с Вами свяжется менеджер")
    print(f"Имя клиента: {message.from_user.first_name} {message.from_user.last_name} @{message.from_user.username} id: {message.from_user.id} Сообщение: {message.text}")
    userid=902847747 #админ, который будет получать сообщения от клиентов (если они напишут боту)
    bot.send_message(userid, f"Имя клиента: {message.from_user.first_name} {message.from_user.last_name} @{message.from_user.username} Сообщение: {message.text}", parse_mode='html')
bot.polling ( none_stop = True )

