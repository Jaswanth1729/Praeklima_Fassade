#include <hls_stream.h>
#include <ap_axi_sdata.h>

typedef ap_axiu<8,0,0,0> intSdCh;

void image_inverter1(hls::stream<intSdCh> &inStream, hls::stream<intSdCh> &outStream);

int main()
{
	//Define streams for input and output
	hls::stream<intSdCh> inputStream;
	hls::stream<intSdCh> outputStream;


		intSdCh valIn;
		valIn.data = 5;
		valIn.keep =1;
		valIn.strb = 1;
//		valIn.user = 1;
//		valIn.id = 0;
//		valIn.dest = 0;

		inputStream << valIn;


	image_inverter1(inputStream,outputStream);


		intSdCh valOut;
		outputStream.read(valOut);
		printf("value  is %d\n", (int)valOut.data);



}
