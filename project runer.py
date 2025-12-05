import tkinter_simplefier as tks
import tkinter as tk
import subprocess

def AI():
    # Hide the main window when starting the AI process
    my_gui.root.withdraw()

    # Run the AI script in a new process
    process = subprocess.Popen(["python3", "first_AI.py"])

    # Periodically check if the AI process is still running
    def check_process():
        if process.poll() is not None:  # If process has finished
            my_gui.root.deiconify()  # Show the main window again
        else:
            # Check again in 500ms if the process is still running
            my_gui.root.after(500, check_process)

    # Start checking the process
    check_process()

def rps():
    # Hide the main window when starting the AI process
    my_gui.root.withdraw()

    # Run the AI script in a new process
    process = subprocess.Popen(["python3", "RPS.py"])

    # Periodically check if the AI process is still running
    def check_process():
        if process.poll() is not None:  # If process has finished
            my_gui.root.deiconify()  # Show the main window again
        else:
            # Check again in 500ms if the process is still running
            my_gui.root.after(500, check_process)

    # Start checking the process
    check_process()

def workout():
    # Hide the main window when starting the AI process
    my_gui.root.withdraw()

    # Run the AI script in a new process
    process = subprocess.Popen(["python3", "workout of the day.py"])

    # Periodically check if the AI process is still running
    def check_process():
        if process.poll() is not None:  # If process has finished
            my_gui.root.deiconify()  # Show the main window again
        else:
            # Check again in 500ms if the process is still running
            my_gui.root.after(500, check_process)

    # Start checking the process
    check_process()

my_gui = tks.setup()
my_gui.write('What would you like to run?', 0, 0)
my_gui.button('Run AI', 0, 1, AI)
my_gui.button('run RPS', 0, 2, rps)
my_gui.button('workout of the day', 0, 3, workout)
my_gui.run()
