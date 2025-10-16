#!/bin/bash

export PETSC_DIR="${PWD}"

BASEDIR="${HOME}/software"

PREFIX="${BASEDIR}/petsc/3.24.0"

FFTWDIR="${BASEDIR}/fftw/3.3.10"
OBLASDIR="${BASEDIR}/openblas/0.3.30"
SLDIR="${BASEDIR}/scalapack/2.2.2"
H5DIR="${BASEDIR}/phdf5/1.14.6"
NCDIR="${BASEDIR}/netcdf-c/4.9.3"
ZLIBDIR="${BASEDIR}/zlib/1.3.1"


./configure \
--prefix=${PREFIX} \
--with-debugging=0 \
--with-make-np=1 \
--with-scalar-type=complex \
--with-fftw=1 \
--with-fftw-dir=${FFTWDIR} \
--with-openblas=1 \
--with-openblas-dir=${OBLASDIR} \
--with-scalapack=1 \
--with-scalapack-dir=${SLDIR} \
--with-hdf5=1 \
--with-hdf5-dir=${H5DIR} \
--with-netcdf=1 \
--with-netcdf-dir=${NCDIR} \
--with-zlib=1 \
--with-zlib-dir=${ZLIBDIR}
