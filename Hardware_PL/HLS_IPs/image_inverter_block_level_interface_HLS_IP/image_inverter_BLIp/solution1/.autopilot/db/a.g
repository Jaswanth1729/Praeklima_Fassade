#!/bin/sh
lli=${LLVMINTERP-lli}
exec $lli \
    /home/jaswanth/WORK/DAC_SDC/image_inverter_block_level_interface/image_inverter_BLIp/solution1/.autopilot/db/a.g.bc ${1+"$@"}
