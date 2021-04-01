# import csv
import pandas

logfile = open("2020-12-02", "rt")
database = pandas.read_csv('database')
print(database)
p = logfile.readlines()
column = ['date', 'time', 'local_weather_timestamp_date', 'local_weather_timestamp_time', 'LocalCurrentTemperature', 'localCurrentApparentTemperature', 'LocalForecastedTemperature_3', 'LocalForecastedApparentTemperature_3', 'LocalForecastedTemperature_6', 'LocalForecastedApparentTemperature_6', 'LocalCurrentHumidity', 'LocalForecastedHumidity_3', 'LocalForecastedHumidity_6', 'localCurrentUVIndexTimestamp_date', 'localCurrentUVIndexTimestamp_time', 'localCurrentUVIndex', 'LocalCurrent_Cloudiness', 'LocalForecastedCloudiness_3', 'LocalForecastedCloudiness_6', 'LocalCurrent_Rain', 'LocalForecastedRain_3', 'LocalForecastedRain_6', 'LocalCurrent_Snow', 'LocalForecastedSnow_3', 'LocalForecastedSnow_6', 'SensorTemperature', 'SensorRelativeHumidity', 'SensorUltraviolet', 'SensorLuminance', 'MotionAlarm', 'TamperAlarm', 'Switch_1', 'WallPlugSwitch_SensorPower_1']
print(len(column))
data = []
last_row_no = len(database)-1
last_row = len(database)
if last_row == 0:
    print("empty database")
    date = "0000-00-00"
    time = "00:00:00"
    local_weather_timestamp_date = "0000-00-00"
    local_weather_timestamp_time = "00:00:00"
    local_Current_Humidity = "0 %"
    Local_Forecasted_Humidity_3 = "0 %"
    Local_Forecasted_Humidity_6 = "0 %"
    WallPlug_Switch_SensorPower_1 = 0
    local_Current_Apparent_Temperature = 0
    local_Current_Temperature = 0
    Local_Forecasted_Temperature_3 = 0
    Local_Forecasted_Temperature_6 = 0
    Local_Forecasted_Apparent_Temperature_3 = 0
    Local_Forecasted_Apparent_Temperature_6 = 0
    switch_1 = "OFF"
    local_Current_UVIndex = 0
    local_Current_UVIndex_Timestamp_date = "0000-00-00"
    local_Current_UVIndex_Timestamp_time = "00:00:00"
    Sensor_Luminance = 0
    Sensor_Ultraviolet = 0
    Sensor_Relative_Humidity = 0
    MotionAlarm = 0
    TamperAlarm = 0
    Sensor_Temperature = 0
    Local_Current_Rain = 0
    Local_Forecasted_Rain_3 = 0
    Local_Forecasted_Rain_6 = 0
    Local_Current_Snow = 0
    Local_Forecasted_Snow_3 = 0
    Local_Forecasted_Snow_6 = 0
    Local_Current_Cloudiness = 0
    Local_Forecasted_Cloudiness_3 = 0
    Local_Forecasted_Cloudiness_6 = 0

