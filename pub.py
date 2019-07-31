import paho.mqtt.client as mqtt
import random
import time
import json
import pprint
import requests


broker = "localhost"
port = 1883

# publish callback function
def on_publish(client, userdata, result):
    print("data published \n")
    pass

# create client object and connect
client = mqtt.Client()
client.username_pw_set("rabbitmq", password='rabbitmq')
client.connect(broker, port, 45)

# assign publish callback function
client.on_publish = on_publish

url = "https://min-api.cryptocompare.com/data/price"
querystring = {"fsym":"BTC","tsyms":"USD,EUR"}
# publish messages
while True:
    payload = ""
    headers = {}
    response = requests.request("GET", url, data=payload, headers=headers, params=querystring)
    print(response.text)
    btcJson = json.loads(response.text)
    btcPrice = btcJson["USD"]
    dict_msg = {
        "symbol": "BTC",
        "price": btcPrice,
    }
    msg = json.dumps(dict_msg)
    ret = client.publish("crypto/btc", msg)
    print(msg)
    time.sleep(5)