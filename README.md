# Praeklima_fassade

## Directory contents 
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
1. REST_API_database.py: 	Script to collect sensor data from openhab server using REST-API and data will be stored in the csv files locally.
2. User_overide_controls.py: 	Script to control actuators connected to Openhab using REST API. 
3. log_to_csv.py:		Script to convert Openhab Log files to csv files for collecting sensor data and actuator status (Need to be updated with respect to Openhab items).
4. Paho_mqtt.py:		Script to connect to HiveMQ MQTT cloud as a client and post the subscribed sensors data to the respective Openhab items.

### Network Setup: 
contains readme files to describe how to work on Mosquito MQTT and Remote.it and its uses.

 Markup : 1. A numbered list
              1. A nested numbered list
              2. Which is numbered
          2. Which is numbered
