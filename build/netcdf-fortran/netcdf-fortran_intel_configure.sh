#!/bin/bash

PREFIX="/path/to/netcdf-fortran"

export CC=mpiicx
export FC=mpiifx

./configure \
--prefix=${PREFIX}
