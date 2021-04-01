// ==============================================================
// Vivado(TM) HLS - High-Level Synthesis from C, C++ and SystemC v2019.2 (64-bit)
// Copyright 1986-2019 Xilinx, Inc. All Rights Reserved.
// ==============================================================

extern void AESL_WRAP_openhab_controls (
hls::stream<struct ap_axiu<32, 1, 1, 1 > > (&inStream),
hls::stream<struct ap_axiu<32, 1, 1, 1 > > (&outStream),
ap_fixed<32, 16, (ap_q_mode) 0, (ap_o_mode)3, 0> thresholds[50],
ap_fixed<32, 16, (ap_q_mode) 0, (ap_o_mode)3, 0> outData[50]);
