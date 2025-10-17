# Instructions

## Create directories

To get source code:
`mkdir ~/source-code`

To install built software:
`mkdir ~/software`

To store module files:
`mkdir ~/my-module-files`

## Clone repository with workshop scripts

Will be available at `~/scripts`:
`git clone https://github.com/jmcastelo/scripts.git ~/scripts`

## Let's build the dependencies

### zlib v1.3.1

`cd ~/source-code`
`wget https://www.zlib.net/zlib-1.3.1.tar.gz`
`tar xzvf zlib-1.3.1.tar.gz`
`cd zlib-1.3.1`
`cp ~/scripts/workshop/zlib/zlib_gnu_configure.sh .`
`cat -n zlib_gnu_configure`
`./zlib_gnu_configure.sh`
`make test`
`make install`

### szip v2.1.1

`cd ~/source-code`
`wget https://docs.hdfgroup.org/archive/support/ftp/lib-external/szip/2.1.1/src/szip-2.1.1.tar.gz`


