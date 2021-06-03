set moduleName openhab_controls_bram
set isTopModule 1
set isTaskLevelControl 1
set isCombinational 0
set isDatapathOnly 0
set isFreeRunPipelineModule 0
set isPipelined 0
set pipeline_type none
set FunctionProtocol ap_ctrl_hs
set isOneStateSeq 0
set ProfileFlag 0
set StallSigGenFlag 0
set isEnableWaveformDebug 1
set C_modelName {openhab_controls_bram}
set C_modelType { void 0 }
set C_modelArgList {
	{ inputData_V int 32 regular {bram 10 { 1 3 } 1 1 }  }
	{ thresholds_V int 32 regular {bram 10 { 1 3 } 1 1 }  }
	{ outData int 32 regular {bram 10 { 0 3 } 0 1 }  }
}
set C_modelArgMapList {[ 
	{ "Name" : "inputData_V", "interface" : "bram", "bitwidth" : 32, "direction" : "READONLY", "bitSlice":[{"low":0,"up":31,"cElement": [{"cName": "inputData.V","cData": "int32","bit_use": { "low": 0,"up": 31},"cArray": [{"low" : 0,"up" : 9,"step" : 1}]}]}]} , 
 	{ "Name" : "thresholds_V", "interface" : "bram", "bitwidth" : 32, "direction" : "READONLY", "bitSlice":[{"low":0,"up":31,"cElement": [{"cName": "thresholds.V","cData": "int32","bit_use": { "low": 0,"up": 31},"cArray": [{"low" : 0,"up" : 9,"step" : 1}]}]}]} , 
 	{ "Name" : "outData", "interface" : "bram", "bitwidth" : 32, "direction" : "WRITEONLY", "bitSlice":[{"low":0,"up":31,"cElement": [{"cName": "outData","cData": "int","bit_use": { "low": 0,"up": 31},"cArray": [{"low" : 0,"up" : 9,"step" : 1}]}]}]} ]}
