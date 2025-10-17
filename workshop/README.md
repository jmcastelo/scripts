# Instructions

## Create directories

To get source code:

`mkdir ~/source-code`

To install built software:

`mkdir ~/software`

To store module files:

`mkdir ~/my-module-files`

## Use our custom module files directory

`module use ~/my-module-files`

## Clone repository with workshop scripts

Will be available at `~/scripts`:

`git clone https://github.com/jmcastelo/scripts.git ~/scripts`

## zlib v1.3.1

This is our first dependency we want to build. Follow the instructions below.

Let's change into the directory where we will keep all source code.

`cd ~/source-code`

Let's get the packed source code and unpack it:

`wget https://www.zlib.net/zlib-1.3.1.tar.gz`

`tar xzvf zlib-1.3.1.tar.gz`

Let's change into the directory where the dependency code has ben extracted:

`cd zlib-1.3.1`

Let's copy the configuration script for this dependency and take a look at it:

`cp ~/scripts/workshop/zlib/zlib_gnu_configure.sh .`

`cat -n zlib_gnu_configure.sh`

If everything looks fine, let's execute it:

`./zlib_gnu_configure.sh`

If the output of the configuration scripts looks fine, let's build and install the dependeny:

`make test`

`make install`

Finally, if compilation was successfull, create a subdirectory to contain the module file for this dependency and copy the module file:

`mkdir ~/my-module-files/zlib`

`cp ~/scripts/workshop/zlib/1.3.1 ~/my-module-files/zlib/`

Let's take a look at the module file:

`cat -n ~/my-module-files/zlib/1.3.1`

And see if it gets correctly detected:

`module avail`

If so, let's load it:

`module load zlib/1.3.1`

## szip v2.1.1

`cd ~/source-code`

`wget https://docs.hdfgroup.org/archive/support/ftp/lib-external/szip/2.1.1/src/szip-2.1.1.tar.gz`


