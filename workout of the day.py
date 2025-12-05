from random import randint
from tkinter import messagebox

workout_type = randint(1, 5)
if (workout_type == 1):
    name_workout = "pushups"
    amount = randint(5, 15)
elif (workout_type == 2):
    name_workout = "situps"
    amount = randint(15, 25)
elif (workout_type == 3):
    name_workout = "squats"
    amount = randint(5, 10)
elif (workout_type == 4):
    name_workout = "weights"
    amount = (str(randint(15, 25)) + " times")
elif (workout_type == 5):
    name_workout = "treadmill"
    amount = (str(randint(15, 20)) + "min")

messagebox.showinfo("workout of the day is: ", str(amount) + " " + name_workout)