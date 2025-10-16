#!/bin/bash

BASEDIR="${HOME}/software"

NCDIR="${BASEDIR}/netcdf-c/4.9.3"
H5DIR="${BASEDIR}/hdf5/1.14.6"

PREFIX="${BASEDIR}/netcdf-fortran/4.6.2"

export CC=mpicc
export FC=mpifort
export CPPFLAGS="-I${NCDIR}/include -I${H5DIR}/include"
export LDFLAGS="-L${NCDIR}/lib -L${H5DIR}/lib"
export LIBS="-lnetcdf -lhdf5_hl -lhdf5"
export HDF5_PLUGIN_PATH="${BASEDIR}/netcdf-c/4.9.3/hdf5"

./configure \
--prefix=${PREFIX}
