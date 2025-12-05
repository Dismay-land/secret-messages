from tkinter import Tk, ttk
root = Tk()
frm = ttk.Frame(root, padding=10)
frm.grid()
ttk.Button(frm, text='OK', command=root.destroy).grid(column=0, row=0)
