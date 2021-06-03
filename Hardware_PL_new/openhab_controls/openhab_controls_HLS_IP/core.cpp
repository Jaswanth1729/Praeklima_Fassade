#include <hls_stream.h>
#include <ap_axi_sdata.h>
#include <ap_fixed.h>
#include <ap_int.h>

typedef ap_fixed<32,16,AP_RND> fp32_16;
typedef ap_axiu<32,1,1,1> intSdCh;

void openhab_controls(hls::stream<intSdCh> &inStream, hls::stream<intSdCh> &outStream, fp32_16 thresholds[20], fp32_16 outData[20])
{
	#pragma HLS INTERFACE bram port=thresholds	//Interface for bram ports thresholds and outData
	#pragma HLS INTERFACE bram port=outData
	#pragma HLS INTERFACE axis port=inStream	// Interface for input streams
	#pragma HLS INTERFACE axis port=outStream

	for(int i = 0; i<20; i++)
	{
		intSdCh valIn = inStream.read();
		intSdCh valOut;
							//type casting data types
		fp32_16 inter_data;
		ap_uint<32> read_val;
		read_val = valIn.data;
		inter_data.range() = read_val.range();
		//#pragma HLS pipeline
		outData[i] = inter_data < thresholds[i];
		valOut.data = valIn.data;

		valOut.keep = valIn.keep;
		valOut.strb = valIn.strb;
		valOut.user = valIn.user;
		valOut.last = valIn.last;
		valOut.id   = valIn.id;
		valOut.dest = valIn.dest;

				// Send to the stream (Block if the FIFO receiver is full)
		outStream.write(valOut);
	}
}


