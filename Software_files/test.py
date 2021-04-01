import requests
num = 10

# check  and print type of num variable
print(type(num))

# convert the num into string and print
"{}".format(num)
x = str(num - 1)
print(x)
print (type(x))
wait_time = 10
url = "http://192.168.3.1:8080/rest/items/Override_time_slider"  # URL to publish or to send command to Wall-Plug  with payload ON
payload = str(0)
print(payload)
headers = {'Content-type': 'text/plain', 'Accept': 'application/json'}
status = requests.post(url, headers=headers, data=payload)
print(status)

