import tkinter_simplefier as tks
import random as r
num = r.randint(1, 6)
root = tks.setup()
def roll():
    num = r.randint(1, 6)
    roll = 'you rolled a' + num
    root.destroy()
    root = tks.setup()
    root.write(roll, 0, 0)
root.write('you rolled a ', 0, 0)
root.write(num, 0, 1)
root.button('roll again', 0, 2, roll)
root.run()
    