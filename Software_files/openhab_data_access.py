import requests
import sys
import pandas
import time
from datetime import datetime


def openhab_read_data(openhab_url, item_name):
    url = openhab_url + item_name + "/state"  # accessing data from items
    res = requests.get(url)
    value = res.text
    # print(value)
    return float(value)


def openhab_read_list_data(openhab_url, items_list):
    output_data = []
    for i in range(0, len(items_list)):
        url = openhab_url + items_list[i] + "/state"  # accessing data from items
        res = requests.get(url)
        value = res.text
        output_data.append(float(value))
    # print(output_data)
    return output_data


def openhab_send_command(openhab_url, item_name, payload):
    url = openhab_url + item_name  # URL to publish or to send command to Wall-Plug  with payload ON
    command = payload
    # print(payload)
    headers = {'Content-type': 'text/plain', 'Accept': 'application/json'}
    status = requests.post(url, headers=headers, data=command)
    status_str = str(status)
    if status_str[len(status_str) - 5:len(status_str) - 2] != "200":
        print(item_name + ": Error status is " + str(status_str))
        return 1
    else:
        print("Command sent successfully")
        return 0


def openhab_send_list_commands(openhab_url, items_list, payload_list):
    for i in range(0, len(items_list)):
        url = openhab_url + items_list[i]  # URL to publish or to send command to Wall-Plug  with payload ON
        command = payload_list[i]
        # print(payload)
        headers = {'Content-type': 'text/plain', 'Accept': 'application/json'}
        status = requests.post(url, headers=headers, data=command)
        status_str = str(status)
        if status_str[len(status_str) - 5:len(status_str) - 2] != "200":
            print(items_list[i] + ": Error status is " + str(status_str))
            return 1
        else:
            print("Command sent successfully")
            return 0


