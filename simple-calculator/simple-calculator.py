from tkinter import *

app = Tk()
app.title("My Calculator")
app.geometry("300x400")
app.config(background="#8997e0")


expression = ""


def click(num):
    exp = entry_field.get()
    entry_field.delete(0, END)
    entry_field.insert(0, str(exp) + str(num))

def operate(operator):
    global expression
    expression = entry_field.get()
    entry_field.delete(0, END)
    entry_field.insert(0, operator)

def clear():
    entry_field.delete(0, END)

def calculate():
    second_num = entry_field.get()
    entry_field.delete(0, END)

    try:
        result = eval(expression + str(second_num))
        entry_field.insert(0, result)
    except:
        entry_field.insert(0, "Error")


entry_field = Entry(app, width=20, justify="right", borderwidth=5)
entry_field.grid(row=0, column=0, columnspan=4, ipadx=10, pady=10)


buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', 'C', '=', '+'
]

row_val = 1
col_val = 0

for button in buttons:
    if button == 'C':
        btn = Button(app, text=button, height=1, width=5, padx=10, pady=10, command=clear)
    elif button == '=':
        btn = Button(app, text=button, height=1, width=5, padx=10, pady=10, command=calculate)
    else:
        btn = Button(app, text=button, height=1, width=5, padx=10, pady=10, command=lambda b=button: click(b) if b.isdigit() or b == '.' else operate(b))

    btn.grid(row=row_val, column=col_val)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

app.mainloop()
#Fahad-Ullah