# RTL Port declarations: 
set portNum 27
set portList { 
	{ ap_clk sc_in sc_logic 1 clock -1 } 
	{ ap_rst sc_in sc_logic 1 reset -1 active_high_sync } 
	{ ap_start sc_in sc_logic 1 start -1 } 
	{ ap_done sc_out sc_logic 1 predone -1 } 
	{ ap_idle sc_out sc_logic 1 done -1 } 
	{ ap_ready sc_out sc_logic 1 ready -1 } 
	{ inputData_V_Addr_A sc_out sc_lv 32 signal 0 } 
	{ inputData_V_EN_A sc_out sc_logic 1 signal 0 } 
	{ inputData_V_WEN_A sc_out sc_lv 4 signal 0 } 
	{ inputData_V_Din_A sc_out sc_lv 32 signal 0 } 
	{ inputData_V_Dout_A sc_in sc_lv 32 signal 0 } 
	{ inputData_V_Clk_A sc_out sc_logic 1 signal 0 } 
	{ inputData_V_Rst_A sc_out sc_logic 1 signal 0 } 
	{ thresholds_V_Addr_A sc_out sc_lv 32 signal 1 } 
	{ thresholds_V_EN_A sc_out sc_logic 1 signal 1 } 
	{ thresholds_V_WEN_A sc_out sc_lv 4 signal 1 } 
	{ thresholds_V_Din_A sc_out sc_lv 32 signal 1 } 
	{ thresholds_V_Dout_A sc_in sc_lv 32 signal 1 } 
	{ thresholds_V_Clk_A sc_out sc_logic 1 signal 1 } 
	{ thresholds_V_Rst_A sc_out sc_logic 1 signal 1 } 
	{ outData_Addr_A sc_out sc_lv 32 signal 2 } 
	{ outData_EN_A sc_out sc_logic 1 signal 2 } 
	{ outData_WEN_A sc_out sc_lv 4 signal 2 } 
	{ outData_Din_A sc_out sc_lv 32 signal 2 } 
	{ outData_Dout_A sc_in sc_lv 32 signal 2 } 
	{ outData_Clk_A sc_out sc_logic 1 signal 2 } 
	{ outData_Rst_A sc_out sc_logic 1 signal 2 } 
}
set NewPortList {[ 
	{ "name": "ap_clk", "direction": "in", "datatype": "sc_logic", "bitwidth":1, "type": "clock", "bundle":{"name": "ap_clk", "role": "default" }} , 
 	{ "name": "ap_rst", "direction": "in", "datatype": "sc_logic", "bitwidth":1, "type": "reset", "bundle":{"name": "ap_rst", "role": "default" }} , 
 	{ "name": "ap_start", "direction": "in", "datatype": "sc_logic", "bitwidth":1, "type": "start", "bundle":{"name": "ap_start", "role": "default" }} , 
 	{ "name": "ap_done", "direction": "out", "datatype": "sc_logic", "bitwidth":1, "type": "predone", "bundle":{"name": "ap_done", "role": "default" }} , 
 	{ "name": "ap_idle", "direction": "out", "datatype": "sc_logic", "bitwidth":1, "type": "done", "bundle":{"name": "ap_idle", "role": "default" }} , 
 	{ "name": "ap_ready", "direction": "out", "datatype": "sc_logic", "bitwidth":1, "type": "ready", "bundle":{"name": "ap_ready", "role": "default" }} , 
 	{ "name": "inputData_V_Addr_A", "direction": "out", "datatype": "sc_lv", "bitwidth":32, "type": "signal", "bundle":{"name": "inputData_V", "role": "Addr_A" }} , 
 	{ "name": "inputData_V_EN_A", "direction": "out", "datatype": "sc_logic", "bitwidth":1, "type": "signal", "bundle":{"name": "inputData_V", "role": "EN_A" }} , 
 	{ "name": "inputData_V_WEN_A", "direction": "out", "datatype": "sc_lv", "bitwidth":4, "type": "signal", "bundle":{"name": "inputData_V", "role": "WEN_A" }} , 
 	{ "name": "inputData_V_Din_A", "direction": "out", "datatype": "sc_lv", "bitwidth":32, "type": "signal", "bundle":{"name": "inputData_V", "role": "Din_A" }} , 
 	{ "name": "inputData_V_Dout_A", "direction": "in", "datatype": "sc_lv", "bitwidth":32, "type": "signal", "bundle":{"name": "inputData_V", "role": "Dout_A" }} , 
 	{ "name": "inputData_V_Clk_A", "direction": "out", "datatype": "sc_logic", "bitwidth":1, "type": "signal", "bundle":{"name": "inputData_V", "role": "Clk_A" }} , 
 	{ "name": "inputData_V_Rst_A", "direction": "out", "datatype": "sc_logic", "bitwidth":1, "type": "signal", "bundle":{"name": "inputData_V", "role": "Rst_A" }} , 
 	{ "name": "thresholds_V_Addr_A", "direction": "out", "datatype": "sc_lv", "bitwidth":32, "type": "signal", "bundle":{"name": "thresholds_V", "role": "Addr_A" }} , 
 	{ "name": "thresholds_V_EN_A", "direction": "out", "datatype": "sc_logic", "bitwidth":1, "type": "signal", "bundle":{"name": "thresholds_V", "role": "EN_A" }} , 
 	{ "name": "thresholds_V_WEN_A", "direction": "out", "datatype": "sc_lv", "bitwidth":4, "type": "signal", "bundle":{"name": "thresholds_V", "role": "WEN_A" }} , 
 	{ "name": "thresholds_V_Din_A", "direction": "out", "datatype": "sc_lv", "bitwidth":32, "type": "signal", "bundle":{"name": "thresholds_V", "role": "Din_A" }} , 
 	{ "name": "thresholds_V_Dout_A", "direction": "in", "datatype": "sc_lv", "bitwidth":32, "type": "signal", "bundle":{"name": "thresholds_V", "role": "Dout_A" }} , 
 	{ "name": "thresholds_V_Clk_A", "direction": "out", "datatype": "sc_logic", "bitwidth":1, "type": "signal", "bundle":{"name": "thresholds_V", "role": "Clk_A" }} , 
 	{ "name": "thresholds_V_Rst_A", "direction": "out", "datatype": "sc_logic", "bitwidth":1, "type": "signal", "bundle":{"name": "thresholds_V", "role": "Rst_A" }} , 
 	{ "name": "outData_Addr_A", "direction": "out", "datatype": "sc_lv", "bitwidth":32, "type": "signal", "bundle":{"name": "outData", "role": "Addr_A" }} , 
 	{ "name": "outData_EN_A", "direction": "out", "datatype": "sc_logic", "bitwidth":1, "type": "signal", "bundle":{"name": "outData", "role": "EN_A" }} , 
 	{ "name": "outData_WEN_A", "direction": "out", "datatype": "sc_lv", "bitwidth":4, "type": "signal", "bundle":{"name": "outData", "role": "WEN_A" }} , 
 	{ "name": "outData_Din_A", "direction": "out", "datatype": "sc_lv", "bitwidth":32, "type": "signal", "bundle":{"name": "outData", "role": "Din_A" }} , 
 	{ "name": "outData_Dout_A", "direction": "in", "datatype": "sc_lv", "bitwidth":32, "type": "signal", "bundle":{"name": "outData", "role": "Dout_A" }} , 
 	{ "name": "outData_Clk_A", "direction": "out", "datatype": "sc_logic", "bitwidth":1, "type": "signal", "bundle":{"name": "outData", "role": "Clk_A" }} , 
 	{ "name": "outData_Rst_A", "direction": "out", "datatype": "sc_logic", "bitwidth":1, "type": "signal", "bundle":{"name": "outData", "role": "Rst_A" }}  ]}

