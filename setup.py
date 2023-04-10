import sys
from cx_Freeze import *

# Dependencies are automatically detected, but it might need fine tuning.
excludes = ['unicodedata', 'logging', 'unittest', 'email', 'html', 'http', 'urllib',
            'xml', 'bz2']
executables=[Executable('JustAGame.py',icon='GayIntro2.ico')]
# GUI applications require a different base on Windows (the default is for a
# console application).
include_files=['gay_gf.py','GayIntro2.bmp','intro.py','button.py','gay_gf.py',
               
               'lolly.bmp','person.py','press.py','player.bmp','lol.py','xmas.bmp']
options={'build_exe':{'include_files':include_files,'excludes':excludes
    }
    }

setup(  name = "JustAGame",
        version = "0.0.1",
        description = "Oh shit!",
        executables=executables,
        options=options
        )
        #options = {"build_exe": {'packages':['pygame'],
        #'include_files':['gay_gf.py','GayIntro2.bmp','intro.py',
        #'lol.py','preson.py','press.py','player.bmp','lol.py']}},
