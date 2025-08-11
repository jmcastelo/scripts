whatis("Name: netcdf-fortran")
whatis("Version: 4.6.2")
whatis("Category: Lmod/Modulefiles")
whatis("Description: built with oneapi/2025.0 + mpi/2021.14 + phdf5/1.14.6 + netcdf-c/4.9.3")

local BASE = "/path/to/netcdf-fortran"

setenv("NFDIR",BASE)

prepend_path("PATH",BASE.."/bin")
prepend_path("CPATH",BASE.."/include")
prepend_path("LIBRARY_PATH",BASE.."/lib")
prepend_path("LD_LIBRARY_PATH",BASE.."/lib")