set RtlHierarchyInfo {[
	{"ID" : "0", "Level" : "0", "Path" : "`AUTOTB_DUT_INST", "Parent" : "",
		"CDFG" : "openhab_controls_bram",
		"Protocol" : "ap_ctrl_hs",
		"ControlExist" : "1", "ap_start" : "1", "ap_ready" : "1", "ap_done" : "1", "ap_continue" : "0", "ap_idle" : "1",
		"Pipeline" : "None", "UnalignedPipeline" : "0", "RewindPipeline" : "0", "ProcessNetwork" : "0",
		"II" : "0",
		"VariableLatency" : "1", "ExactLatency" : "-1", "EstimateLatencyMin" : "21", "EstimateLatencyMax" : "21",
		"Combinational" : "0",
		"Datapath" : "0",
		"ClockEnable" : "0",
		"HasSubDataflow" : "0",
		"InDataflowNetwork" : "0",
		"HasNonBlockingOperation" : "0",
		"Port" : [
			{"Name" : "inputData_V", "Type" : "Bram", "Direction" : "I"},
			{"Name" : "thresholds_V", "Type" : "Bram", "Direction" : "I"},
			{"Name" : "outData", "Type" : "Bram", "Direction" : "O"}]}]}


set ArgLastReadFirstWriteLatency {
	openhab_controls_bram {
		inputData_V {Type I LastRead 1 FirstWrite -1}
		thresholds_V {Type I LastRead 1 FirstWrite -1}
		outData {Type O LastRead -1 FirstWrite 2}}}

set hasDtUnsupportedChannel 0

set PerformanceInfo {[
	{"Name" : "Latency", "Min" : "21", "Max" : "21"}
	, {"Name" : "Interval", "Min" : "22", "Max" : "22"}
]}

set PipelineEnableSignalInfo {[
]}

set Spec2ImplPortList { 
	inputData_V { bram {  { inputData_V_Addr_A MemPortADDR2 1 32 }  { inputData_V_EN_A MemPortCE2 1 1 }  { inputData_V_WEN_A MemPortWE2 1 4 }  { inputData_V_Din_A MemPortDIN2 1 32 }  { inputData_V_Dout_A MemPortDOUT2 0 32 }  { inputData_V_Clk_A mem_clk 1 1 }  { inputData_V_Rst_A mem_rst 1 1 } } }
	thresholds_V { bram {  { thresholds_V_Addr_A MemPortADDR2 1 32 }  { thresholds_V_EN_A MemPortCE2 1 1 }  { thresholds_V_WEN_A MemPortWE2 1 4 }  { thresholds_V_Din_A MemPortDIN2 1 32 }  { thresholds_V_Dout_A MemPortDOUT2 0 32 }  { thresholds_V_Clk_A mem_clk 1 1 }  { thresholds_V_Rst_A mem_rst 1 1 } } }
	outData { bram {  { outData_Addr_A MemPortADDR2 1 32 }  { outData_EN_A MemPortCE2 1 1 }  { outData_WEN_A MemPortWE2 1 4 }  { outData_Din_A MemPortDIN2 1 32 }  { outData_Dout_A MemPortDOUT2 0 32 }  { outData_Clk_A mem_clk 1 1 }  { outData_Rst_A mem_rst 1 1 } } }
}

set busDeadlockParameterList { 
}

# RTL port scheduling information:
set fifoSchedulingInfoList { 
}

# RTL bus port read request latency information:
set busReadReqLatencyList { 
}

# RTL bus port write response latency information:
set busWriteResLatencyList { 
}

# RTL array port load latency information:
set memoryLoadLatencyList { 
}
