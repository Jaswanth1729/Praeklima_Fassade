import openhab_data_access # openhab functions to read and write
import time

# openhab urls openhab cloud url(cloud_api_url) and openhab server on the device(localhost_url).
cloud_api_url = "https://praeklima.tud%40gmail.com:praeklima_tud@2021@home.myopenhab.org/rest/items/"
localhost_url = "http://192.168.3.1:8080/rest/items/"

# Frequency of data to be collected in seconds
Sleep_time = 3
# No of data samples required which means after every No_of_data_samples*Sleep_time secs actuator command will be sent
No_of_Data_samples = 6

# list of openhab sensor items
temperature_items = ['sensor1_temperature', 'sensor2_temperature', 'sensor3_temperature', 'sensor4_temperature',
                     'sensor5_temperature']
count = 0
avg_data = []
while 1:
    sensor_data = openhab_data_access.openhab_read_list_data(cloud_api_url, temperature_items)
    avg_data.append(sum(sensor_data)/len(sensor_data))
    count = count + 1
    if count == No_of_Data_samples:
        count = 0
        whole_average = sum(avg_data)/len(avg_data)
        print(whole_average)
        if whole_average < 27:
            openhab_data_access.openhab_send_command(cloud_api_url, "WallPlugSwitch1_Switch_1", "ON")
        else:
            openhab_data_access.openhab_send_command(cloud_api_url, "WallPlugSwitch1_Switch_1", "OFF")
        avg_data = []
    time.sleep(Sleep_time)