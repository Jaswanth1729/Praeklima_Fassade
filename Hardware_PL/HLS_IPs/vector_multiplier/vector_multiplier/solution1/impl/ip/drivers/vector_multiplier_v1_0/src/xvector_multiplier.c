// ==============================================================
// Vivado(TM) HLS - High-Level Synthesis from C, C++ and SystemC v2019.2 (64-bit)
// Copyright 1986-2019 Xilinx, Inc. All Rights Reserved.
// ==============================================================
/***************************** Include Files *********************************/
#include "xvector_multiplier.h"

/************************** Function Implementation *************************/
#ifndef __linux__
int XVector_multiplier_CfgInitialize(XVector_multiplier *InstancePtr, XVector_multiplier_Config *ConfigPtr) {
    Xil_AssertNonvoid(InstancePtr != NULL);
    Xil_AssertNonvoid(ConfigPtr != NULL);

    InstancePtr->Axilites_BaseAddress = ConfigPtr->Axilites_BaseAddress;
    InstancePtr->IsReady = XIL_COMPONENT_IS_READY;

    return XST_SUCCESS;
}
#endif

void XVector_multiplier_Set_constant_V(XVector_multiplier *InstancePtr, u32 Data) {
    Xil_AssertVoid(InstancePtr != NULL);
    Xil_AssertVoid(InstancePtr->IsReady == XIL_COMPONENT_IS_READY);

    XVector_multiplier_WriteReg(InstancePtr->Axilites_BaseAddress, XVECTOR_MULTIPLIER_AXILITES_ADDR_CONSTANT_V_DATA, Data);
}

u32 XVector_multiplier_Get_constant_V(XVector_multiplier *InstancePtr) {
    u32 Data;

    Xil_AssertNonvoid(InstancePtr != NULL);
    Xil_AssertNonvoid(InstancePtr->IsReady == XIL_COMPONENT_IS_READY);

    Data = XVector_multiplier_ReadReg(InstancePtr->Axilites_BaseAddress, XVECTOR_MULTIPLIER_AXILITES_ADDR_CONSTANT_V_DATA);
    return Data;
}

