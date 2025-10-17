#!/bin/bash

BASEDIR="${HOME}/software"

export PETSC_DIR="${BASEDIR}/petsc/3.22.5"
export SLEPC_DIR="${PWD}"

PREFIX="${BASEDIR}/slepc/3.22.2"

./configure \
--prefix=${PREFIX} \
--with-clean 
