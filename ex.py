import flask
import telebot
import conf
from telebot import types


WEBHOOK_URL_BASE = "https://{}:{}".format(conf.WEBHOOK_HOST, conf.WEBHOOK_PORT)
WEBHOOK_URL_PATH = "/{}/".format(conf.TOKEN)

bot = telebot.TeleBot(conf.TOKEN, threaded=False)

bot.remove_webhook()

bot.set_webhook(url=WEBHOOK_URL_BASE+WEBHOOK_URL_PATH)

app = flask.Flask(__name__)

f = open('results.csv', 'r', encoding = 'utf-8')

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.send_message(message.chat.id, 'Привет! Я - бот, который спрашивает анкету по типологии признаков "острый - тупой".')
	bot.send_message(message.chat.id, 'Я буду задавать тебе вопросы на русском языке. Напиши, пожалуйста, название языка, на котором ты будешь отвечать.')
	with open('results.csv', 'a', encoding = 'utf-8') as results: 
                results.write(message.text+'\n')

f = open(таблица, 'r', encoding = 'utf-8')
table = f.read()
words = table1.split('\n')
f.close()

@bot.message_handler(func=lambda m: True)
def send_len(message):        
        i = 0
        question1 = 'Можно ли на вашем языке употребить слово "тупой" вместе со словом ' + words1[i] + '?'
        question2 = 'Можно ли на вашем языке употребить слово "острый" вместе со словом ' + words1[i] + '?'
        keyboard = types.ReplyKeyboardMarkup(row_width=2)
        btn1 = types.KeyboardButton('да')
        btn2 = types.KeyboardButton('нет')
        keyboard.add(btn1, btn2)
        if i < len(words1):
                tb.send_message(chat_id, question1, reply_markup=keyboard)
                if KeyboardButton == bt1:
                        bot.send_message(message.chat.id, 'Напиши, пожалуйста, как это будет на твоем языке.')
                        with open('results.csv', 'a', encoding = 'utf-8') as results:
                                results.write(message.text+'\n')
                else:
                        continue                
        else:
                tb.send_message(chat_id, question2, reply_markup=keyboard)
                if KeyboardButton == bt1:
                        bot.send_message(message.chat.id, 'Напиши, пожалуйста, как это будет на твоем языке.')
                        with open('results.csv', 'a', encoding = 'utf-8') as results:
                                results.write(message.text+'\n')
                else:
                        continue
                i = i + 1
        bot.send_message(message.chat.id, 'Чтобы посмотреть на свои ответы, набери \answers.')

@bot.message_handler(commands=['answers'])
def send_answers(message):
        f = open('results.csv', 'r', encoding = 'utf-8')
        answers = f.read()
        f.close()
	bot.send_message(message.chat.id, answers)


@app.route('/', methods=['GET', 'HEAD'])
def index():
    return 'ok'


@app.route(WEBHOOK_URL_PATH, methods=['POST'])
def webhook():
    if flask.request.headers.get('content-type') == 'application/json':
        json_string = flask.request.get_data().decode('utf-8')
        update = telebot.types.Update.de_json(json_string)
        bot.process_new_updates([update])
        return ''
    else:
