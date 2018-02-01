import requests
from bot import config
from bot import models
url = "https://api.telegram.org/bot" + config.token + "/"


def get_updates_json(request):
    response = requests.get(request + 'getUpdates')
    return response.json()


def last_update(data):
    results = data['result']
    total_updates = len(results) - 1
    return results[total_updates]


def get_chat_id(update):
    chat_id = update['message']['chat']['id']
    return chat_id


def send_mess(chat, text):
    params = {'chat_id': chat, 'text': text}
    response = requests.post(url + 'sendMessage', params)
    return response

def isInHandleMessage(message_id):
    try:
        message = models.Message.objects.get(id=message_id)
        return True
    except:
        return False