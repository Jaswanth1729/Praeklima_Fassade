#!/bin/sh
lli=${LLVMINTERP-lli}
exec $lli \
    /home/jaswanth/WORK/DAC_SDC/image_inverter/solution1/.autopilot/db/a.g.bc ${1+"$@"}
