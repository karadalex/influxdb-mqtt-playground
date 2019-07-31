import paho.mqtt.client as mqtt
import random
import time
import json
import pprint


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

# publish messages
price = 9500.50
while True:
    priceChange = random.randint(-50, 50)
    price = price + priceChange
    dict_msg = {
        "symbol": "BTC",
        "price": price,
    }
    msg = json.dumps(dict_msg)
    ret = client.publish("crypto/btc", msg)
    print(msg)
    time.sleep(5)