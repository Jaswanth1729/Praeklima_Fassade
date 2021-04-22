# Designing PYNQ DPU Overlay with Vitis AI
This repository holds the PYNQ DPU overlay. Specifically, the Vitis AI DPU for Ultra96 FPGA. 
Steps to rebuild the designs in Vitis and can be ported onto PYNQ-enabled Zynq Ultrascale+ boards.

PYNQ DPU currently support the following boards:

* Ultra96
* ZCU104
* ZCU111

Prebuild DPU Block design models are available in this repository for Ultra96.

## Quick Start from Edge side (Ultra96 FPGA)

### 1. Upgrading the PYNQ v2.6 image in Ultra96

This upgrade step is to make sure users have a DPU-ready image. 
This step is only required for one time.

On your board, run `su` to use super user. Then run the following commands:

```shell
git clone --recursive --shallow-submodules https://github.com/Xilinx/DPU-PYNQ.git
cd DPU-PYNQ/upgrade
make
```

The upgrade process may take up to 1 hour, since a few packages will 
need to be installed. 

### 2. Install

Run the following on board:

```shell
pip3 install pynq-dpu
```

Then go to your jupyter notebook home folder and fetch the notebooks:

```shell
cd $PYNQ_JUPYTER_NOTEBOOKS
pynq get-notebooks pynq-dpu -p .
```

This will make sure the desired notebooks (Resnet50 and inception notebooks and their trained models) shows up in your jupyter notebook 
folder.

### 3. Run

You are ready to go! Now in jupyter, you can explore the notebooks 
in `pynq-dpu` folder.

## DPU Block Design
The DPU IP comes from the [Vitis Ai Github](https://github.com/Xilinx/Vitis-AI/tree/v1.2.1).
Can use this IP in Vivado to build custom designs.

To create Overlay in pynq generally, we need .bit and .hwh design files. 
for vitis AI we nedd .bit, .hwh and .xclbin files (block design files) to run Vitis AI models (.xmodel file). 
From example notebooks from xilinx pynq-dpu download the prebuild block design files by xilinx.

### To rebuild DPU block design 
Make sure you have cloned this repository onto your host machine. We will
leverage the DPU IP officially released in the Vitis AI repository, so we
need to populate the submodule in DPU-PYNQ repository.

If you have not cloned the repo yet:

```bash
git clone --recursive --shallow-submodules https://github.com/Xilinx/DPU-PYNQ.git
cd DPU-PYNQ/boards
```

If you have already cloned the repository, make sure submodules are loaded:

```bash
cd DPU-PYNQ
git submodule init
git submodule update
cd boards
```

To build the DPU hardware design, we first need to make sure Vitis and XRT 
have been installed and their settings are sourced properly.

```shell
source <vitis-install-path>/Vitis/2020.2/settings64.sh
source <xrt-install-path>/xilinx/xrt/setup.sh
```

To build the DPU hardware design, you can modify the `dpu_conf.vh` file to change the DPU IP settings in the 
board folder. The adjustable settings of the DPU IP include: 

* `DPU model number` 
* `URAM_ENABLE`
* `RAM_USAGE_LOW`
* `CHANNEL_AUGMENTATION_ENABLE`
* `DWCV_ENABLE`
* `POOL_AVG_ENABLE`
* `RELU_LEAKYRELU_RELU6`
* `DSP48_USAGE_HIGH`
* `LOWPOWER_ENABLE`
* `DEVICE Configuration`

Max DPU architecture that Ultra96 has is 'B1600' which is used by xilinx in their default dpu.bit file.
For more information regarding the DPU IP, you can refer to the [official Vitis AI DPU guide](https://github.com/Xilinx/Vitis-AI/blob/v1.2.1/DPU-TRD/prj/Vitis/README.md) in 5.3 configurating DPU section.
After changing required configurations then build the hardware design. In our case BOARD=Ultra96

```shell
make BOARD=<Board>
```

During this process, the corresponding Vitis platform will be generated
for the specified board. The make process generates in `<Board>`:

1. `dpu.bit`
2. `dpu.hwh`
3. `dpu.xclbin`

## Build Machine Learning Models for DPU
you can refer to the
[instructions for DPU models](https://github.com/Xilinx/DPU-PYNQ/blob/master/host/README.md).






