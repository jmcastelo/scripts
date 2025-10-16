#!/bin/bash

BASEDIR="${HOME}/software"

OBLAS_DIR="${BASEDIR}/openblas/0.3.30"
FFTW_DIR="${BASEDIR}/fftw/3.3.10"
SLEPC_DIR="${BASEDIR}/slepc/3.24.0"
PETSC_DIR="${BASEDIR}/petsc/3.24.0"
SCALA_DIR="${BASEDIR}/scalapack/2.2.2"
HDF5_DIR="${BASEDIR}/phdf5/1.14.6"
NC_DIR="${BASEDIR}/netcdf-c/4.9.3"
NF_DIR="${BASEDIR}/netcdf-fortran/4.6.2"
LIBXC_DIR="${BASEDIR}/libxc/6.2.2"

YAMBO_LIBS_DIR="${HOME}/source-code/yambo-libs"

export CC=gcc
export FC=gfortran
export MPICC=mpicc
export MPIFC=mpifort

./configure \
--enable-msgs-comps \
--enable-time-profile \
--enable-mpi \
--enable-iotk \
--without-editor \
--enable-memory-profile \
--enable-slepc-linalg \
--enable-hdf5-par-io \
--with-blas-libs="-L${OBLAS_DIR}/lib -lopenblas" \
--with-lapack-libs="-L${OBLAS_DIR}/lib -lopenblas" \
--with-fft-path=${FFTW_DIR} \
--with-slepc-path=${SLEPC_DIR} \
--with-petsc-path=${PETSC_DIR} \
--with-blacs-libs="-L${SCALA_DIR}/lib -lscalapack" \
--with-scalapack-libs="-L${SCALA_DIR}/lib -lscalapack" \
--with-hdf5-path=${HDF5_DIR} \
--with-netcdf-path=${NC_DIR} \
--with-netcdff-path=${NF_DIR} \
--with-libxc-path=${LIBXC_DIR} \
--with-extlibs-path="${YAMBO_LIBS_DIR}"
