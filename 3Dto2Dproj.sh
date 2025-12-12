#!/bin/csh

# this script produces 2D projections from a processed nmrpipe spectrum file in pipe format
if( $# < 1 ) then
   echo "Use: $0 <spectrum type> "
   exit 1
endif

set proc_out=test%03d.dat

cat $1 | pipe2xyz -out ft/${proc_out} -x -verb -ov
proj3D.tcl -in ft/${proc_out}
rm -r ft

if( $1:e == 'P3') then
    foreach f (*.dat)
        mv "$f" "$1:h/$1:t:r_$f:r.P3"
    end
else
    foreach f (*.dat)
        mv "$f" "$1:h/$1:t:r_$f:r.ft2"
    end
endif
