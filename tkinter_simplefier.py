# # tkinter_simplefier.py
# This is an extension pack for tkinter, designed to make runs easier

from tkinter import Tk, ttk, scrolledtext

class ScrollTK:
    def __init__(self):
        self.root = Tk()
        self.frm = ttk.Frame(self.root, padding=10)
        self.frm.grid()
        self.text = scrolledtext.ScrolledText(self.frm, width=40, height=10)
        self.text.grid(column=0, row=0)
        self.text.insert('1.0', 'hello.')
    def AddText(self, text, next_line):
        if next_line == 'true':
            self.text.insert('end', '\n' + text)
        else:
            self.text.insert('end', text)
            
    # def padding(self, padding, scrollpading):
    #     self.frm['padding'] = (padding, padding)
    #     self.text['padding'] = (scrollpading, scrollpading)
        

class setup:
    def __init__(self):
        self.root = Tk()
        self.frm = ttk.Frame(self.root, padding=10)
        self.frm.grid()

    def write(self, btext, column2, row2):
        label = ttk.Label(self.frm, text=btext)
        label.grid(column=column2, row=row2)

    def button(self, btext, column2, row2, command):
        btn = ttk.Button(self.frm, text=btext, command=command)
        btn.grid(column=column2, row=row2)

    def run(self):
        self.root.mainloop()
        
    def title(self, title):
        self.root.title(title)
        
    def hide(self):
        self.root.withdraw()
        
    def show(self):
        self.root.deiconify()
        
    def destroy(self):
        self.root.destroy()

# Optional utility class to just run a mainloop
# class LoopIt:
#     def __init__(self, root):
#         root.mainloop()