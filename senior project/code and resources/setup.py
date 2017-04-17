import sys
from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need fine tuning.
build_exe_options = {"optimize": 2, }

setup(  name = "Tetris Code",
        version = "3.6",
        description = "My take on Tetris.",
        executables = [Executable("tetris_code.py", base="Win32GUI")])
