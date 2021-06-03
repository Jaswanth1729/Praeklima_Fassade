# VIVADO Block designs
use .tcl files to built the Vivado Block designs for the below mentioned projects

Vivado HLS IPs 	          | Description
--------------------------|------------
adder |Block design to perform addition using AXI_GPIOs 
Openhab_controls    | Block design to perform arithmatic and logical operations on FIFO (used to perform comparisions and averaging based on the operation selected)
openhab_controls_bram    | Block design to perform arithmatic and logical operations using BRAM (used to perform comparisions and averaging based on the operation selected)
image_inverter	    | Project to invert series of images from colour to Black&white images (using AXI_Stream interface).
image_inverter_block_level_interface	    | Project to invert series of images from colour to Black&white images (using AXI_Stream interface with start and stop pins for controlling IP)
parallel_processing_1 | Block design which has 2 instantes of FIFO multiplier IP which can work in parallel (testing parallel processing to reduce time to perform multiplication operation).
parallel_processing_1 | Block design which has 3 instantes of FIFO multiplier IP which can work in parallel (testing parallel processing to reduce time to perform multiplication operation).
vector_multiplier   | array Multiplier FIFO
OpenCV	| IP for dilation and resizing the image using OpenCV xilinx functions(xf_header.h).
