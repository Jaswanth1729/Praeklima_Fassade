#include <hls_stream.h>
#include <ap_axi_sdata.h>

typedef ap_fixed<32,16,AP_RND> fp32_16;

void openhab_controls_bram(fp32_16 inputData[10], fp32_16 thresholds[10], int outData[10]);

int main()
{
	fp32_16 inData[10];
	fp32_16 thresholds[10];
	int bram_out[10];
	for (int idxX = 0; idxX < 10; idxX++)
		{
			fp32_16 x = 5.5;
			thresholds[idxX] = x;
			inData[idxX] = (idxX <= 5)? x+1 : x-1;
			printf("%f \n",(double)(thresholds[idxX]));
			printf("%f \n\n",(double)(inData[idxX]));
		}
	// Call top function of IP

	openhab_controls_bram(inData,thresholds,bram_out);

	for (int idxOut = 0; idxOut < 10; idxOut++)
		{
			printf("Value is %f\n",(double)inData[idxOut]);
//			printf("Value is %lld\n",(long long)(valOut.data));
			printf("%f \n ", (double)(thresholds[idxOut] ));
			printf("%d \n ", bram_out[idxOut]);

		}


	return 0;
}
