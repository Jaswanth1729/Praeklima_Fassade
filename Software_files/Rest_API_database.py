import requests
import sys
import pandas
import time
from datetime import datetime
import openhab_data_access

Sleep_time = 30  # Frequency of data to be collected in seconds
No_of_Data_samples = 30  # No of data samples required with a frequency of Sleep_time
database = pandas.read_csv('~/Work/pycharm_projects/REST_API_database_2', low_memory=False)
# Opening csv file using pandas

print("working")

# openhab cloud REST API URL syntax https://<user_emailid>:<password>@home.myopenhab.org/rest/items
cloud_api_url = "https://praeklima.tud%40gmail.com:praeklima_tud@2021@home.myopenhab.org/rest/items/"
localhost_url = "http://192.168.3.1:8080/rest/items/"
# Column names for the database
# column = ['date', 'time', 'localCurrentTemperature', 'localCurrentApparentTemperature', 'LocalForecastedTemperature_3',
#           'LocalForecastedApparentTemperature_3', 'LocalForecastedTemperature_6',
#           'LocalForecastedApparentTemperature_6', 'localCurrentHumidity', 'LocalForecastedHumidity_3',
#           'LocalForecastedHumidity_6', 'LocalCurrent_Cloudiness', 'LocalForecastedCloudiness_3',
#           'LocalForecastedCloudiness_6', 'localCurrentUVIndex', 'LocalCurrent_Rain', 'LocalForecastedRain_3',
#           'LocalForecastedRain_6',
#           'LocalCurrent_Snow', 'LocalForecastedSnow_3', 'LocalForecastedSnow_6', 'SensorTemperature',
#           'SensorRelativeHumidity', 'SensorUltraviolet', 'SensorLuminance', 'MotionAlarm', 'TamperAlarm',
#           'WallPlugSwitch_Switch_1', 'WallPlugSwitch_SensorPower_1', 'Multisensor_outside_SensorTemperature',
#           'Multisensor_outside_SensorRelativeHumidity', 'Multisensor_outside_SensorUltraviolet',
#           'Multisensor_outside_SensorLuminance',
#           'Multisensor_outside_TamperAlarm', 'Multisensor_outside_MotionAlarm', 'sensor1_temperature',
#           'sensor2_temperature', 'sensor3_temperature', 'sensor4_temperature', 'sensor5_temperature',
#           'sensor1_humidity', 'sensor2_humidity', 'sensor3_humidity', 'sensor4_humidity', 'sensor5_humidity']

column = ['date', 'time', 'localCurrentTemperature', 'localCurrentApparentTemperature', 'LocalForecastedTemperature_3',
          'LocalForecastedApparentTemperature_3', 'LocalForecastedTemperature_6',
          'LocalForecastedApparentTemperature_6', 'localCurrentHumidity', 'LocalForecastedHumidity_3',
          'LocalForecastedHumidity_6', 'LocalCurrent_Cloudiness', 'LocalForecastedCloudiness_3',
          'LocalForecastedCloudiness_6', 'localCurrentUVIndex', 'LocalCurrent_Rain', 'LocalForecastedRain_3',
          'LocalForecastedRain_6',
          'LocalCurrent_Snow', 'LocalForecastedSnow_3', 'LocalForecastedSnow_6', 'SensorTemperature',
          'SensorRelativeHumidity', 'SensorUltraviolet', 'SensorLuminance', 'MotionAlarm', 'TamperAlarm',
          'WallPlugSwitch1_Switch_1', 'WallPlugSwitch1_SensorPower_1','Multisensor_outside_SensorTemperature',
          'Multisensor_outside_SensorRelativeHumidity', 'Multisensor_outside_SensorUltraviolet', 'Multisensor_outside_SensorLuminance',
          'Multisensor_outside_TamperAlarm', 'Multisensor_outside_MotionAlarm']

row_data = []
data = []
count = 0

openhab_data_access.openhab_read_data(localhost_url, column[22])

while True:  # infinite loop
    now = datetime.now()
    row_data = [now.strftime("%Y-%m-%d"), now.strftime("%H:%M:%S")]  # time stamp for data collection
    for i in range(2, len(column)):
        value = openhab_data_access.openhab_read_data(localhost_url, column[i])
        if 1 < i < 8 or i == 21 or i == 29:  # Removing units from the data
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
    #     print(count)
    sys.stdout.write("\r")
    print(count, end='', flush=True)
    if count == No_of_Data_samples:
        time.sleep(1)
        sys.stdout.write("\r")
        count = 0
        #         print(data)
        df = pandas.DataFrame(data, columns=column)  # Creating a Pandas database for current data
        #         print(df)
        database = database.append(df, ignore_index=True)  # appending new data to the main REST_API_database
        #         print(database)
        database.to_csv('~/Work/pycharm_projects/REST_API_database_2', index=False)  # Converting it into csv file
        data = []

