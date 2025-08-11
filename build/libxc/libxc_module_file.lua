whatis("Name: libxc")
whatis("Version: 6.2.2")
whatis("Category: Lmod/Modulefiles")
whatis("Description: built with oneapi/2025.0")

local BASE = "/path/to/libxc"

setenv("LIBXC_DIR",BASE)

prepend_path("PATH",BASE.."/bin")
prepend_path("CPATH",BASE.."/include")
prepend_path("LIBRARY_PATH",BASE.."/lib")
prepend_path("LD_LIBRARY_PATH",BASE.."/lib")
