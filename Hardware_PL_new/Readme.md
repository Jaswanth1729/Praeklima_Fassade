# List of projects using PYNQ Overlays and Vivado HLX on Ultra96
Each project has 
1. a jupyter notebook to create overlay and .bit and .hwh files.
2. Vivado HLS IP (designed for the specific project)
3. Vivado HLS block deisgn files (.tcl and other) to recreate the Vivado project.

Check jupyter notebook for understanding of the project and working on PYNQ Overlays. 

Projects 	          | Description
--------------------------|------------
adder | Example project for working on PYNQ overlay it has adder IP which perform addition operation. 
openhab_controls    | collect sensor data from openhab server using REST-API and data will be sent to IP for processing and control actuators 
image_inverter	    | Project to invert series of images from colour to Black&white images.
parallel_processing | It has multiple instantes of FIFO multiplier IP which can work in parallel (testing parallel processing to reduce time to perform multiplication operation).

