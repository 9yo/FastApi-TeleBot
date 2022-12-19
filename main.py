import telebot

from fastapi import FastAPI, Request
from fastapi.openapi.models import Response


HOST = 'HOST ADDRESS'
BOT_TOKEN = 'TELEGRAM BOT TOKEN'
WEB_HOOK_URL = f'{HOST}/webhook'


bot = telebot.TeleBot(BOT_TOKEN)
bot.remove_webhook()
bot.set_webhook(url=WEB_HOOK_URL)


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Howdy, how are you doing?")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)


app = FastAPI()

@app.post("/webhook")
async def webhook_handler(req: Request):
    if req.headers.get('content-type') == 'application/json':
        update = telebot.types.Update.de_json(await req.json())
        bot.process_new_updates([update])
        return
    else:
        return Response(status_code=403)



