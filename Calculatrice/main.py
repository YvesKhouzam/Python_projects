from tkinter import *

root = Tk()
root.title("Calculatrice")

e = Entry(root, width=50, borderwidth=5)
e.grid(row=0, column=0, columnspan=4, padx=10, pady=10)


def button_click(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))
    return


def button_clear():
    e.delete(0, END)


def button_add():
    first_number = e.get()
    global f_num, operation
    f_num = float(first_number)
    e.delete(0, END)
    operation = "+"


def button_min():
    first_number = e.get()
    global f_num, operation
    f_num = float(first_number)
    e.delete(0, END)
    operation = "-"


def button_mul():
    first_number = e.get()
    global f_num, operation
    f_num = float(first_number)
    e.delete(0, END)
    operation = "*"


def button_div():
    first_number = e.get()
    global f_num, operation
    f_num = float(first_number)
    e.delete(0, END)
    operation = "/"


def button_equal():
    second_number = float(e.get())
    e.delete(0, END)
    if operation == "+":
        e.insert(0, f_num + second_number)
    if operation == "-":
        e.insert(0, f_num - second_number)
    if operation == "*":
        e.insert(0, f_num * second_number)
    if operation == "/":
        e.insert(0, f_num / second_number)


def button_opp():
    temp_num = e.get()
    e.delete(0, END)
    e.insert(0, float(temp_num) * -1)


# Define Buttons

button_1 = Button(root, text="1", padx=40, pady=20, command=lambda: button_click(1))
button_2 = Button(root, text="2", padx=40, pady=20, command=lambda: button_click(2))
button_3 = Button(root, text="3", padx=40, pady=20, command=lambda: button_click(3))
button_4 = Button(root, text="4", padx=40, pady=20, command=lambda: button_click(4))
button_5 = Button(root, text="5", padx=40, pady=20, command=lambda: button_click(5))
button_6 = Button(root, text="6", padx=40, pady=20, command=lambda: button_click(6))
button_7 = Button(root, text="7", padx=40, pady=20, command=lambda: button_click(7))
button_8 = Button(root, text="8", padx=40, pady=20, command=lambda: button_click(8))
button_9 = Button(root, text="9", padx=40, pady=20, command=lambda: button_click(9))
button_0 = Button(root, text="0", padx=40, pady=20, command=lambda: button_click(0))

button_clear = Button(root, width=15, text="C", padx=40, pady=20, command=button_clear)
button_equal = Button(root, width=15, text="=", padx=39, pady=20, command=button_equal)

button_plus = Button(root, text="+", padx=39, pady=20, command=button_add)
button_min = Button(root, text="-", padx=39, pady=20, command=button_min)
button_mul = Button(root, text="*", padx=39, pady=20, command=button_mul)
button_div = Button(root, text="/", padx=39, pady=20, command=button_div)
button_opp = Button(root, text="+/-", padx=39, pady=20, command=button_opp)

# Display Buttons on the screen

button_clear.grid(row=1, column=0, columnspan=2, padx=5, pady=5)
button_div.grid(row=1, column=3, padx=5, pady=5)

button_mul.grid(row=2, column=3, padx=5, pady=5)
button_7.grid(row=2, column=0, padx=5, pady=5)
button_8.grid(row=2, column=1, padx=5, pady=5)
button_9.grid(row=2, column=2, padx=5, pady=5)

button_4.grid(row=3, column=0, padx=5, pady=5)
button_6.grid(row=3, column=2, padx=5, pady=5)
button_min.grid(row=3, column=3, padx=5, pady=5)
button_5.grid(row=3, column=1, padx=5, pady=5)

button_1.grid(row=4, column=0, padx=5, pady=5)
button_2.grid(row=4, column=1, padx=5, pady=5)
button_3.grid(row=4, column=2, padx=5, pady=5)
button_plus.grid(row=4, column=3, padx=5, pady=5)

button_opp.grid(row=5, column=0, padx=5, pady=5)
button_0.grid(row=5, column=1, padx=5, pady=5)
button_equal.grid(row=5, column=2, padx=5, pady=5, columnspan=2)

root.mainloop()
