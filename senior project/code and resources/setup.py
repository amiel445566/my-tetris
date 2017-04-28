import sys
from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need fine tuning.
build_exe_options = {"optimize": 2,
                     "packages": ["dbm"],
                     "include_files": ["image(s)", "font(s)", "db"]
                     }

setup(  name = "Tetris Code",
        version = "3.6",
        options = {"build_exe": build_exe_options},
        description = "My take on Tetris.",
        executables = [Executable("tetris_code.py", base="Win32GUI", icon="image(s)\\logo.ico")])
