import sys

import paho.mqtt.client as mqtt
import time
from queue import Queue

q = Queue()
messages = []


def on_connect(client, userdata, flags, rc):
    if rc == 0:
        client.connected_flag = True  # set flag
        print("connected OK")
    else:
        print("Bad connection Returned code=", rc)
        client.bad_connection_flag = True


def on_message(client1, userdata, message):
    # global messages
    m = "message received  ", str(message.payload.decode("utf-8"))
    n = str(message.payload.decode("utf-8"))
    print(n, type(n))
    messages.append(m)  # put messages in list
    q.put(m)  # put messages on queue
    print("message received  ", m)


def on_publish(client, userdata, mid):
    global messages
    m = "on publish callback mid " + str(mid)
    # messages.append(m)


def on_subscribe(client, userdata, mid, granted_qos):
    m = "on_subscribe callback mid " + str(mid)


def on_disconnect(client, userdata, rc=0):
    print("DisConnected result code " + str(rc))
    client.loop_stop()


mqtt.Client.connected_flag = False  # create flag in class
mqtt.Client.bad_connection_flag = False
QOS = 0
broker = "192.168.209.215"
port = 8883
client = mqtt.Client("system1")  # create new instance
client.on_connect = on_connect  # bind call back function
client.on_message = on_message  # attach function to callback
client.on_publish = on_publish  # attach function to callback
client.on_subscribe = on_subscribe  # attach function to callback
time.sleep(1)
client.username_pw_set(username="praeklima", password="praeklima")

client.loop_start()
print("Connecting to broker ", broker)
client.connect(broker, port)  # connect to broker
# try:
#     client.connect(broker, port)  # connect to broker
# except:
#     print("connection failed")
#     exit(1)


while not client.connected_flag and not client.bad_connection_flag:  # wait in loop
    print("In wait loop")
    time.sleep(0.1)

if client.bad_connection_flag:
    client.loop_stop()  # Stop loop
    sys.exit()
print("in Main Loop")
client.publish("test", "ON")
print("Subscribing to topic", "sub_test")
client.subscribe("sub_test", QOS)

# while len(messages)>0:
#     print(messages.pop(0))
#
# while not q.empty():
#     message = q.get()
#     print("queue: ",message)

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    print("exiting")
    client.disconnect()  # disconnect
    client.loop_stop()  # Stop loop
