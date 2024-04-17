# Setup build file for compile .py to .exe
from cx_Freeze import setup, Executable


build_exe_options = {
    "packages": ["PIL"],
    "include_files": ["functions/", "ressources/"],
}

setup(
    name = "SystemItium",
    version = "0.1",
    description = "Application allowing quick installation of software needed to code projects in Python and C/C++.",
    options = {"build_exe": build_exe_options},
    executables = [Executable("main.py", base="Win32GUI", icon="./ressources/logo_sistemitium.ico")]
)