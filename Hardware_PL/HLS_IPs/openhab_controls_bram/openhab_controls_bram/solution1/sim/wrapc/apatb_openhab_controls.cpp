// ==============================================================
// Vivado(TM) HLS - High-Level Synthesis from C, C++ and SystemC v2019.2 (64-bit)
// Copyright 1986-2019 Xilinx, Inc. All Rights Reserved.
// ==============================================================

#define AP_INT_MAX_W 32678

#include <systemc>
#include <iostream>
#include <cstdlib>
#include <cstddef>
#include <stdint.h>
#include "SysCFileHandler.h"
#include "ap_int.h"
#include "ap_fixed.h"
#include <complex>
#include <stdbool.h>
#include "autopilot_cbe.h"
#include "hls_stream.h"
#include "hls_half.h"
#include "hls_signal_handler.h"

using namespace std;
using namespace sc_core;
using namespace sc_dt;


// [dump_struct_tree [build_nameSpaceTree] dumpedStructList] ---------->


// [dump_enumeration [get_enumeration_list]] ---------->


// wrapc file define: "inputData_V"
#define AUTOTB_TVIN_inputData_V  "../tv/cdatafile/c.openhab_controls.autotvin_inputData_V.dat"
// wrapc file define: "thresholds_V"
#define AUTOTB_TVIN_thresholds_V  "../tv/cdatafile/c.openhab_controls.autotvin_thresholds_V.dat"
// wrapc file define: "outData"
#define AUTOTB_TVOUT_outData  "../tv/cdatafile/c.openhab_controls.autotvout_outData.dat"
#define AUTOTB_TVIN_outData  "../tv/cdatafile/c.openhab_controls.autotvin_outData.dat"

#define INTER_TCL  "../tv/cdatafile/ref.tcl"

// tvout file define: "outData"
#define AUTOTB_TVOUT_PC_outData  "../tv/rtldatafile/rtl.openhab_controls.autotvout_outData.dat"

class INTER_TCL_FILE {
	public:
		INTER_TCL_FILE(const char* name) {
			mName = name;
			inputData_V_depth = 0;
			thresholds_V_depth = 0;
			outData_depth = 0;
			trans_num =0;
		}

		~INTER_TCL_FILE() {
			mFile.open(mName);
			if (!mFile.good()) {
				cout << "Failed to open file ref.tcl" << endl;
				exit (1);
			}
			string total_list = get_depth_list();
			mFile << "set depth_list {\n";
			mFile << total_list;
			mFile << "}\n";
			mFile << "set trans_num "<<trans_num<<endl;
			mFile.close();
		}

		string get_depth_list () {
			stringstream total_list;
			total_list << "{inputData_V " << inputData_V_depth << "}\n";
			total_list << "{thresholds_V " << thresholds_V_depth << "}\n";
			total_list << "{outData " << outData_depth << "}\n";
			return total_list.str();
		}

		void set_num (int num , int* class_num) {
			(*class_num) = (*class_num) > num ? (*class_num) : num;
		}
	public:
		int inputData_V_depth;
		int thresholds_V_depth;
		int outData_depth;
		int trans_num;

	private:
		ofstream mFile;
		const char* mName;
};

extern void openhab_controls (
ap_fixed<32, 16, (ap_q_mode) 0, (ap_o_mode)3, 0> inputData[10],
ap_fixed<32, 16, (ap_q_mode) 0, (ap_o_mode)3, 0> thresholds[10],
int outData[10]);

