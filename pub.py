import paho.mqtt.client as mqtt
import random
import time


broker = "localhost"
port = 1883

# publish callback function
def on_publish(client, userdata, result):
    print("data published \n")
    pass

# create client object and connect
client = mqtt.Client()
client.username_pw_set("rabbitmq", password='rabbitmq')
client.connect(broker,port)

# assign publish callback function
client.on_publish = on_publish

# publish messages
price = 9500
while True:
    priceChange = random.randint(-50, 50)
    ret = client.publish("crypto/btc", price + priceChange)
    time.sleep(5)