from tkinter import messagebox, simpledialog

word_replacements = {
    'a': '4',
    'b': '8',
    'c': '<',
    'd': '|)',
    'e': '3',
    'f': '|=',
    'g': '9',
    'h': '#',
    'i': '1',
    'j': '_|',
    'k': '|<',
    'l': '|_',
    'm': '|\/|',
    'n': '|\/',
    'o': '0',
    'p': '|*',
    'q': '(,)',
    'r': '|2',
    's': '$',
    't': '+',
    'u': '|_|',
    'v': '\/',
    'w': '\/\/',
    'x': '}{',
    'y': '`/',
    'z': '2',
    ' ': ' '
}
word_setups = {
    '4': 'a',
    '8': 'b',
    '<': 'c',
    '|)': 'd',
    '3': 'e',
    '|=': 'f',
    '9': 'g',
    '#': 'h',
    '1': 'i',
    '_|': 'j',
    '|<': 'k',
    '|_': 'l',
    '|\/|': 'm',
    '|\/': 'n',
    '0': 'o',
    '|*': 'p',
    '(,)': 'q',
    '|2': 'r',
    '$': 's',
    '+': 't',
    '|_|': 'u',
    '\/': 'v',
    '\/\/': 'w',
    '}|{': 'x',
    '`/': 'y',
    '2': 'z'
}   

def get_task():
    task = simpledialog.askstring('Task', "encrypt or decrypt (e/d): ")
    if 'e' in task:
        word = simpledialog.askstring('Task', 'Enter the message: ')
        amount = len(word)
        for counter in range(0, amount):
            letter = word[counter]
            if letter in word_replacements:
                word = word.replace(letter, word_replacements[letter])   
    elif 'd' in task:
        word = simpledialog.askstring('Task', 'Enter the message: ')
        amount = len(word)
        for counter in range(0, amount):
            letter = word[counter]
            if letter in word_setups:
                word = word.replace(letter, word_setups[letter])
    else:
        pass
    return word

while True:
    task = get_task()
    if task == 'exit':
        break
    messagebox.showinfo('your new sentence/word is: ', task)   