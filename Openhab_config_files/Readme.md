# Fassade Setup
![Fassade to Openhab data communication](images/logo.jpeg)

Fassade to Openhab communication has 3 main blocks 
1. Casenio System
		Sensors and actuators are connected to this Casenio system via Z-wave and MQTT.
		Casenio Systems uses MQTT to transmit data to HiveMQ cloud broker 
2. Paho MQTT [python script ](https://github.com/Jaswanth1729/Praeklima_fassade/blob/main/Software_files/paho_mqtt.py)
		Using Paho_mqtt python library we create a client to HiveMQ MQTT cloud broker/server and publish/subscribe the sensors/actuators data.
		Sensors and Actuators data will be sent to Openhab server(running in Rasberry Pi) using Openhab Cloud's Rest-API.

3. Openhab server:
		We can control/visualize the sensors and actuator status using  Openhab's Habpanel/PaperUI. 	

Email ID for Openhab cloud service, remote.it, open weather api, HiveMQ services are 
ID 		|	praeklima.tud@gmail.com
password	|	praeklima_tud@2021
