
/home/jaswanth/toolsEDA/Xilinx/Vivado/2019.2/bin/xelab xil_defaultlib.apatb_image_inverter1_top glbl -prj image_inverter1.prj -L smartconnect_v1_0 -L axi_protocol_checker_v1_1_12 -L axi_protocol_checker_v1_1_13 -L axis_protocol_checker_v1_1_11 -L axis_protocol_checker_v1_1_12 -L xil_defaultlib -L unisims_ver -L xpm --initfile "/home/jaswanth/toolsEDA/Xilinx/Vivado/2019.2/data/xsim/ip/xsim_ip.ini" --lib "ieee_proposed=./ieee_proposed" -s image_inverter1 
/home/jaswanth/toolsEDA/Xilinx/Vivado/2019.2/bin/xsim --noieeewarnings image_inverter1 -tclbatch image_inverter1.tcl

