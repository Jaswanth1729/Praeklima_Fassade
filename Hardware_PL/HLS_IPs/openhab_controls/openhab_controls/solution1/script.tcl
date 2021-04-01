############################################################
## This file is generated automatically by Vivado HLS.
## Please DO NOT edit it.
## Copyright (C) 1986-2019 Xilinx, Inc. All Rights Reserved.
############################################################
open_project openhab_controls
set_top openhab_controls
add_files core.cpp
add_files -tb tb_core.cpp -cflags "-Wno-unknown-pragmas" -csimflags "-Wno-unknown-pragmas"
open_solution "solution1"
set_part {xczu3eg-sbva484-1-e}
create_clock -period 10 -name default
config_export -format ip_catalog -rtl verilog
#source "./openhab_controls/solution1/directives.tcl"
csim_design -clean -O
csynth_design
cosim_design
export_design -rtl verilog -format ip_catalog
