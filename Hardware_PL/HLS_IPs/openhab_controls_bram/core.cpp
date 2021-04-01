#include <hls_stream.h>
#include <ap_axi_sdata.h>
#include <ap_fixed.h>

typedef ap_fixed<32,16,AP_RND> fp32_16;
//typedef ap_axiu<32,1,1,1> intSdCh;

void openhab_controls_bram(fp32_16 inputData[10], fp32_16 thresholds[10], int outData[10])
{
	#pragma HLS INTERFACE bram port=thresholds	//Interface for bram ports thresholds and outData
	#pragma HLS INTERFACE bram port=outData
	#pragma HLS INTERFACE bram port=inputData



	for(int i = 0; i<10; i++)
	{
		outData[i] = inputData[i] < thresholds[i];
	}
}
