#!/bin/bash

export CC=mpicc
export CXX=mpicxx
export FC=mpifort
export F9X=mpifort

BASEDIR="${HOME}/software"

PREFIX="${BASEDIR}/hdf5/1.14.6"
ZLIB_DIR="${BASEDIR}/zlib/1.3.1"
SZLIB_DIR="${BASEDIR}/szip/2.1.1"

./configure \
--prefix=${PREFIX} \
--enable-fortran \
--enable-parallel \
--with-zlib=${ZLIB_DIR} \
--with-szlib=${SZLIB_DIR}
