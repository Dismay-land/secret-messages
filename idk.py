import tkinter_simplefier as tks
import time as d
app = tks.setup()
app.button("click me...", 0, 0, lambda: hide_button())
def hide_button():
    app.hide
    d.sleep(10)
    app.write("       ...once!        ", 0, 0)
app.run()