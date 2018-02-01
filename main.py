import bot
import stokAPI.yobitAPI
from time import sleep
import bot.botAPI as botAPI

def checkForUpd4ate():
    for val in bot.get_updates_json(bot.url)['result']:
        pair = val['message']['text']
        chat_id = val['message']['chat']['id']
        message_id = val['message']['message_id']
        if botAPI.isInHandleMessage(message_id):
            continue
        else:
            if (val['message']['text'] == "/start"):
                addToHandledMessae(chat_id, message_id)
                bot.send_mess(chat_id, "Привет, введи пару валют, например, btc_usd")
                continue
            else:
                addToHandledMessae(chat_id, message_id)
                try:
                    yobitAPI.getLastPrice(val['message']['text'])
                    bot.send_mess(chat_id, yobitAPI.getLastPrice(pair))
                except:
                    bot.send_mess(chat_id, "пара указана неверно")


