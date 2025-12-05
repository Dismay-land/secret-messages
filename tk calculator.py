from tkinter import simpledialog, messagebox
# functions \/
def get_operator():
    operator = simpledialog.askstring("get data", "Enter the operator ('+'/'-'/'x'/'/') or type nothing to end: ")
    if operator == '':
        exit()
    return operator

def get_first_number():
    first_number = simpledialog.askinteger('get data', 'Enter the first number: ')
    return first_number

def get_second_number():
    second_number = simpledialog.askinteger('get data', 'Enter the second number: ')
    return second_number

def show_answer():
    if operator == '+':
        answer = fnumber + snumber
    elif operator == '-':
        answer = fnumber - snumber
    elif operator == 'x':
        answer = fnumber * snumber
    elif operator == '/':
        if snumber == 0:
            messagebox.showerror('error', 'cant divide by 0 (INfInitY)')
            exit()
        answer = fnumber / snumber  
    return answer
# main loop / main code \/
while True:
    operator = get_operator()
    fnumber = get_first_number()
    snumber = get_second_number()
    answer = show_answer()
    messagebox.showinfo('answer', 'the answer is: ' + str(answer))