else:
    print("in a database")
    date = database.at[last_row_no, 'date']
    time = database.at[last_row_no, 'time']
    local_weather_timestamp_date = database.at[last_row_no, 'local_weather_timestamp_date']
    local_weather_timestamp_time = database.at[last_row_no, 'local_weather_timestamp_time']
    local_Current_Humidity = database.at[last_row_no, 'LocalCurrentHumidity']
    Local_Forecasted_Humidity_3 = database.at[last_row_no, 'LocalForecastedHumidity_3']
    Local_Forecasted_Humidity_6 = database.at[last_row_no, 'LocalForecastedHumidity_6']
    WallPlug_Switch_SensorPower_1 = database.at[last_row_no, 'date']
    local_Current_Apparent_Temperature = database.at[last_row_no, 'localCurrentApparentTemperature']
    local_Current_Temperature = database.at[last_row_no, 'LocalCurrentTemperature']
    Local_Forecasted_Temperature_3 = database.at[last_row_no, 'LocalForecastedTemperature_3']
    Local_Forecasted_Temperature_6 = database.at[last_row_no, 'LocalForecastedTemperature_6']
    Local_Forecasted_Apparent_Temperature_3 = database.at[last_row_no, 'LocalForecastedApparentTemperature_3']
    Local_Forecasted_Apparent_Temperature_6 = database.at[last_row_no, 'LocalForecastedApparentTemperature_6']
    switch_1 = database.at[last_row_no, 'Switch_1']
    local_Current_UVIndex = database.at[last_row_no, 'localCurrentUVIndex']
    local_Current_UVIndex_Timestamp_date = database.at[last_row_no, 'localCurrentUVIndexTimestamp_date']
    local_Current_UVIndex_Timestamp_time = database.at[last_row_no, 'localCurrentUVIndexTimestamp_time']
    Sensor_Luminance = database.at[last_row_no, 'SensorLuminance']
    Sensor_Ultraviolet = database.at[last_row_no, 'SensorUltraviolet']
    Sensor_Relative_Humidity = database.at[last_row_no, 'SensorRelativeHumidity']
    MotionAlarm = database.at[last_row_no, 'MotionAlarm']
    TamperAlarm = database.at[last_row_no, 'TamperAlarm']
    Sensor_Temperature = database.at[last_row_no, 'SensorTemperature']
    Local_Current_Rain = database.at[last_row_no, 'LocalCurrent_Rain']
    Local_Forecasted_Rain_3 = database.at[last_row_no, 'LocalForecastedRain_3']
    Local_Forecasted_Rain_6 = database.at[last_row_no, 'LocalForecastedRain_6']
    Local_Current_Snow = database.at[last_row_no, 'LocalCurrent_Snow']
    Local_Forecasted_Snow_3 = database.at[last_row_no, 'LocalForecastedSnow_3']
    Local_Forecasted_Snow_6 = database.at[last_row_no, 'LocalForecastedSnow_6']
    Local_Current_Cloudiness = database.at[last_row_no, 'LocalCurrent_Cloudiness']
    Local_Forecasted_Cloudiness_3 = database.at[last_row_no, 'LocalForecastedCloudiness_3']
    Local_Forecasted_Cloudiness_6 = database.at[last_row_no, 'LocalForecastedCloudiness_6']

