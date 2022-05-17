# Praeklima_fassade

## Directory contents 
### Openhab_Config_files: 
Configuration between Openhab and casenio server (responsible for pytotype control) is mentioned in this directory.
### DPU-PYNQ-Overlays: 
This directory has the information about the working flow of Vitis AI for Ultra96 as an Edge device, which includes
1. How to generate custom Deep learning Processing Unit (DPU) for Ultra96?
2. How to train our Machile learning model with respect to DPU (for Ultra96)?
3. How to create overlay for deploying DPU in Processing Logic (PL) and work on our trained machine learning model.
4. You can find some example DPU bit streams and config file.

### Hardware PL: 
This directory has 3 sub directories which are listed below.
Sub directory name | Description
-------------------| -------------
HLS_IPs            | Contains custom IPs designed using Vivado HLS (along with project files to recreate). 
Vivado_designs     | .bin, .hwh and .tcl files for recreating Block diagrams using designed IPs using Vivado
Pynq_overlays      |  Contains the jupytor notebooks to create overlays for each project using .bit and .hwh files.

### Software_files: 
Contains the python scripts 
Contains the python scripts 
Python Script Name        | Description
--------------------------|------------
REST_API_database.py & temporary_csv_generators.py   |	Script to collect sensor data from openhab server using REST-API and data will be stored in the csv files locally.
User_overide_controls.py  | Script to control actuators connected to Openhab using REST API. 
openhab_data_access.py    | Openhab functions to read sensors' data and Send commands to actuators.
openhab_controls.py       | Script to collect sensors' data and control actuators w.r.to the sensors' data .
log_to_csv.py             |	Script to convert Openhab Log files to csv files for collecting sensor data and actuator status (Need to be updated with respect to Openhab items).
Paho_mqtt.py              |	Script to connect to HiveMQ MQTT cloud as a client and post the subscribed sensors data to the respective Openhab items.
actuators_MQTT.py | Script to connect to HiveMQ MQTT cloud as a client and publish commands to the actuators from the Openhab Habpanels.
RBC_accelerator | Rule Based Control algorithm to control prototype. This scripts works based on the Control_Algorithm item on Openhab Habpanel.

### Network Setup: 
contains readme files to describe how to work on Mosquito MQTT and Remote.it and its uses.

