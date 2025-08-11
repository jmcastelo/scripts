#!/bin/bash

PREFIX="/path/to/libxc"

export CC=icx
export FC=ifx

autoreconf -i

./configure \
--prefix=${PREFIX}
