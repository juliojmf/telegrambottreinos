import telebot
from wks import Worksheet

TELEGRAM_API_KEY = "" #your telegram bot api key

USER_IDS = {} #your dictionary with the telegram id's of your friends and their names on the google sheets worksheet (id:name)

bot = telebot.TeleBot(TELEGRAM_API_KEY)


@bot.message_handler(commands="start")
def start(message):
    text = f"Olá, envie o id {message.chat.id} para o admin para ser incluído no banco de dados"
    bot.send_message(message.chat.id, text)


@bot.message_handler(commands="stats")
def stats(message):
    worksheet = Worksheet(USER_IDS[message.chat.id])
    text = f"Seus status são:\n" \
           f"{worksheet.week_wkts} treinos essa semana\n" \
           f"{worksheet.month_wkts} treinos esse mês\n" \
           f"{worksheet.year_wkts} treinos esse ano"
    bot.send_message(message.chat.id, text)


@bot.message_handler(commands="addtreino")
def addtreino(message):
    text = message.text.split()
    if len(text) != 1:
        date = text[1]
        run = bike = swim = gym = other = 0
        if "run" in text:
            run = 1
        if "bike" in text:
            bike = 1
        if "swim" in text:
            swim = 1
        if "gym" in text:
            gym = 1
        if "outro" in text:
            other = 1
        workout = [date, run, bike, swim, gym, other]
        worksheet = Worksheet(USER_IDS[message.chat.id])
        worksheet.addworkout(workout)
        bot.send_message(message.chat.id, "Treino adicionado com sucesso!")
    else:
        text = "Para adicionar treinos digite /addtreino a data e os treinos q fez no dia\n"\
               "Ex: /addtreino 18/01/2022 run bike swim gym outro \n"\
               "(Use somente essas palavras e a data no formato DD/MM/AAAA)"
        bot.send_message(message.chat.id, text)


@bot.message_handler(func=lambda a: True)
def answer(message):
    text = "Oi, eu sou o bot do PROJETO 2022, escolha um dos comandos para continuar:\n" \
           "/start\n" \
           "/stats\n" \
           "/addtreino"
    bot.send_message(message.chat.id, text)


print("Bot ligado")
bot.polling()
