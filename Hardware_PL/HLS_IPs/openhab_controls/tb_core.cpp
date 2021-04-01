#include <hls_stream.h>
#include <ap_axi_sdata.h>

typedef ap_fixed<32,16,AP_RND> fp32_16;
typedef ap_axiu<32,1,1,1> intSdCh;

void openhab_controls(hls::stream<intSdCh> &inStream, hls::stream<intSdCh> &outStream, fp32_16 thresholds[20], fp32_16 outData[20]);

int main()
{
	// Define streams for input and output
	hls::stream<intSdCh> inputStream;
	hls::stream<intSdCh> outputStream;

	// Populate input stream
	for (int idx = 0; idx < 20; idx++)
		{

			intSdCh valIn;
			valIn.data = 380108;
			valIn.keep = 1; valIn.strb = 1; valIn.user = 1; valIn.id = 0; valIn.dest = 0;
			inputStream << valIn;
			printf("Value is %f and idx is %d\n",(float)valIn.data, idx);
		}

	fp32_16 inter_data;
			ap_uint<32> read_val;
			read_val = 380108;
			inter_data.range() = read_val.range();
			printf("%d \n ", (int)read_val);
			printf("%f \n", (float)inter_data);

	fp32_16 thresholds[20];
	fp32_16 bram_out[20];
	for (int idxX = 0; idxX < 20; idxX++)
		{
			thresholds[idxX] = idxX;
			printf("%f \n",thresholds[idxX].to_float());
			printf("Value is %d\n",thresholds[idxX]);
		}
	// Call top function of IP

	openhab_controls(inputStream,outputStream,thresholds,bram_out);

	for (int idxOut = 0; idxOut < 20; idxOut++)
		{
			intSdCh valOut;
			outputStream.read(valOut);
			float temp = bram_out[idxOut].to_float();
			printf("Value is %d\n",(int)valOut.data);
			printf("%f \n ", temp );
		}


	return 0;
}
