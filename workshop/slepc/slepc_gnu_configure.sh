#!/bin/bash

BASEDIR="${HOME}/software"

export PETSC_DIR="${BASEDIR}/petsc/3.24.0"
export SLEPC_DIR="${PWD}"

PREFIX="${BASEDIR}/slepc/3.24.0"

./configure \
--prefix=${PREFIX} \
--with-clean 
