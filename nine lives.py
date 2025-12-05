import random as r
from tkinter import simpledialog, messagebox
lives = 9
words = ['pizza', 'fairy', 'teeth', 'shirt', 'otter', 'plane', 'candy', 'pillow', 'socks', 'sweater', 'turtle', 'giraffe', 'elephant', 'pasta', 'donut', 'cupcake', 'banana', 'apple', 'orange', 'grape', 'watermelon', 'kiwi', 'strawberry', 'blueberry', 'raspberry', 'peach', 'pear', 'plum', 'cherry']
secret_word = r.choice(words)
clue =[]
index= 0
while index < len(secret_word):
    clue.append('?')
    index += 1
    debug = clue
heart = '❤️'
guessed_word_corectley = False
def update_clue(guessed_letter,secret_word, clue):
    index = 0
    while index < len(secret_word):
        if secret_word[index] == guessed_letter:
            clue[index] = guessed_letter
        index += 1
        
while lives > 0:
    messagebox.showinfo(debug) # print(clue)
    messagebox.showinfo('lives left: ' + str(lives) + heart * lives) # print('lives left: ' + str(lives) + heart * lives)
    guess = simpledialog.askstring('get', 'guess a letter or a whole word: ')#input('guess a letter or a whole word: ')
    if guess == secret_word:
        guessed_word_corectley = True
        break
    if guess in secret_word:
        update_clue(guess,secret_word, clue)
    else:
        lives -= 1
        
if guessed_word_corectley:
    messagebox.showinfo('you won! the secret word was: ' + secret_word)
else:
    messagebox.showinfo('you lost! the secret word was: ' + secret_word)