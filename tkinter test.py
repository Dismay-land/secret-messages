import tkinter_simplefier as tks
from random import randint


def start():
    
    def do():
        def randomACTION():
            bring = randint(0, 1)
            if bring == 1:
                my_gui.show()
                other_gui.destroy()
                scamGUI.destroy()
            else:
                my_gui.destroy()
                other_gui.destroy()
                scamGUI.write('you lost your original GUI!', 0, 1)
                scamGUI.button('ok', 0, 2, scamGUI.destroy)
                
        scamGUI = tks.setup()
        scamGUI.title('scam GUI')
        scamGUI.write("G3T SC4MN3D!!!!1!!! it's a 50/50 chance to get it back, or lose it all.", 0, 0)
        scamGUI.button('ok', 0, 1, lambda: randomACTION())
    my_gui.hide()
    other_gui = tks.setup()
    other_gui.title('defenetliely not a scam!')
    other_gui.write('the original GUI is gone, deleted! press the button to bring it back.', 0, 0)
    other_gui.button('bring back NOW!!!', 0, 1, lambda: do())
    other_gui.run()
    
my_gui = tks.setup()
my_gui.title('first menu')
my_gui.write('MY MENU', 0, 0)
my_gui.button('Button1', 0, 1, lambda: my_gui.write('Button1 pressed', 0, 2))
my_gui.button('Button2', 0, 3, lambda: my_gui.write('button2 pressed', 0, 4))
my_gui.button('Button3', 0, 5, lambda: start())
my_gui.button('Exit', 0, 7, my_gui.destroy)
my_gui.run()