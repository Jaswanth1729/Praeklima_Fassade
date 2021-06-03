import paho.mqtt.client as mqtt
import requests
import time
from datetime import datetime

#Dictonary of MQTT Feeds/topics, add the topics of the broker in this Dictonary
column = ['topic/LEDControl1_Switch', 
          'casenio/event/89490200001132903918/7/1/JSON', 'casenio/event/89490200001132903918/8/1/JSON','casenio/event/89490200001132903918/9/1/JSON',
          'casenio/event/89490200001132903918/10/1/JSON', 'casenio/event/89490200001132903918/11/1/JSON', 
          'casenio/event/89490200001132903918/7/5/JSON', 'casenio/event/89490200001132903918/8/5/JSON','casenio/event/89490200001132903918/9/5/JSON',
          'casenio/event/89490200001132903918/10/5/JSON', 'casenio/event/89490200001132903918/11/5/JSON']
#Openhab items, where the MQTT topics data is to be stored on Openhab items, "place the list in the same order as MQTT topics"
openhab_item_names = ['LEDControl1_Switch', 'sensor1_temperature', 'sensor2_temperature','sensor3_temperature','sensor4_temperature','sensor5_temperature',
                     'sensor1_humidity', 'sensor2_humidity', 'sensor3_humidity', 'sensor4_humidity', 'sensor5_humidity']

print("PAHO_MQTT")
# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected successfully")
    else:
        print("Connect returned result code: " + str(rc))
payload = 0
# The callback for when a PUBLISH message is received from the server.
# Callback Definition: subscribed topics data will be received and will commit that data to the respective openhab item
def on_message(client, userdata, msg):
    print("Received message: " + msg.topic + " -> " + msg.payload.decode("utf-8"))
    for i in range(len(column)):
        if(msg.topic == column[i]):
            payload_received = msg.payload.decode("utf-8")
            payload = payload_received[7:11]
            url = "http://192.168.3.1:8080/rest/items/" + openhab_item_names[i]  # URL to publish or to send command to Wall-Plug  with payload OFF
            # print(payload + "for LEDSwitch")
            headers = {'Content-type': 'text/plain', 'Accept': 'application/json'}
            status = requests.post(url, headers=headers, data=payload)
#             print(openhab_item_names[i] +" set to " + payload +": " + str(status))
            status_str = str(status)
            if(status_str[len(status_str) -5 :len(status_str) -2] != "200"):
                print("Error status is " + str(status_str))
                
                
                    

# create the client
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

# enable TLS
client.tls_set(tls_version=mqtt.ssl.PROTOCOL_TLS)

# set username and password
client.username_pw_set("praeklima", "Praeklima2021")

# connect to HiveMQ Cloud on port 8883
client.connect("fb06b8022fb941089214e0f7b7025453.s1.eu.hivemq.cloud", 8883) #client.connect(<MQTT ip address/hostname>, <port number>)  

# subscribe to the topics
for i in range(len(column)):
    client.subscribe(column[i])

# publish Data to the topic "my/LEDControl1_Switch"
client.publish("topic/LEDControl1_Switch", "OFF")

# Blocking call that processes network traffic, dispatches callbacks and handles reconnecting.
client.loop_forever()