void AESL_WRAP_openhab_controls (
ap_fixed<32, 16, (ap_q_mode) 0, (ap_o_mode)3, 0> inputData[10],
ap_fixed<32, 16, (ap_q_mode) 0, (ap_o_mode)3, 0> thresholds[10],
int outData[10])
{
	refine_signal_handler();
	fstream wrapc_switch_file_token;
	wrapc_switch_file_token.open(".hls_cosim_wrapc_switch.log");
	int AESL_i;
	if (wrapc_switch_file_token.good())
	{
		CodeState = ENTER_WRAPC_PC;
		static unsigned AESL_transaction_pc = 0;
		string AESL_token;
		string AESL_num;
		static AESL_FILE_HANDLER aesl_fh;


		// output port post check: "outData"
		aesl_fh.read(AUTOTB_TVOUT_PC_outData, AESL_token); // [[transaction]]
		if (AESL_token != "[[transaction]]")
		{
			exit(1);
		}
		aesl_fh.read(AUTOTB_TVOUT_PC_outData, AESL_num); // transaction number

		if (atoi(AESL_num.c_str()) == AESL_transaction_pc)
		{
			aesl_fh.read(AUTOTB_TVOUT_PC_outData, AESL_token); // data

			sc_bv<32> *outData_pc_buffer = new sc_bv<32>[10];
			int i = 0;

			while (AESL_token != "[[/transaction]]")
			{
				bool no_x = false;
				bool err = false;

				// search and replace 'X' with "0" from the 1st char of token
				while (!no_x)
				{
					size_t x_found = AESL_token.find('X');
					if (x_found != string::npos)
					{
						if (!err)
						{
							cerr << "WARNING: [SIM 212-201] RTL produces unknown value 'X' on port 'outData', possible cause: There are uninitialized variables in the C design." << endl;
							err = true;
						}
						AESL_token.replace(x_found, 1, "0");
					}
					else
					{
						no_x = true;
					}
				}

				no_x = false;

				// search and replace 'x' with "0" from the 3rd char of token
				while (!no_x)
				{
					size_t x_found = AESL_token.find('x', 2);

					if (x_found != string::npos)
					{
						if (!err)
						{
							cerr << "WARNING: [SIM 212-201] RTL produces unknown value 'X' on port 'outData', possible cause: There are uninitialized variables in the C design." << endl;
							err = true;
						}
						AESL_token.replace(x_found, 1, "0");
					}
					else
					{
						no_x = true;
					}
				}

				// push token into output port buffer
				if (AESL_token != "")
				{
					outData_pc_buffer[i] = AESL_token.c_str();
					i++;
				}

				aesl_fh.read(AUTOTB_TVOUT_PC_outData, AESL_token); // data or [[/transaction]]

				if (AESL_token == "[[[/runtime]]]" || aesl_fh.eof(AUTOTB_TVOUT_PC_outData))
				{
					exit(1);
				}
			}

			// ***********************************
			if (i > 0)
			{
				// RTL Name: outData
				{
					// bitslice(31, 0)
					// {
						// celement: outData(31, 0)
						// {
							sc_lv<32>* outData_lv0_0_9_1 = new sc_lv<32>[10];
						// }
					// }

					// bitslice(31, 0)
					{
						int hls_map_index = 0;
						// celement: outData(31, 0)
						{
							// carray: (0) => (9) @ (1)
							for (int i_0 = 0; i_0 <= 9; i_0 += 1)
							{
								if (&(outData[0]) != NULL) // check the null address if the c port is array or others
								{
									outData_lv0_0_9_1[hls_map_index].range(31, 0) = sc_bv<32>(outData_pc_buffer[hls_map_index].range(31, 0));
									hls_map_index++;
								}
							}
						}
					}

					// bitslice(31, 0)
					{
						int hls_map_index = 0;
						// celement: outData(31, 0)
						{
							// carray: (0) => (9) @ (1)
							for (int i_0 = 0; i_0 <= 9; i_0 += 1)
							{
								// sub                    : i_0
								// ori_name               : outData[i_0]
								// sub_1st_elem           : 0
								// ori_name_1st_elem      : outData[0]
								// output_left_conversion : outData[i_0]
								// output_type_conversion : (outData_lv0_0_9_1[hls_map_index]).to_uint64()
								if (&(outData[0]) != NULL) // check the null address if the c port is array or others
								{
									outData[i_0] = (outData_lv0_0_9_1[hls_map_index]).to_uint64();
									hls_map_index++;
								}
							}
						}
					}
				}
			}

			// release memory allocation
			delete [] outData_pc_buffer;
		}

		AESL_transaction_pc++;
	}
	else
	{
		CodeState = ENTER_WRAPC;
		static unsigned AESL_transaction;

		static AESL_FILE_HANDLER aesl_fh;

		// "inputData_V"
		char* tvin_inputData_V = new char[50];
		aesl_fh.touch(AUTOTB_TVIN_inputData_V);

		// "thresholds_V"
		char* tvin_thresholds_V = new char[50];
		aesl_fh.touch(AUTOTB_TVIN_thresholds_V);

		// "outData"
		char* tvin_outData = new char[50];
		aesl_fh.touch(AUTOTB_TVIN_outData);
		char* tvout_outData = new char[50];
		aesl_fh.touch(AUTOTB_TVOUT_outData);

		CodeState = DUMP_INPUTS;
		static INTER_TCL_FILE tcl_file(INTER_TCL);
		int leading_zero;

		// [[transaction]]
		sprintf(tvin_inputData_V, "[[transaction]] %d\n", AESL_transaction);
		aesl_fh.write(AUTOTB_TVIN_inputData_V, tvin_inputData_V);

		sc_bv<32>* inputData_V_tvin_wrapc_buffer = new sc_bv<32>[10];

		// RTL Name: inputData_V
		{
			// bitslice(31, 0)
			{
				int hls_map_index = 0;
				// celement: inputData.V(31, 0)
				{
					// carray: (0) => (9) @ (1)
					for (int i_0 = 0; i_0 <= 9; i_0 += 1)
					{
						// sub                   : i_0
						// ori_name              : inputData[i_0]
						// sub_1st_elem          : 0
						// ori_name_1st_elem     : inputData[0]
						// regulate_c_name       : inputData_V
						// input_type_conversion : (inputData[i_0]).range().to_string(SC_BIN).c_str()
						if (&(inputData[0]) != NULL) // check the null address if the c port is array or others
						{
							sc_lv<32> inputData_V_tmp_mem;
							inputData_V_tmp_mem = (inputData[i_0]).range().to_string(SC_BIN).c_str();
							inputData_V_tvin_wrapc_buffer[hls_map_index].range(31, 0) = inputData_V_tmp_mem.range(31, 0);
                                 	       hls_map_index++;
						}
					}
				}
			}
		}

		// dump tv to file
		for (int i = 0; i < 10; i++)
		{
			sprintf(tvin_inputData_V, "%s\n", (inputData_V_tvin_wrapc_buffer[i]).to_string(SC_HEX).c_str());
			aesl_fh.write(AUTOTB_TVIN_inputData_V, tvin_inputData_V);
		}

		tcl_file.set_num(10, &tcl_file.inputData_V_depth);
		sprintf(tvin_inputData_V, "[[/transaction]] \n");
		aesl_fh.write(AUTOTB_TVIN_inputData_V, tvin_inputData_V);

		// release memory allocation
		delete [] inputData_V_tvin_wrapc_buffer;

		// [[transaction]]
		sprintf(tvin_thresholds_V, "[[transaction]] %d\n", AESL_transaction);
		aesl_fh.write(AUTOTB_TVIN_thresholds_V, tvin_thresholds_V);

		sc_bv<32>* thresholds_V_tvin_wrapc_buffer = new sc_bv<32>[10];

		// RTL Name: thresholds_V
		{
			// bitslice(31, 0)
			{
				int hls_map_index = 0;
				// celement: thresholds.V(31, 0)
				{
					// carray: (0) => (9) @ (1)
					for (int i_0 = 0; i_0 <= 9; i_0 += 1)
					{
						// sub                   : i_0
						// ori_name              : thresholds[i_0]
						// sub_1st_elem          : 0
						// ori_name_1st_elem     : thresholds[0]
						// regulate_c_name       : thresholds_V
						// input_type_conversion : (thresholds[i_0]).range().to_string(SC_BIN).c_str()
						if (&(thresholds[0]) != NULL) // check the null address if the c port is array or others
						{
							sc_lv<32> thresholds_V_tmp_mem;
							thresholds_V_tmp_mem = (thresholds[i_0]).range().to_string(SC_BIN).c_str();
							thresholds_V_tvin_wrapc_buffer[hls_map_index].range(31, 0) = thresholds_V_tmp_mem.range(31, 0);
                                 	       hls_map_index++;
						}
					}
				}
			}
		}

		// dump tv to file
		for (int i = 0; i < 10; i++)
		{
			sprintf(tvin_thresholds_V, "%s\n", (thresholds_V_tvin_wrapc_buffer[i]).to_string(SC_HEX).c_str());
			aesl_fh.write(AUTOTB_TVIN_thresholds_V, tvin_thresholds_V);
		}

		tcl_file.set_num(10, &tcl_file.thresholds_V_depth);
		sprintf(tvin_thresholds_V, "[[/transaction]] \n");
		aesl_fh.write(AUTOTB_TVIN_thresholds_V, tvin_thresholds_V);

		// release memory allocation
		delete [] thresholds_V_tvin_wrapc_buffer;

		// [[transaction]]
		sprintf(tvin_outData, "[[transaction]] %d\n", AESL_transaction);
		aesl_fh.write(AUTOTB_TVIN_outData, tvin_outData);

		sc_bv<32>* outData_tvin_wrapc_buffer = new sc_bv<32>[10];

		// RTL Name: outData
		{
			// bitslice(31, 0)
			{
				int hls_map_index = 0;
				// celement: outData(31, 0)
				{
					// carray: (0) => (9) @ (1)
					for (int i_0 = 0; i_0 <= 9; i_0 += 1)
					{
						// sub                   : i_0
						// ori_name              : outData[i_0]
						// sub_1st_elem          : 0
						// ori_name_1st_elem     : outData[0]
						// regulate_c_name       : outData
						// input_type_conversion : outData[i_0]
						if (&(outData[0]) != NULL) // check the null address if the c port is array or others
						{
							sc_lv<32> outData_tmp_mem;
							outData_tmp_mem = outData[i_0];
							outData_tvin_wrapc_buffer[hls_map_index].range(31, 0) = outData_tmp_mem.range(31, 0);
                                 	       hls_map_index++;
						}
					}
				}
			}
		}

		// dump tv to file
		for (int i = 0; i < 10; i++)
		{
			sprintf(tvin_outData, "%s\n", (outData_tvin_wrapc_buffer[i]).to_string(SC_HEX).c_str());
			aesl_fh.write(AUTOTB_TVIN_outData, tvin_outData);
		}

		tcl_file.set_num(10, &tcl_file.outData_depth);
		sprintf(tvin_outData, "[[/transaction]] \n");
		aesl_fh.write(AUTOTB_TVIN_outData, tvin_outData);

		// release memory allocation
		delete [] outData_tvin_wrapc_buffer;

// [call_c_dut] ---------->

		CodeState = CALL_C_DUT;
		openhab_controls(inputData, thresholds, outData);

		CodeState = DUMP_OUTPUTS;

		// [[transaction]]
		sprintf(tvout_outData, "[[transaction]] %d\n", AESL_transaction);
		aesl_fh.write(AUTOTB_TVOUT_outData, tvout_outData);

		sc_bv<32>* outData_tvout_wrapc_buffer = new sc_bv<32>[10];

		// RTL Name: outData
		{
			// bitslice(31, 0)
			{
				int hls_map_index = 0;
				// celement: outData(31, 0)
				{
					// carray: (0) => (9) @ (1)
					for (int i_0 = 0; i_0 <= 9; i_0 += 1)
					{
						// sub                   : i_0
						// ori_name              : outData[i_0]
						// sub_1st_elem          : 0
						// ori_name_1st_elem     : outData[0]
						// regulate_c_name       : outData
						// input_type_conversion : outData[i_0]
						if (&(outData[0]) != NULL) // check the null address if the c port is array or others
						{
							sc_lv<32> outData_tmp_mem;
							outData_tmp_mem = outData[i_0];
							outData_tvout_wrapc_buffer[hls_map_index].range(31, 0) = outData_tmp_mem.range(31, 0);
                                 	       hls_map_index++;
						}
					}
				}
			}
		}

		// dump tv to file
		for (int i = 0; i < 10; i++)
		{
			sprintf(tvout_outData, "%s\n", (outData_tvout_wrapc_buffer[i]).to_string(SC_HEX).c_str());
			aesl_fh.write(AUTOTB_TVOUT_outData, tvout_outData);
		}

		tcl_file.set_num(10, &tcl_file.outData_depth);
		sprintf(tvout_outData, "[[/transaction]] \n");
		aesl_fh.write(AUTOTB_TVOUT_outData, tvout_outData);

		// release memory allocation
		delete [] outData_tvout_wrapc_buffer;

		CodeState = DELETE_CHAR_BUFFERS;
		// release memory allocation: "inputData_V"
		delete [] tvin_inputData_V;
		// release memory allocation: "thresholds_V"
		delete [] tvin_thresholds_V;
		// release memory allocation: "outData"
		delete [] tvout_outData;
		delete [] tvin_outData;

		AESL_transaction++;

		tcl_file.set_num(AESL_transaction , &tcl_file.trans_num);
	}
}