for line in range(0, len(p)):
    print(p[line])
    date = p[line][0:10]
    time = p[line][11:19]
    print(f'{date} {time}')
    if p[line][34:39] == "State":
        if p[line][55:75] == "localLastmeasurement":
            j = 0
            for i in range(75, len(p[line])):
                if p[line][i] + p[line][i + 1] == "to":
                    j = i
                    break
            local_weather_timestamp_date = p[line][j + 3:131]
            local_weather_timestamp_time = p[line][132:140]
            print(local_weather_timestamp_date)
            print(local_weather_timestamp_time)

        elif p[line][55:75] == "localCurrentHumidity":
            j = 0
            for i in range(75, len(p[line])):
                if p[line][i] + p[line][i + 1] == "to":
                    j = i
                    break
            local_Current_Humidity = p[line][j + 3:(len(p[line]) - 1)]
            print(local_Current_Humidity)

        elif p[line][55:80] == "LocalForecastedHumidity_3":
            j = 0
            for i in range(75, len(p[line])):
                if p[line][i] + p[line][i + 1] == "to":
                    j = i
                    break
            Local_Forecasted_Humidity_3 = p[line][j + 3:(len(p[line]) - 1)]
            print(Local_Forecasted_Humidity_3)

        elif p[line][55:80] == "LocalForecastedHumidity_6":
            j = 0
            for i in range(75, len(p[line])):
                if p[line][i] + p[line][i + 1] == "to":
                    j = i
                    break
            Local_Forecasted_Humidity_6 = p[line][j + 3:(len(p[line]) - 1)]
            print(Local_Forecasted_Humidity_6)

        elif p[line][55:78] == "WallPlugSwitch_Switch_1":
            j = 0
            for i in range(82, len(p[line])):
                if p[line][i] + p[line][i + 1] == "to":
                    j = i
                    break
            switch_1 = p[line][j + 3:(len(p[line]) - 1)]
            print(switch_1)

        elif p[line][55:78] == "LocalCurrent_Cloudiness":
            j = 0
            for i in range(80, len(p[line])):
                if p[line][i] + p[line][i + 1] == "to":
                    j = i
                    break
            Local_Current_Cloudiness = p[line][j + 3:(len(p[line]) - 1)]
            print(Local_Current_Cloudiness)

        elif p[line][55:82] == "LocalForecastedCloudiness_3":
            j = 0
            for i in range(82, len(p[line])):
                if p[line][i] + p[line][i + 1] == "to":
                    j = i
                    break
            Local_Forecasted_Cloudiness_3 = p[line][j + 3:(len(p[line]) - 1)]
            print(Local_Forecasted_Cloudiness_3)

        elif p[line][55:82] == "LocalForecastedCloudiness_6":
            j = 0
            for i in range(82, len(p[line])):
                if p[line][i] + p[line][i + 1] == "to":
                    j = i
                    break
            Local_Forecasted_Cloudiness_6 = p[line][j + 3:(len(p[line]) - 1)]
            print(Local_Forecasted_Cloudiness_6)

        elif p[line][55:83] == "WallPlugSwitch_SensorPower_1":
            j = 0
            for i in range(95, len(p[line])):
                if p[line][i] + p[line][i + 1] == "to":
                    j = i
                    break
            WallPlug_Switch_SensorPower_1 = p[line][j + 3:(len(p[line]) - 1)]
            print(WallPlug_Switch_SensorPower_1)

        elif p[line][55:86] == "localCurrentApparentTemperature":
            j = 0
            for i in range(72, len(p[line])):
                if p[line][i] + p[line][i + 1] == "to":
                    j = i
                    break
            local_Current_Apparent_Temperature = p[line][(j + 3):(len(p[line]) - 4)]
            print(local_Current_Apparent_Temperature)

        elif p[line][55:78] == "localCurrentTemperature":
            j = 0
            for i in range(72, len(p[line])):
                if p[line][i] + p[line][i + 1] == "to":
                    j = i
                    break
            local_Current_Temperature = p[line][(j + 3):(len(p[line]) - 4)]
            print(local_Current_Temperature)

        elif p[line][55:91] == "LocalForecastedApparentTemperature_3":
            j = 0
            for i in range(72, len(p[line])):
                if p[line][i] + p[line][i + 1] == "to":
                    j = i
                    break
            Local_Forecasted_Apparent_Temperature_3 = p[line][(j + 3):(len(p[line]) - 4)]
            print(Local_Forecasted_Apparent_Temperature_3)

        elif p[line][55:91] == "LocalForecastedApparentTemperature_6":
            j = 0
            for i in range(72, len(p[line])):
                if p[line][i] + p[line][i + 1] == "to":
                    j = i
                    break
            Local_Forecasted_Apparent_Temperature_6 = p[line][(j + 3):(len(p[line]) - 4)]
            print(Local_Forecasted_Apparent_Temperature_6)

        elif p[line][55:83] == "LocalForecastedTemperature_6":
            j = 0
            for i in range(72, len(p[line])):
                if p[line][i] + p[line][i + 1] == "to":
                    j = i
                    break
            Local_Forecasted_Temperature_6 = p[line][(j + 3):(len(p[line]) - 4)]
            print(Local_Forecasted_Temperature_6)

        elif p[line][55:83] == "LocalForecastedTemperature_3":
            j = 0
            for i in range(72, len(p[line])):
                if p[line][i] + p[line][i + 1] == "to":
                    j = i
                    break
            Local_Forecasted_Temperature_3 = p[line][(j + 3):(len(p[line]) - 4)]
            print(Local_Forecasted_Temperature_3)

        elif p[line][55:72] == "LocalCurrent_Rain":
            j = 0
            for i in range(72, len(p[line])):
                if p[line][i] + p[line][i + 1] == "to":
                    j = i
                    break
            Local_Current_Rain = p[line][(j + 3):(len(p[line]) - 1)]
            print(Local_Current_Rain)

        elif p[line][55:74] == "LocalForecastedRain_3":
            j = 0
            for i in range(72, len(p[line])):
                if p[line][i] + p[line][i + 1] == "to":
                    j = i
                    break
            Local_Forecasted_Rain_3 = p[line][(j + 3):(len(p[line]) - 1)]
            print(Local_Forecasted_Rain_3)

        elif p[line][55:74] == "LocalForecastedRain_6":
            j = 0
            for i in range(72, len(p[line])):
                if p[line][i] + p[line][i + 1] == "to":
                    j = i
                    break
            Local_Forecasted_Rain_6 = p[line][(j + 3):(len(p[line]) - 1)]
            print(Local_Forecasted_Rain_6)

        elif p[line][55:72] == "LocalCurrent_Snow":
            j = 0
            for i in range(72, len(p[line])):
                if p[line][i] + p[line][i + 1] == "to":
                    j = i
                    break
            Local_Current_Snow = p[line][(j + 3):(len(p[line]) - 1)]
            print(Local_Current_Snow)

        elif p[line][55:74] == "LocalForecastedSnow_3":
            j = 0
            for i in range(72, len(p[line])):
                if p[line][i] + p[line][i + 1] == "to":
                    j = i
                    break
            Local_Forecasted_Snow_3 = p[line][(j + 3):(len(p[line]) - 1)]
            print(Local_Forecasted_Snow_3)

        elif p[line][55:74] == "LocalForecastedSnow_6":
            j = 0
            for i in range(72, len(p[line])):
                if p[line][i] + p[line][i + 1] == "to":
                    j = i
                    break
            Local_Forecasted_Snow_6 = p[line][(j + 3):(len(p[line]) - 1)]
            print(Local_Forecasted_Snow_6)

        elif p[line][55:72] == "SensorTemperature":
            j = 0
            for i in range(72, len(p[line])):
                if p[line][i] + p[line][i + 1] == "to":
                    j = i
                    break
            Sensor_Temperature = p[line][(j + 3):(len(p[line]) - 4)]
            print(Sensor_Temperature)

        elif p[line][55:72] == "SensorUltraviolet":
            j = 0
            for i in range(72, len(p[line])):
                if p[line][i] + p[line][i + 1] == "to":
                    j = i
                    break
            Sensor_Ultraviolet = p[line][(j + 3):(len(p[line]) - 1)]
            print(Sensor_Ultraviolet)

        elif p[line][55:77] == "SensorRelativeHumidity":
            j = 0
            for i in range(72, len(p[line])):
                if p[line][i] + p[line][i + 1] == "to":
                    j = i
                    break
            Sensor_Relative_Humidity = p[line][(j + 3):(len(p[line]) - 1)]
            print(Sensor_Relative_Humidity)

        elif p[line][55:70] == "SensorLuminance":
            j = 0
            for i in range(72, len(p[line])):
                if p[line][i] + p[line][i + 1] == "to":
                    j = i
                    break
            Sensor_Luminance = p[line][(j + 3):(len(p[line]) - 1)]
            print(Sensor_Luminance)

        elif p[line][55:66] == "MotionAlarm":
            j = 0
            for i in range(67, len(p[line])):
                if p[line][i] + p[line][i + 1] == "to":
                    j = i
                    break
            MotionAlarm = p[line][(j + 3):(len(p[line]) - 1)]
            print(MotionAlarm)

        elif p[line][55:66] == "TamperAlarm":
            j = 0
            for i in range(67, len(p[line])):
                if p[line][i] + p[line][i + 1] == "to":
                    j = i
                    break
            TamperAlarm = p[line][(j + 3):(len(p[line]) - 1)]
            print(TamperAlarm)

        elif p[line][55:83] == "localCurrentUVIndexTimestamp":
            j = 0
            for i in range(83, len(p[line])):
                if p[line][i] + p[line][i + 1] == "to":
                    j = i
                    break
            local_Current_UVIndex_Timestamp_date = p[line][(j + 3):j + 13]
            local_Current_UVIndex_Timestamp_time = p[line][j + 14:j + 22]
            print(local_Current_UVIndex_Timestamp_date)
            print(local_Current_UVIndex_Timestamp_time)

        elif p[line][55:74] == "localCurrentUVIndex":
            j = 0
            for i in range(67, len(p[line])):
                if p[line][i] + p[line][i + 1] == "to":
                    j = i
                    break
            local_Current_UVIndex = p[line][(j + 3):(len(p[line]) - 1)]
            print(local_Current_UVIndex)

    data.append([date, time, local_weather_timestamp_date, local_weather_timestamp_time, local_Current_Temperature,
                 local_Current_Apparent_Temperature, Local_Forecasted_Temperature_3,
                 Local_Forecasted_Apparent_Temperature_3, Local_Forecasted_Temperature_6,
                 Local_Forecasted_Apparent_Temperature_6, local_Current_Humidity, Local_Forecasted_Humidity_3,
                 Local_Forecasted_Humidity_6, local_Current_UVIndex_Timestamp_date,
                 local_Current_UVIndex_Timestamp_time,
                 local_Current_UVIndex, Local_Current_Cloudiness, Local_Forecasted_Cloudiness_3,
                 Local_Forecasted_Cloudiness_6, Local_Current_Rain, Local_Forecasted_Rain_3, Local_Forecasted_Rain_6,
                 Local_Current_Snow, Local_Forecasted_Snow_3, Local_Forecasted_Snow_6, Sensor_Temperature,
                 Sensor_Relative_Humidity, Sensor_Ultraviolet, Sensor_Luminance, MotionAlarm, TamperAlarm, switch_1,
                 WallPlug_Switch_SensorPower_1])

df = pandas.DataFrame(data, columns=column)
print(df)
print(len(data[2]))
database = database.append(df, ignore_index=True)
print(database)
print(len(database))
database.to_csv('database', index=False)
