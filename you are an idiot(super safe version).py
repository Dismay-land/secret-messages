import tkinter_simplefier as tks
import subprocess
import os

# Build an absolute path to idiot.mp3 (always works if it's in the same folder)
import os
import sys

# When bundled by PyInstaller, resources are in sys._MEIPASS.
if getattr(sys, "frozen", False):
    base = sys._MEIPASS
else:
    base = os.path.dirname(__file__)

sound_path = os.path.join(base, "idiot.mp3")

r = 6
def makemore():
    for r in range(6):
        newwindow = tks.setup()
        newwindow.title("You are an idiot")
        newwindow.write("You are an idiot", 0, 0)
        newwindow.write("  🙂🙂🙂", 0, 1)
        newwindow.write("you are an idiot", 0, 2)
        newwindow.button("click to close", 0, 3, makemore)
        subprocess.Popen(["afplay", sound_path])  # play sound on new windows too
        r=r+6
    newwindow.run()
    makemore()

for i in range(1):
    mygui = tks.setup()
    subprocess.Popen(["afplay", sound_path])  # play sound when windows open
    mygui.title("You are an idiot")
    mygui.write("You are an idiot", 0, 0)
    mygui.write("You are an idiot", 0, 1)
    mygui.write("You are an idiot", 0, 2)
    mygui.button("click to close", 0, 3, makemore)
mygui.run()
makemore()
