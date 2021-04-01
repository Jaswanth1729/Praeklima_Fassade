import requests
import pandas
import time
from datetime import datetime

Sleep_time = 60  # Frequency of data to be collected in seconds
No_of_Data_samples = 60   # No of data samples required with a frequency of Sleep_time
database = pandas.read_csv('REST_API_database', low_memory=False)  # Opening csv file using pandas

# Column names for the database
column = ['date', 'time', 'localCurrentTemperature', 'localCurrentApparentTemperature', 'LocalForecastedTemperature_3',
          'LocalForecastedApparentTemperature_3', 'LocalForecastedTemperature_6',
          'LocalForecastedApparentTemperature_6', 'localCurrentHumidity', 'LocalForecastedHumidity_3',
          'LocalForecastedHumidity_6', 'LocalCurrent_Cloudiness', 'LocalForecastedCloudiness_3',
          'LocalForecastedCloudiness_6', 'localCurrentUVIndex', 'LocalCurrent_Rain', 'LocalForecastedRain_3',
          'LocalForecastedRain_6',
          'LocalCurrent_Snow', 'LocalForecastedSnow_3', 'LocalForecastedSnow_6', 'SensorTemperature',
          'SensorRelativeHumidity', 'SensorUltraviolet', 'SensorLuminance', 'MotionAlarm', 'TamperAlarm',
          'WallPlugSwitch_Switch_1', 'WallPlugSwitch_SensorPower_1','Multisensor_outside_SensorTemperature',
          'Multisensor_outside_SensorRelativeHumidity', 'Multisensor_outside_SensorUltraviolet', 'Multisensor_outside_SensorLuminance',
          'Multisensor_outside_TamperAlarm', 'Multisensor_outside_MotionAlarm']
row_data = []
data = []
count = 0

while True:     # infinite loop
    now = datetime.now()
    row_data = [now.strftime("%Y-%m-%d"), now.strftime("%H:%M:%S")]  # time stamp for data collection
    for i in range(2, len(column)):
        url = "http://192.168.3.1:8080/rest/items/" + column[i] + "/state"  # accessing data from items
        res = requests.get(url)
        value = res.text
        if 1 < i < 8 or i == 21 or i == 29:    # Removing units from the data
            value = value[:len(value) - 4]
        elif 14 < i < 21:
            value = value[:len(value) - 3]
        elif 7 < i < 14:
            value = value[:len(value) - 2]
        row_data.append(value)
    count = count + 1
    data.append(row_data)
    print(row_data)
    time.sleep(Sleep_time)
    print(count)
    if count == No_of_Data_samples:
        count = 0
        print(data)
        df = pandas.DataFrame(data, columns=column)  # Creating a Pandas database for current data
        print(df)
        database = database.append(df, ignore_index=True)  # appending new data to the main REST_API_database
        print(database)
        database.to_csv('REST_API_database', index=False)  # Converting it into csv file
        data = []
        print(data)
# print(data)
# df = pandas.DataFrame(data, columns=column)     # Creating a Pandas database for current data
# print(df)
# database = database.append(df, ignore_index=True)   # appending new data to the main REST_API_database
# print(database)
# database.to_csv('REST_API_database', index=False)   # Converting it into csv file

# # Controlling Wall-plug with respect to Room Temperature(SensorTemperature Item)
#
# url = "http://192.168.3.1:8080/rest/items/SensorTemperature/state"  # URL to get status of RoomTemperature item
# res = requests.get(url)
# temp_data = res.text
# temp_data = temp_data[:len(temp_data) - 4]
# print(temp_data)
# if float(temp_data) > 25:  # condition to check RoomTemperature > 25 degrees
#     url = "http://192.168.3.1:8080/rest/items/WallPlugSwitch_Switch_1"  # URL to publish or to send command to Wall-Plug  with payload OFF
#     payload = "OFF"
#     headers = {'Content-type': 'text/plain', 'Accept': 'application/json'}
#     status = requests.post(url, headers=headers, data=payload)
#     print(status)
# else:
#     url = "http://192.168.3.1:8080/rest/items/WallPlugSwitch_Switch_1"  # URL to publish or to send command to Wall-Plug  with payload ON
#     payload = "ON"
#     headers = {'Content-type': 'text/plain', 'Accept': 'application/json'}
#     status = requests.post(url, headers=headers, data=payload)
#     print(status)
