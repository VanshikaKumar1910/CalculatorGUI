from tkinter import *
import math


def button_click(value):
    current = result_label.cget("text")
    if current == "0" or current == "Error":
        result_label.config(text=value)
    else:
        result_label.config(text=current + value)


def calculate():
    try:
        expression = result_label.cget("text")
        expression = expression.replace('^', '**')  # Handle exponentiation
        result = eval(expression)
        result_label.config(text=str(result))
    except Exception:
        result_label.config(text="Error")


def clear_display():
    result_label.config(text="0")


def scientific_operation(op):
    current = result_label.cget("text")
    try:
        if op == 'sqrt':
            result = math.sqrt(float(current))
        elif op == 'log':
            result = math.log10(float(current))
        elif op == 'ln':
            result = math.log(float(current))
        elif op == 'sin':
            result = math.sin(math.radians(float(current)))
        elif op == 'cos':
            result = math.cos(math.radians(float(current)))
        elif op == 'tan':
            result = math.tan(math.radians(float(current)))
        elif op == 'exp':
            result = math.exp(float(current))
        result_label.config(text=str(result))
    except Exception:
        result_label.config(text="Error")


root = Tk()
root.title('Scientific Calculator')
root.geometry('400x600')
root.resizable(False, False)
root.configure(bg='white')

result_label = Label(
    root,
    text='0',
    font=('Arial', 20, 'bold'),
    bg='white',
    fg='black',
)
result_label.grid(row=0, column=0, columnspan=5, pady=(20, 25), sticky="nsew")

buttons = [
    '7', '8', '9', '/', 'sqrt', '4', '5', '6', '*', 'log', '1', '2', '3', '-',
    'ln', '0', '.', '=', '+', 'exp', 'sin', 'cos', 'tan', '(', ')', 'C'
]

row_val = 1
col_val = 0

for button in buttons:
    if button == 'C':
        btn = Button(root,
                     text=button,
                     bg='#ff6f61',
                     fg='white',
                     font=('Arial', 12, 'bold'),
                     width=8,
                     height=2,
                     command=clear_display)
    elif button in {'=', 'sqrt', 'log', 'ln', 'sin', 'cos', 'tan', 'exp'}:
        btn = Button(root,
                     text=button,
                     bg='#00a65a',
                     fg='whitesmoke',
                     font=('Arial', 12, 'bold'),
                     width=8,
                     height=2,
                     command=lambda b=button: scientific_operation(b)
                     if b != '=' else calculate())
    else:
        btn = Button(root,
                     text=button,
                     bg='#00a65a',
                     fg='whitesmoke',
                     font=('Arial', 12, 'bold'),
                     width=8,
                     height=2,
                     command=lambda b=button: button_click(b))

    btn.grid(row=row_val, column=col_val, padx=5, pady=5)
    col_val += 1
    if col_val > 4:
        col_val = 0
        row_val += 1

for i in range(5):
    root.grid_columnconfigure(i, weight=1)
    root.grid_rowconfigure(i + 1, weight=1)

root.mainloop()
