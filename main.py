from tkinter import *
import re

BACKGROUND_COLOR_WINDOW = "#B2E6B8"
BACKGROUND_COLOR = "#F2DD4F"

window = Tk()
window.title("Calculator")
window.config(bg=BACKGROUND_COLOR_WINDOW)
# window.minsize(width=1290, height=720)
window.title("CALCULATOR")
window.iconbitmap("calculator image/window_icon.ico")


def user_entry(number):
    entry.insert(END, number)
    entry.update()


def operations():
    input = entry.get()
    equal = eval(input)
    entry.delete(0, END)
    entry.insert(END, equal)
    entry.update()


def delete():
    entry.delete(0, END)
    entry.update()


def single_delete():
    entry.delete(entry.index("end")-1)


entry = Entry(width=29, font=("Bahnschrift Light Condensed", 20),border=5)
entry.grid(row=0, column=0, columnspan=6)

ac_img = PhotoImage(file="calculator image/ac.png")
ac = Button(image=ac_img, highlightthickness=0, command=delete, background=BACKGROUND_COLOR)
ac.grid(row=1, column=0)
one_delete_img = PhotoImage(file="calculator image/one_delete.png")
one_delete = Button(image=one_delete_img, highlightthickness=0, command=single_delete, background=BACKGROUND_COLOR)
one_delete.grid(row=1, column=1)
percentage_img = PhotoImage(file="calculator image/percent.png")
percent = Button(image=percentage_img, highlightthickness=0, command=lambda: user_entry("%"),
                 background=BACKGROUND_COLOR)
percent.grid(row=1, column=2)
divide_img = PhotoImage(file="calculator image/divide.png")
divide = Button(image=divide_img, highlightthickness=0, command=lambda: user_entry("/"), background=BACKGROUND_COLOR)
divide.grid(row=1, column=3)

seven_button = Button()
seven_img = PhotoImage(file="calculator image/seven.png")
seven_button.grid(row=2, column=0)
seven_button.config(image=seven_img, highlightthickness=0, command=lambda: user_entry("7"), background=BACKGROUND_COLOR)
eight_button = Button()
eight_img = PhotoImage(file="calculator image/eight.png")
eight_button.grid(row=2, column=1)
eight_button.config(image=eight_img, highlightthickness=0, command=lambda: user_entry("8"), background=BACKGROUND_COLOR)
nine_button = Button()
nine_img = PhotoImage(file="calculator image/nine.png")
nine_button.grid(row=2, column=2)
nine_button.config(image=nine_img, highlightthickness=0, command=lambda: user_entry("9"), background=BACKGROUND_COLOR)
multiply_img = PhotoImage(file="calculator image/multiply.png")
multiply = Button(image=multiply_img, highlightthickness=0, command=lambda: user_entry("*"),
                  background=BACKGROUND_COLOR)
multiply.grid(row=2, column=3)

four_img = PhotoImage(file="calculator image/four.png")
four = Button(image=four_img, highlightthickness=0, command=lambda: user_entry("4"), background=BACKGROUND_COLOR)
four.grid(row=3, column=0)
five_img = PhotoImage(file="calculator image/five.png")
five = Button(image=five_img, highlightthickness=0, command=lambda: user_entry("5"), background=BACKGROUND_COLOR)
five.grid(row=3, column=1)
six_img = PhotoImage(file="calculator image/six.png")
six = Button(image=six_img, highlightthickness=0, command=lambda: user_entry("6"), background=BACKGROUND_COLOR)
six.grid(row=3, column=2)
minus = Button()
minus_img = PhotoImage(file="calculator image/minus.png")
minus.grid(row=3, column=3)
minus.config(image=minus_img, highlightthickness=0, command=lambda: user_entry("-"), background=BACKGROUND_COLOR)

one = Button()
one_img = PhotoImage(file="calculator image/one.png")
one.grid(row=4, column=0)
one.config(image=one_img, highlightthickness=0, bg=BACKGROUND_COLOR, command=lambda: user_entry("1"),
           background=BACKGROUND_COLOR)
two = Button()
two_img = PhotoImage(file="calculator image/two.png")
two.grid(row=4, column=1)
two.config(image=two_img, highlightthickness=0, bg=BACKGROUND_COLOR, command=lambda: user_entry("2"),
           background=BACKGROUND_COLOR)
three = Button()
three_image = PhotoImage(file="calculator image/three.png")
three.grid(row=4, column=2)
three.config(image=three_image, highlightthickness=0, bg=BACKGROUND_COLOR, command=lambda: user_entry("3"),
             background=BACKGROUND_COLOR)
plus = Button()
plus_img = PhotoImage(file="calculator image/plus.png")
plus.grid(column=3, row=4)
plus.config(image=plus_img, highlightthickness=0, command=lambda: user_entry("+"), background=BACKGROUND_COLOR)

zero = Button()
zero_img = PhotoImage(file="calculator image/zero.png")
zero.grid(row=5, column=1)
zero.config(image=zero_img, highlightthickness=0, command=lambda: user_entry("0"), background=BACKGROUND_COLOR)
dot = Button()
dot_img = PhotoImage(file="calculator image/dot.png")
dot.grid(row=5, column=2)
dot.config(image=dot_img, highlightthickness=0, command=lambda: user_entry("."), background=BACKGROUND_COLOR)
equal = Button()
equal_image = PhotoImage(file="calculator image/equals.png")
equal.grid(row=5, column=3)
equal.config(image=equal_image, highlightthickness=0, command=operations, background=BACKGROUND_COLOR)

window.mainloop()
