import tkinter_simplefier as tks

my_gui = tks.setup()
other_gui = tks.setup()
my_gui.hide()
other_gui.button('show', 0, 0, lambda: my_gui.show())
my_gui.write('hello', 0, 0)
my_gui.button('click me', 0, 1, lambda: my_gui.write('you clicked me!', 0, 2))
my_gui.button('hide', 0, 3, my_gui.hide)
my_gui.button('delete', 0, 4, lambda: my_gui.destroy())

scroll = tks.ScrollTK()  # Create an instance
scroll.AddText('this uses a scrollTK.AddText method to add text to the scrolled text widget', 'true')

my_gui.run()
