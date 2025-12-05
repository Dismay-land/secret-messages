import tkinter_simplefier as tks
import time as t


for i in range(10000000000000000000000000000000000000000000000000000000):
    root = tks.setup()
    root.title(f"Window {i + 1}")
    root.write(f"This is window {i + 1}", 0, 0)
    root.button("Close", 0, 1, root.destroy)
t.sleep(0.1)  # Adding a small delay to avoid overwhelming the system
root.run()
root.destroy()
root.run()