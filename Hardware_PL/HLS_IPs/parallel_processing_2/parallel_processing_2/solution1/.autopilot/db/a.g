#!/bin/sh
lli=${LLVMINTERP-lli}
exec $lli \
    /home/jaswanth/workspace/hls_ip/parallel_processing_2/parallel_processing_2/solution1/.autopilot/db/a.g.bc ${1+"$@"}
