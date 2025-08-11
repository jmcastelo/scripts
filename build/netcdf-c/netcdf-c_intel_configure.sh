#!/bin/bash

PREFIX="/path/to/netcdf-c"

export CC=mpiicx

./configure \
--disable-parallel-tests \
--disable-dap \
--disable-libxml2 \
--prefix=${PREFIX}
