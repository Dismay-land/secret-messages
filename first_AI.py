from tkinter import Tk, ttk, simpledialog, messagebox
from random import choice
from datetime import datetime

class runAi:
    def __init__(self, run):
        if run == 1:
            pass
        else:
            print(" ")
            

def setup():
    root = Tk()
    frm = ttk.Frame(root, padding=10)
    frm.grid()
    root.title("DimaGPT options")
    ttk.Label(frm, text="exit").grid(column=0, row=0)
    ttk.Label(frm, text="what is your name").grid(column=1, row=1)
    ttk.Label(frm, text="how are you").grid(column=0, row=2)
    ttk.Label(frm, text="what can you do").grid(column=1, row=3)
    ttk.Label(frm, text="*nothing*").grid(column=0, row=4)
    ttk.Label(frm, text="*any math question*").grid(column=1, row=5)
    ttk.Label(frm, text="im impressed").grid(column=0, row=6)
    ttk.Label(frm, text="tell me a joke").grid(column=1, row=7)
    ttk.Label(frm, text="what is the meaning of life").grid(column=0, row=8)
    ttk.Label(frm, text="what time is it").grid(column=1, row=9)
    ttk.Label(frm, text="flip a coin").grid(column=0, row=10)
    ttk.Label(frm, text="roll a dice").grid(column=1, row=11)
    ttk.Label(frm, text="what is your favorite color").grid(column=0, row=12)
    ttk.Label(frm, text="sing me a song").grid(column=1, row=13)
    ttk.Label(frm, text="tell me a fun fact").grid(column=0, row=14)
    ttk.Label(frm, text="what's your favorite food").grid(column=1, row=15)
    ttk.Label(frm, text="can you dance").grid(column=0, row=16)
    ttk.Label(frm, text="what is the periodic table").grid(column=1, row=17)
    ttk.Label(frm, text="tell me one of the elements in the periodic table").grid(column=0, row=18)
    ttk.Label(frm, text="im fine").grid(column=1, row=19)
setup()

# This is a simple AI program that can answer questions and perform math operations.

greetings = ([
    "Hello,", "Hi,", "Hey,", "Howdy,", "Greetings,", 
    "Salutations,", "What's up,", "Good day,", "Yo,", "Hiya,"
])
greetings = choice(greetings)
questions = [
    "how may i help you?", 
    "what do you need?", 
    "what can i do for you?", 
    "how can i assist you?", 
    "do you have a question for me?", 
    "what's on your mind?", 
    "is there something you'd like to know?", 
    "how can I make your day better?", 
    "what would you like to ask?", 
    "is there anything I can help you with?"
]

elements = [
            "Hydrogen (H)", "Helium (He)", "Lithium (Li)", "Beryllium (Be)", 
            "Boron (B)", "Carbon (C)", "Nitrogen (N)", "Oxygen (O)", 
            "Fluorine (F)", "Neon (Ne)", "Sodium (Na)", "Magnesium (Mg)",
            "Aluminum (Al)", "Silicon (Si)", "Phosphorus (P)", 
            "Sulfur (S)", "Chlorine (Cl)", "Argon (Ar)"
            "Potassium (K)", "Calcium (Ca)", "Scandium (Sc)",
            "Titanium (Ti)", "Vanadium (V)", "Chromium (Cr)",
            "Manganese (Mn)", "Iron (Fe)", "Cobalt (Co)",
            "Nickel (Ni)", "Copper (Cu)", "Zinc (Zn)", "Gallium (Ga)",
            "Germanium (Ge)", "Arsenic (As)", "Selenium (Se)",
            "Bromine (Br)", "Krypton (Kr)", "Rubidium (Rb)",
            "Strontium (Sr)", "Yttrium (Y)", "Zirconium (Zr)",
            "Niobium (Nb)", "Molybdenum (Mo)", "Technetium (Tc)",
            "Ruthenium (Ru)", "Rhodium (Rh)", "Palladium (Pd)",
            "Silver (Ag)", "Cadmium (Cd)", "Indium (In)",
            "Tin (Sn)", "Antimony (Sb)", "Tellurium (Te)",
            "Iodine (I)", "Xenon (Xe)", "Cesium (Cs)",
            "Barium (Ba)", "Lanthanum (La)", "Cerium (Ce)",
            "Praseodymium (Pr)", "Neodymium (Nd)", "Promethium (Pm)",
            "Samarium (Sm)", "Europium (Eu)", "Gadolinium (Gd)",
            "Terbium (Tb)", "Dysprosium (Dy)", "Holmium (Ho)",
            "Erbium (Er)", "Thulium (Tm)", "Ytterbium (Yb)",
            "Lutetium (Lu)", "Hafnium (Hf)", "Tantalum (Ta)",
            "Tungsten (W)", "Rhenium (Re)", "Osmium (Os)",
            "Iridium (Ir)", "Platinum (Pt)", "Gold (Au)",
        ]
questions = choice(questions)

goodbye = ["goodbye", "see you later", "bye", "take care", "farewell", "adieu", "later", "peace out", "catch you later", "so long"]

def count_elements(elements):
    some_elments = []
    for counter in range(0, 21):
        random_element = choice(elements)
        some_elments.append(random_element)
    return some_elments

