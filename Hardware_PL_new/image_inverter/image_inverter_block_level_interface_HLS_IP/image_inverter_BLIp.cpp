#include <hls_stream.h>
#include <ap_axi_sdata.h>

//declare 32 bit integer with side channels (Data,user,id,dest) widths of strobe(strb) and keep are calculated from data width.
typedef ap_axiu<8,0,0,0> intSdCh;

void image_inverter_BLIp(hls::stream<intSdCh> &inStream, hls::stream<intSdCh> &outStream)
{

#pragma HLS INTERFACE axis register port=inStream
#pragma HLS INTERFACE axis register port=outStream
//#pragma HLS INTERFACE ap_ctrl_none port=return
// we need to indicate a size of the stream

#pragma HLS PIPELINE
		// Read and cache (block here if FIFO sender is empty
		intSdCh valIn = inStream.read();
		intSdCh valOut;

		valOut.data = 255 - valIn.data;

		//connecting side channels of input to output for 2 way communication
		valOut.keep = valIn.keep;
		valOut.strb = valIn.strb;
//		valOut.user = valIn.user;
		valOut.last = valIn.last;
//		valOut.id = valIn.id;
//		valOut.dest = valIn.dest;

		//Sends to stream
		outStream.write(valOut);
}
