#!/bin/bash

BASEDIR="${HOME}/software"

export CC=mpicc

export H5DIR="${BASEDIR}/hdf5/1.14.6"
export CPPFLAGS="-I${H5DIR}/include"
export LDFLAGS="-L${H5DIR}/lib"

PREFIX="${BASEDIR}/netcdf-c/4.9.3"

./configure \
--prefix=${PREFIX}
