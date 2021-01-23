from cx_Freeze import *
import platform
import sys

includefiles = ['qr1.ico','qr2.ico']

base =None
if sys.platform == 'win32':
    base = "Win32GUI"

shortcut_table =[
    ("DesktopShortcut",
     "DesktopFolder",
     "Qr Generator",
     "TARGETDIR",
     "TARGETDIR\main.exe",
     None,
     None,
     None,
     None,
     None,
     None,
     "TARGETDIR"

     )
]
msi_data={"Shortcut" : shortcut_table}

bdist_msi_option = {'data': msi_data}

setup(
    varsion ="1.0",
    description ="Qr Generator Software",
    author="RB group",
    name = "Qr generator with security scan",
    options={'build_exe':{'include_files': includefiles},'bdist_msi':bdist_msi_option},
    excutables=[
        Executable(
            script="main.py",
            base=base,
            icon='qr2.ico'
        )
    ]



)
