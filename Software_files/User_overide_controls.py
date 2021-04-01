import requests
import time
from datetime import datetime
# past = datetime.now()
# present = datetime.now()
# print(int(past.strftime("%M")))
count = 0
past_time = 0
wait_time = 0
signal = 0
while True:
    url = "http://192.168.3.1:8080/rest/items/SensorLuminance/state"  # URL to get status of Roomluminance item
    res = requests.get(url)
    Roomluminance = res.text
    #temp_data = Roomluminance[:len(temp_data) - 4]
    # print(Roomluminance)

    url = "http://192.168.3.1:8080/rest/items/LEDControl1_Switch/state"
    res = requests.get(url)
    LED_user_control = res.text
    # print(LED_user_control)

    if float(Roomluminance) > 100:   # condition to check RoomTemperature > 25 degrees
        if LED_user_control == "ON":
            signal = 0
            if count == 0:
                url = "http://192.168.3.1:8080/rest/items/WallPlugSwitch_Switch_1"  # URL to publish or to send command to Wall-Plug  with payload ON
                payload = "ON"
                # print(payload)
                headers = {'Content-type': 'text/plain', 'Accept': 'application/json'}
                status = requests.post(url, headers=headers, data=payload)
                print("Switch1 set to ON : " + str(status))
                count += 1

                url = "http://192.168.3.1:8080/rest/items/Override_time_slider/state"  # URL to get status of RoomTemperature item
                res = requests.get(url)
                wait_time = int(res.text)
                print("wait time is : " + str(wait_time))
                print('.', end='', flush=True)
            else:

                if count == 60:
                    count = 0
                    url = "http://192.168.3.1:8080/rest/items/Override_time_slider"  # URL to publish or to send command to Wall-Plug  with payload ON
                    payload = str(wait_time - 1)

                    headers = {'Content-type': 'text/plain', 'Accept': 'application/json'}
                    status = requests.post(url, headers=headers, data=payload)
                    print('Override time slider : ' + str(payload) + "  " + str(status))
                count += 1
                print('.', end='', flush=True)
                url = "http://192.168.3.1:8080/rest/items/Override_time_slider/state"  # URL to get status of RoomTemperature item
                res = requests.get(url)
                wait_time = int(res.text)
                if wait_time == 0:
                    count = 0
                    url = "http://192.168.3.1:8080/rest/items/WallPlugSwitch_Switch_1"  # URL to publish or to send command to Wall-Plug  with payload OFF
                    payload = "OFF"
                    # print(payload)
                    headers = {'Content-type': 'text/plain', 'Accept': 'application/json'}
                    status = requests.post(url, headers=headers, data=payload)
                    print("Switch 1 set to OFF : " + str(status))
                    url = "http://192.168.3.1:8080/rest/items/LEDControl1_Switch"  # URL to publish or to send command to Wall-Plug  with payload OFF
                    payload = "OFF"
                    # print(payload)
                    headers = {'Content-type': 'text/plain', 'Accept': 'application/json'}
                    status = requests.post(url, headers=headers, data=payload)
                    print("LED_switch1 set to OFF : " + str(status))
                    url = "http://192.168.3.1:8080/rest/items/Override_time_slider"  # URL to publish or to send command to Wall-Plug  with payload ON
                    payload = '0'
                    headers = {'Content-type': 'text/plain', 'Accept': 'application/json'}
                    status = requests.post(url, headers=headers, data=payload)
                    print('Override time slider : ' + str(payload) + "  " + str(status))
        else:
            count = 0
            url = "http://192.168.3.1:8080/rest/items/WallPlugSwitch_Switch_1/state"  # URL to get status of RoomTemperature item
            res = requests.get(url)
            LED_user_control = res.text
            # print(LED_user_control)
            if LED_user_control == "OFF":

                if signal != 1:
                    print("already off : do nothing")
                    signal = 1
            else:
                signal = 0
                url = "http://192.168.3.1:8080/rest/items/WallPlugSwitch_Switch_1"  # URL to publish or to send command to Wall-Plug  with payload OFF
                payload = "OFF"
                # print(payload)
                headers = {'Content-type': 'text/plain', 'Accept': 'application/json'}
                status = requests.post(url, headers=headers, data=payload)
                print(status)
                url = "http://192.168.3.1:8080/rest/items/LEDControl1_Switch"  # URL to publish or to send command to Wall-Plug  with payload OFF
                payload = "OFF"
                # print(payload)
                headers = {'Content-type': 'text/plain', 'Accept': 'application/json'}
                status = requests.post(url, headers=headers, data=payload)
                print(status)
    else:
        if LED_user_control == "OFF":
            signal = 0
            if count == 0:
                url = "http://192.168.3.1:8080/rest/items/WallPlugSwitch_Switch_1"  # URL to publish or to send command to Wall-Plug  with payload ON
                payload = "OFF"
                # print(payload)
                headers = {'Content-type': 'text/plain', 'Accept': 'application/json'}
                status = requests.post(url, headers=headers, data=payload)
                print(status)
                count += 1
                url = "http://192.168.3.1:8080/rest/items/Override_time_slider/state"  # URL to get status of RoomTemperature item
                res = requests.get(url)
                wait_time = int(res.text)
                print("wait time is : " + str(wait_time))
                print('.', end='', flush=True)
            else:

                # present = datetime.now()
                # present_time = int(present.strftime("%M"))
                # print(present_time)
                if count == 60:
                    count = 0
                    url = "http://192.168.3.1:8080/rest/items/Override_time_slider"  # URL to publish or to send command to Wall-Plug  with payload ON
                    payload = str(wait_time - 1)
                    headers = {'Content-type': 'text/plain', 'Accept': 'application/json'}
                    status = requests.post(url, headers=headers, data=payload)
                    print('Override time slider : ' + str(payload) + "  " + str(status))
                count += 1
                print('.', end='', flush=True)
                url = "http://192.168.3.1:8080/rest/items/Override_time_slider/state"  # URL to get status of RoomTemperature item
                res = requests.get(url)
                wait_time = int(res.text)
                if wait_time == 0:
                    count = 0
                    url = "http://192.168.3.1:8080/rest/items/WallPlugSwitch_Switch_1"  # URL to publish or to send command to Wall-Plug  with payload OFF
                    payload = "ON"
                    # print(payload + "for switch1")
                    headers = {'Content-type': 'text/plain', 'Accept': 'application/json'}
                    status = requests.post(url, headers=headers, data=payload)
                    print("Switch1 set to ON : " + str(status))
                    url = "http://192.168.3.1:8080/rest/items/LEDControl1_Switch"  # URL to publish or to send command to Wall-Plug  with payload OFF
                    payload = "ON"
                    # print(payload + "for LEDSwitch")
                    headers = {'Content-type': 'text/plain', 'Accept': 'application/json'}
                    status = requests.post(url, headers=headers, data=payload)
                    print("LEDSwitch set to ON : " + str(status))
                    url = "http://192.168.3.1:8080/rest/items/Override_time_slider"  # URL to publish or to send command to Wall-Plug  with payload ON
                    payload = '0'
                    headers = {'Content-type': 'text/plain', 'Accept': 'application/json'}
                    status = requests.post(url, headers=headers, data=payload)
                    print('Override time slider : ' + str(payload) + "  " + str(status))
        else:
            count = 0
            url = "http://192.168.3.1:8080/rest/items/WallPlugSwitch_Switch_1/state"  # URL to get status of RoomTemperature item
            res = requests.get(url)
            LED_user_control = res.text
            # print(LED_user_control)
            if LED_user_control == "ON":

                if signal != 1:
                    print("already ON : do nothing")
                    signal = 1
            else:
                signal = 0
                url = "http://192.168.3.1:8080/rest/items/WallPlugSwitch_Switch_1"  # URL to publish or to send command to Wall-Plug  with payload ON
                payload = "ON"
                # print(payload)
                headers = {'Content-type': 'text/plain', 'Accept': 'application/json'}
                status = requests.post(url, headers=headers, data=payload)
                print("Switch1 set to ON : " + str(status))
                url = "http://192.168.3.1:8080/rest/items/LEDControl1_Switch"  # URL to publish or to send command to Wall-Plug  with payload OFF
                payload = "ON"
                # print(payload)
                headers = {'Content-type': 'text/plain', 'Accept': 'application/json'}
                status = requests.post(url, headers=headers, data=payload)
                print("LEDSwitch1 set to ON : " + str(status))
    time.sleep(1)


