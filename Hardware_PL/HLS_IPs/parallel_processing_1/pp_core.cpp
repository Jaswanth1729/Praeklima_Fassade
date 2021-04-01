#include <hls_stream.h>
#include <ap_axi_sdata.h>
#include <ap_fixed.h>
#include <ap_int.h>

typedef ap_fixed<32,16,AP_RND> fp32_16;
typedef ap_axiu<32,1,1,1> intSdCh;

void pp_1(hls::stream<intSdCh> &inStream, hls::stream<intSdCh> &outStream)
{
	#pragma HLS INTERFACE axis port=inStream	// Interface for input streams
	#pragma HLS INTERFACE axis port=outStream

	for(int i = 0; i<20; i++)
	{
		intSdCh valIn = inStream.read();
		intSdCh valOut;
							//type casting data types
		valOut.data = valIn.data + 5;

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

