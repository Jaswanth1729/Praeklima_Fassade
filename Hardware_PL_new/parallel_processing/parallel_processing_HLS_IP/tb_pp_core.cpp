#include <hls_stream.h>
#include <ap_axi_sdata.h>

// Declare 32-bit integer with side-channel
typedef ap_axiu<32,1,1,1> intSdCh;

void pp_1(hls::stream<intSdCh> &inStream, hls::stream<intSdCh> &outStream);

int main()
{
	// Define streams for input and output
	hls::stream<intSdCh> inputStream;
	hls::stream<intSdCh> outputStream;

	// Populate input stream
	for (int idx = 0; idx < 20; idx++)
	{
		intSdCh valIn;
		valIn.data = idx;
		valIn.keep = 1; valIn.strb = 1; valIn.user = 1; valIn.id = 0; valIn.dest = 0;
		inputStream << valIn;
	}

	// Call top function of IP
	pp_1(inputStream,outputStream);

	// Populate input stream
	for (int idxOut = 0; idxOut < 20; idxOut++)
	{
		intSdCh valOut;
		outputStream.read(valOut);
		printf("Value is %d\n",(int)valOut.data);
	}

	return 0;
}
