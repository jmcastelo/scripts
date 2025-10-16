#!/bin/bash

BASEDIR="${HOME}/software"
PREFIX="${BASEDIR}/libxc/6.2.2"

autoreconf -i

./configure \
--prefix=${PREFIX}
