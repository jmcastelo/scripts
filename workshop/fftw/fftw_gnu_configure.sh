#!/bin/bash

BASEDIR="${HOME}/software"

PREFIX="${BASEDIR}/fftw/3.3.10"

export CFLAGS="-fPIC"

./configure \
--prefix=${PREFIX} \
--enable-mpi
