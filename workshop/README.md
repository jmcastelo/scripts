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

A lossless data-compresion library.

[Official website](https://www.zlib.net)

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

Provides lossless compression of scientific data.

[Official website](https://docs.hdfgroup.org/archive/support/doc_resource/SZIP/index.html)

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

HDF = Hierarchical Data Format

- Set of libraries and data formats, designed to store and organize largfe amounts of data.
- An HDF5 files is a container of heterogeneous datasets (images, tables, graphs, documents, etc.)
- Available for C, C++, Fortran, Java and Python.

[Introduction to HDF5](https://support.hdfgroup.org/documentation/hdf5/latest/_intro_h_d_f5.html)

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

`./netcdf-fortran_gnu_configure.sh`

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

## ScaLAPACK v2.2.2

`cd ~/source-code`

`wget https://github.com/Reference-ScaLAPACK/scalapack/archive/v2.2.2.tar.gz`

`tar xzvf v2.2.2.tar.gz`

`cd scalapack-2.2.2`

`cp ~/scripts/workshop/scalapack/SLmake.inc .`

`diff SLmake.inc.example SLmake.inc`

`make lib`

`mkdir -p ~/software/scalapack/2.2.2/lib`

`cp libscalapack.a ~/software/scalapack/2.2.2/lib/`

`mkdir ~/my-module-files/scalapack`

`cp ~/scripts/workshop/scalapack/2.2.2 ~/my-module-files/scalapack/`

`module show scalapack/2.2.2`

`module load scalapack/2.2.2`

## FFTW v3.3.10

`cd ~/source-code`

`wget https://fftw.org/fftw-3.3.10.tar.gz`

`tar xzvf fftw-3.3.10.tar.gz`

`cd fftw-3.3.10`

`cp ~/scripts/workshop/fftw/fftw_gnu_configure.sh .`

`cat -n fftw_gnu_configure.sh`

`./fftw_gnu_configure.sh`

`make`

`make install`

`ls -R ~/software/fftw/3.3.10`

`mkdir ~/my-module-files/fftw`

`cp ~/scripts/workshop/fftw/3.3.10 ~/my-module-files/fftw/`

`module show fftw/3.3.10`

`module load fftw/3.3.10`

## PETSc v3.22.5

`cd ~/source-code`

`wget https://web.cels.anl.gov/projects/petsc/download/release-snapshots/petsc-3.22.5.tar.gz`

`tar xzvf petsc-3.22.5.tar.gz`

`cd petsc-3.22.5`

`cp ~/scripts/workshop/petsc/petsc_gnu_configure.sh .`

`cat -n petsc_gnu_configure.sh`

`./petsc_gnu_configure.sh`

After the configuration has ended, the `configure` script gives us the compilation command, which is `make all` with the `PETSC_DIR` and `PETSC_ARCH` variables set properly. Copy and paste it on your terminal, and execute it.

When compilation has ended, you can install the libraries with the command that is suggested at the end of the build output. It should be similar to the command before, but with `install` argument passed to `make`.

Lots of files have been installed, so we will just check that the library and the headers have been correctly copied:

`ls ~/software/petsc/3.22.5/lib ~/software/petsc/3.22.5/include`

`mkdir ~/my-module-files/petsc`

`cp ~/scripts/workshop/petsc/3.22.5 ~/my-module-files/petsc/`

`module show petsc/3.22.5`

`module load petsc/3.22.5`

## SLEPc v3.22.2

`cd ~/source-code`

`wget https://slepc.upv.es/download/distrib/slepc-3.22.2.tar.gz`

`tar xzvf slepc-3.22.2.tar.gz`

`cd slepc-3.22.2`

`cp ~/scripts/workshop/slepc/slepc_gnu_configure.sh .`

`cat -n slepc_gnu_configure.sh`

`./slepc_gnu_configure.sh`

As was the case with PETSc, the specific build and install lines are suggested on the output of the commands. Copy, paste and execute them successively.

Let's check that it was correctly installed:

`ls ~/software/slepc/3.22.2/lib ~/software/slepc/3.22.2/include`

`mkdir ~/my-module-files/slepc`

`cp ~/scripts/workshop/slepc/3.22.2 ~/my-module-files/slepc/`

`module show slepc/3.22.2`

`module load slepc/3.22.2`

## LibXC v6.2.2

`cd ~/source-code`

`wget https://gitlab.com/libxc/libxc/-/archive/6.2.2/libxc-6.2.2.tar.bz2`

This is a packed file using bzip compression, so we need to unpack it using the `j` argument, instead of `z`, which is for gzip decompression.

`tar xjvf libxc-6.2.2.tar.bz2`

`cd libxc-6.2.2`

`cp ~/scripts/workshop/libxc/libxc_gnu_configure.sh .`

`cat -n libxc_gnu_configure.sh`

`./libxc_gnu_configure.sh`

`make`

`make install`

`ls -R ~/software/libxc/6.2.2`

`mkdir ~/my-module-files/libxc`

`cp ~/scripts/workshop/libxc/6.2.2 ~/my-module-files/libxc/`

`module show libxc/6.2.2`

`module load libxc/6.2.2`

## YAMBO v5.3

`cd ~/source-code`

`git clone https://github.com/yambo-code/yambo.git`

`cd yambo`

We will build the code present in branch 5.3, so we need to switch to that branch:

`git switch 5.3`

`cp ~/scripts/workshop/yambo/yambo_gnu_configure.sh .`

`cat -n yambo_gnu_configure.sh`

`./yambo_gnu_configure`

Read carefully the output of the configuration scripts. All options should have been taken into account (noted by a [X] symbol) and all libraries should have been detected (noted by the [E] symbol). Those libraries which were not detected as already existing, will be compiled (noted by the [C] symbol).

Let's cross fingers and build the core:

`make core`

Ooops! There was a compilation error. Fortunately, after asking in YAMBO forum, we got a fix:

`cp ~/scripts/workshop/yambo/fix-gcc15/symbols.h include/headers/parser/`

`cp ~/scripts/workshop/yambo/fix-gcc15/PARSER_symbols.c src/parser/`

Let's clean our last build:

`make distclean`

And try again:

`./yambo_gnu_configure.sh`

Note that those libraries which were tagged as [C] in our previous attempt, now are tagged as [I], which means that they were already compiled.

`make core`

Great! Let's look at the compiled binaries:

`ls bin`

And copy them to our software directory:

`mkdir -p ~/software/yambo/5.3/bin`

`cp bin/* ~/software/yambo/5.3/bin/`

Finally, copy the ready-made module file:

`mkdir ~/my-module-files/yambo`

`cp ~/scripts/workshop/yambo/5.3 ~/my-module-files/yambo/`

And let's see if it works:

`module load yambo/5.3`

`which yambo`

`yambo --version`
