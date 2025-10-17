# Instructions

Our objective is to build YAMBO with (almost) all its dependencies as well.

First, we will create some directories in our home directory (that's what the tilde `~` stands for), to keep all the required data. We will clone this repository, which contains, under the `workshop` (this) directory all scripts required to configure the build of the dependencies, and also their respective module files.

Each configuration script has been tested within the system where the workshop is taking place, and should work for the version of its corresponding code. Note that in order to prepare these configuration scripts, one has to read the install/build instructions (files `README`, `INSTALL` and similar) for each software or library one wants to build and understand the building process. Usually, the GNU build tools are employed (although other alternatives exist, like CMake), whose general procedure is:

1. `./configure`
2. `make`
3. `make install`

The configuration script prepares a `Makefile` file with build instructions, so it usually accepts many options (flags) and reads from environment variables to set the build to our specific system (selecting compilers, switching on/off several software features, setting paths for dependencies and installation, etc.). After configuration, `make` compiles the software/library according to the `Makefile`, which contains our building choices. Finally, `make install` copies the result of our compilation to the installation directory we have chosen.

As for the module files in this repository, they can be loaded to modify our shell environment and make their associated software/libraries available for us to keep building against them, even if it is not strictly neeed in most cases, since we will specify the paths of the dependencies in the configuration scripts.

We will give detailed instructions to build the first dependency. The rest will be built in a similar way, so we will only give comments whenever we make something differently.

Let's start!

## Create directories

To store source code:

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

If the execution of the configuration script does not yield any error, let's build the dependency:

`make test`

If compilation was successful, let's install (copy) our new dependency:

`make install`

Let's check which files were installed:

`ls -R ~/software/zlib/1.3.1`

Now, create a subdirectory to contain the module file for this dependency and copy the module file:

`mkdir ~/my-module-files/zlib`

`cp ~/scripts/workshop/zlib/1.3.1 ~/my-module-files/zlib/`

Let's take a look at the module file:

`cat -n ~/my-module-files/zlib/1.3.1`

And see if it gets correctly detected by the environment modules system:

`module avail`

`module show zlib/1.3.1`

If so, let's load it to set our environment capable of using this dependency for the compilation of further dependencies:

`module load zlib/1.3.1`

And check if the module has been correctly loaded:

`module list`

This ends our first dependency build. For the rest, we will just give the commands without textual instructions if they are analogous to those we have just covered.

## szip v2.1.1

`cd ~/source-code`

`wget https://docs.hdfgroup.org/archive/support/ftp/lib-external/szip/2.1.1/src/szip-2.1.1.tar.gz`

`tar xzvf szip-2.1.1.tar.gz`

`cd szip-2.1.1`

`cp ~/scripts/workshop/szip/szip_gnu_configure.sh .`

`cat -n szip_gnu_configure.sh`

`./szip_gnu_configure.sh`

`make`

`make check`

`make install`

`ls -R ~/software/szip/2.1.1`

`mkdir ~/my-module-files/szip`

`cp ~/scripts/workshop/szip/2.1.1 ~/my-module-files/szip/`

`module avail`

`module show szip/2.1.1`

`module load szip/2.1.1`

`module list`

## HDF5 v1.14.6

`cd ~/source-code`

`wget https://github.com/HDFGroup/hdf5/archive/refs/tags/hdf5_1.14.6.tar.gz`

`tar xzvf hdf5_1.14.6.tar.gz`

`cd hdf5-hdf5_1.14.6`

`cp ~/scripts/workshop/hdf5/hdf5_gnu_configure.sh .`

`cat -n hdf5_gnu_configure.sh`

`./hdf5_gnu_configure.sh`

`make`

We will skip the tests (`make check`), since they take long and consume many resources.

`make install`

`ls -R ~/software/hdf5/1.14.6`

`mkdir ~/my-module-files/hdf5`

`cp ~/scripts/workshop/hdf5/1.14.6 ~/my-module-files/hdf5/`

`module avail`

`module show hdf5/1.14.6`

`module load hdf5/1.14.6`

`module list`

## NetCDF-C v4.9.3

`cd ~/source-code`

`wget https://github.com/Unidata/netcdf-c/archive/refs/tags/v4.9.3.tar.gz`

`tar xzvf v4.9.3.tar.gz`

`cd netcdf-c-4.9.3`

`cp ~/scripts/workshop/netcdf-c/netcdf-c_gnu_configure.sh .`

`cat -n netcdf-c_gnu_configure.sh`

`./netcdf-c_gnu_configure.sh`

`make`

We will skip the tests (`make check`), since they take long and consume many resources.

`make install`

`ls -R ~/software/netcdf-c/4.9.3`

`mkdir ~/my-module-files/netcdf-c`

`cp ~/scripts/workshop/netcdf-c/4.9.3 ~/my-module-files/netcdf-c/`

`module avail`

`module show netcdf-c/4.9.3`

`module load netcdf-c/4.9.3`

`module list`

## NetCDF-Fortran v4.6.2

`cd ~/source-code`

`wget https://github.com/Unidata/netcdf-fortran/archive/refs/tags/v4.6.2.tar.gz`

`tar xzvf v4.6.2.tar.gz`

`cd netcdf-fortran-4.6.2`

`cp ~/scripts/workshop/netcdf-fortran/netcdf-fortran_gnu_configure.sh .`

`cat -n netcdf-fortran_gnu_configure.sh`

`make`

We will skip the tests (`make check`), since they take long and consume many resources.

`make install`

`ls -R ~/software/netcdf-fortran/4.6.2`

`mkdir ~/my-module-files/netcdf-fortran`

`cp ~/scripts/workshop/netcdf-fortran/4.6.2 ~/my-module-files/netcdf-fortran/`

`module avail`

`module show netcdf-fortran/4.6.2`

`module load netcdf-fortran/4.6.2`

`module list`

## OpenBLAS v0.3.30

`cd ~/source-code`

`wget https://github.com/OpenMathLib/OpenBLAS/archive/refs/tags/v0.3.30.tar.gz`

`tar xzvf v0.3.30.tar.gz`

`cd OpenBLAS-0.3.30`

This dependency does not configure the build with the usual `configure` script, but we have to tweak the `Makefile.rule` file with our own configuration settings. Let's back it up and copy the modified file:

`mv Makefile.rule Makefile.rule.bak`

`cp ~/scripts/workshop/openblas/Makefile.rule .`

See the changes we made:

`diff Makefile.rule.bak Makefile.rule`

`make`

`make install`

`ls -R ~/software/openblas/0.3.30`

`mkdir ~/my-module-files/openblas`

`cp ~/scripts/workshop/openblas/0.3.30 ~/my-module-files/openblas/`

`module show openblas/0.3.30`

`module load openblas/0.3.30`

`module list`
