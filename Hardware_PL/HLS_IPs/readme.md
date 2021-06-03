# VIVADO HLS IP are uploaded here

Vivado HLS IPs 	          | Description
--------------------------|------------
adder | Ip to perform addition using AXI_GPIOs 
Openhab_controls    | IP to perform arithmatic and logical operations on FIFO (used to perform comparisions and averaging based on the operation selected)
openhab_controls_bram    | IP to perform arithmatic and logical operations using BRAM (used to perform comparisions and averaging based on the operation selected)
image_inverter	    | Project to invert series of images from colour to Black&white images (using AXI_Stream interface).
image_inverter_block_level_interface	    | Project to invert series of images from colour to Black&white images (using AXI_Stream interface with start and stop pins for controlling IP)
parallel_processing_1 | FIFO addition operation
parallel_processing_2 | FIFO multiplication operation
vector_multiplier   | array Multiplier FIFO using axi_stream interface and a constant using axilite slave interface
OpenCV	| IP for dilation and resizing the image using OpenCV xilinx functions(xf_header.h).