def get_question(greet, ask, goodbyes):
    question = simpledialog.askstring("question", greet + " " + ask)
    if "xit" in question:
        messagebox.showinfo("goodbye", choice(goodbyes))
        exit()
    return question

def solve_question(question):
    if question == "what is your name":
        return "My name is DimaGPT, Im still in Beta version so don't expect me to answer anything."
    elif question == "how are you":
        return "I'm just a computer program, but I'm here to help!"
    elif question == "what can you do":
        return "I can assist you with various tasks and answer questions."
    elif question == "":
        return "I'm not sure how to respond to that."
    elif question == "im impressed":
        return "Thank you! I'm glad to hear that."
    elif question == "tell me a joke":
        jokes = [
            "Why don't scientists trust atoms? Because they make up everything!",
            "Why did the scarecrow win an award? Because he was outstanding in his field!",
            "Why don't skeletons fight each other? They don't have the guts!",
            "Why did the bicycle fall over? Because it was two-tired!",
            "Why can't your nose be 12 inches long? Because then it would be a foot!",
            "Why did the math book look sad? Because it had too many problems!    ",
            "Why was the computer cold? It left its Windows open!",
            "Why did the golfer bring two pairs of pants? In case he got a hole in one!",
            "Why don't eggs tell jokes? They might crack up!",
            "Why did the tomato turn red? Because it saw the salad dressing!",
            "why don't programmers like nature? It has too many bugs!",
        ]
        jokes = choice(jokes)
        return jokes
    elif question == "what is the meaning of life":
        return "42. According to The Hitchhiker's Guide to the Galaxy, that's the answer to life, the universe, and everything."
    elif question == "what time is it":
        return "The current time is " + datetime.now().strftime("%H:%M")
    elif "flip" in question:
        return "Heads" if choice([True, False]) else "Tails"
    elif question == "roll a dice":
        return f"You rolled a {choice([1, 2, 3, 4, 5, 6])}"
    elif question == "what is your favorite color":
        return "I don't have eyes, but if I did, I'd probably like blue. It's calming!"
    elif "song" in question:
        return "I'm not much of a singer, but here's a classic: 'Twinkle, twinkle, little star...'"
    elif "fun" in question:
        facts = [
            "Honey never spoils. Archaeologists have found pots of honey in ancient Egyptian tombs that are over 3,000 years old and still perfectly edible.",
            "Octopuses have three hearts and blue blood.",
            "Bananas are berries, but strawberries aren't.",
            "A day on Venus is longer than a year on Venus.",
            "Sharks existed before trees."
            "A group of jellyfish is called a 'smack.'",
            "A group of flamingos is called a 'flamboyance.'",
            "Wombat poop is cube-shaped.",
            "The Eiffel Tower can be 15 cm taller during the summer due to thermal expansion.",
            "Sloths can hold their breath longer than dolphins—up to 40 minutes.",
            "There are more stars in the universe than grains of sand on Earth.",
            "Butterflies can taste with their feet.",
            "The heart of a blue whale is so large that a human could swim through its arteries.",
            "Some cats are allergic to humans.",
            "The inventor of the Pringles can is buried in one.",
            "A day on Mercury lasts 1,408 hours."
        ]
        return choice(facts)
    elif question == "what's your favorite food":
        return "I don't eat, but I hear pizza is pretty popular!"
    elif question == "can you dance":
        return "I can't dance, but I can imagine doing the robot!"
    elif question == "what is the periodic table":
        return "The periodic table is a tabular arrangement of chemical elements, organized by their atomic number, electron configuration, and recurring chemical properties. It provides a useful framework for analyzing chemical behavior."
    elif "tell me one" in question:
        return "i could, but there is so much of them, it will be a pain to countinously repeat a question, so here a re 20 of them!" + str(count_elements(elements)) 
    elif "fi" in question:
        return "That's great to hear! If you have any questions or need assistance, feel free to ask."
    if ("+" in question):
        numbers = question.split("+")
        try:
            num1 = int(numbers[0])
            num2 = int(numbers[1])
            return str(num1 + num2)
        except ValueError:
            return "Please enter valid numbers."
    elif ("-" in question):
        numbers = question.split("-")
        try:
            num1 = int(numbers[0])
            num2 = int(numbers[1])
            return str(num1 - num2)
        except ValueError:
            return "Please enter valid numbers."
    
    elif ("*" in question):

        numbers = question.split("*")
        try:
            num1 = int(numbers[0])
            num2 = int(numbers[1])
            return str(num1 * num2)
        except ValueError:
            return "Please enter valid numbers."
    elif ("/" in question):
        numbers = question.split("/")

        try:
            num1 = int(numbers[0])
            num2 = int(numbers[1])
            return str(num1 / num2)
        except ValueError:
            return "Please enter valid numbers."
    else:
        return "I don't understand that question. please do not include letters when giving math problems, such as: what is, whats, what's, etc.. use '*'(shift + 8) for multiplication, and '/' for division. use '-' for subtraction, and '+' (shift + =) for addition."
while True:
    messagebox.showinfo("answer", solve_question(get_question(greetings, questions, goodbye)))
    