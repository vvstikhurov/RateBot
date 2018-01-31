import requests
yobitUrltrades="https://yobit.net/api/3/trades/"

def getTradeInfo(pair):
    yobitUrltrades="https://yobit.net/api/3/trades/"+pair
    response = requests.get(yobitUrltrades)
    return response.json()
def getLastPrice(pair):
    return getTradeInfo(pair.lower())[pair.lower()][0]['price']