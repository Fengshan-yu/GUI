# my calculator

import tkinter as tk

window = tk.Tk()
window.title("My Calculator")


def display(num):
    if len(str(num)) <= 10:
        entry.insert(0, num)
    else:
        inte = str(num).split(".")[0]
        decimal = str(num).split(".")[1]
        if len(decimal) > 1 and int(inte) > 0:
            entry.insert(0, round(num, (10 - len(inte))))
        elif len(decimal) > 1 and int(inte) == 0:
            zeros = decimal.count("0")
            output = f"{decimal[zeros]}.{decimal[(zeros+1):(zeros+4)]}e-{zeros}"
            entry.insert(0, output)
        else:
            output = f"{inte[0]}.{inte[1:5]}e{str(len(inte) - 1)}"
            entry.insert(0, output)

def click(number):
    current = entry.get()
    if "." in current and number == ".":
        pass
    else:
        entry.delete(0, 'end')
        entry.insert(0, str(current) + str(number))

def calculate(method):
    global number_1
    global formula
    number_1 = entry.get()
    entry.delete(0, 'end')
    formula = method

def equal():
    number_2 = entry.get()
    entry.delete(0, 'end')
    if formula == "+":
        result = float(number_1) + float(number_2)
    elif formula == "-":
        result = float(number_1) - float(number_2)
    elif formula == "x":
        result = float(number_1) * float(number_2)
    elif formula == "/" and float(number_2) != 0:
        result = float(number_1) / float(number_2)
    elif formula == "/" and float(number_2) == 0:
        entry.insert(0, "Error")
    elif formula == "**":
        result = float(number_1) ** float(number_2)
    elif formula == "CR":
        result = round(float(number_1) ** (1. / 3.), 2)
    elif formula == "RE" and float(number_1) == 0:
        entry.insert(0, "Error")
    elif formula == "RE" and float(number_1) != 0:
        result = 1 / float(number_1)
    display(result)

def clear():
    entry.delete(0, "end")

entry = tk.Entry(window)
entry.grid(row=0, column=0, padx=20, pady=10, columnspan=4)

button_1 = tk.Button(window, text="1", padx=20, pady=10, width=1, command=lambda: click(1))
button_2 = tk.Button(window, text="2", padx=20, pady=10, width=1, command=lambda: click(2))
button_3 = tk.Button(window, text="3", padx=20, pady=10, width=1, command=lambda: click(3))
button_4 = tk.Button(window, text="4", padx=20, pady=10, width=1, command=lambda: click(4))
button_5 = tk.Button(window, text="5", padx=20, pady=10, width=1, command=lambda: click(5))
button_6 = tk.Button(window, text="6", padx=20, pady=10, width=1, command=lambda: click(6))
button_7 = tk.Button(window, text="7", padx=20, pady=10, width=1, command=lambda: click(7))
button_8 = tk.Button(window, text="8", padx=20, pady=10, width=1, command=lambda: click(8))
button_9 = tk.Button(window, text="9", padx=20, pady=10, width=1, command=lambda: click(9))
button_0 = tk.Button(window, text="0", padx=20, pady=10, width=1, command=lambda: click(0))
button_1.grid(row=1, column=0)
button_2.grid(row=1, column=1)
button_3.grid(row=1, column=2)
button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)
button_7.grid(row=3, column=0)
button_8.grid(row=3, column=1)
button_9.grid(row=3, column=2)
button_0.grid(row=4, column=0)

button_add = tk.Button(window, text="+", padx=20, pady=10, width=1, command=lambda: calculate("+"))
button_minus = tk.Button(window, text="-", padx=20, pady=10, width=1, command=lambda: calculate("-"))
button_multi = tk.Button(window, text="x", padx=20, pady=10, width=1, command=lambda: calculate("x"))
button_divide = tk.Button(window, text="/", padx=20, pady=10, width=1, command=lambda: calculate("/"))
button_power = tk.Button(window, text="成方", padx=20, pady=10, width=1, command=lambda: calculate("**"))
button_cubic_root = tk.Button(window, text="立方根", padx=20, pady=10, width=1, command=lambda: calculate("CR"))
button_reciprocal = tk.Button(window, text="倒数", padx=20, pady=10, width=1, command=lambda: calculate("RE"))
button_dot = tk.Button(window, text='.', padx=20, pady=10, width=1, command=lambda: click("."))
button_clear = tk.Button(window, text='C', padx=20, pady=10, width=1, command=clear)
button_equal = tk.Button(window, text="=", padx=20,
                         pady=10, width=1, bg="white", fg="green", command=equal)
button_add.grid(row=1, column=3)
button_minus.grid(row=2, column=3)
button_multi.grid(row=3, column=3)
button_divide.grid(row=4, column=3)
button_power.grid(row=5, column=0)
button_cubic_root.grid(row=5, column=1)
button_reciprocal.grid(row=5, column=2)
button_equal.grid(row=5, column=3)
button_dot.grid(row=4, column=1)
button_clear.grid(row=4, column=2)

window.mainloop()
