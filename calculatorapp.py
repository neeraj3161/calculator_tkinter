from tkinter import *

root = Tk()

ent = Entry(root, width=45)
ent.grid(row=0, column=0, columnspan=3, padx=10, pady=10)
root.title("Simple Calculator :)")


def clicked(number):
    # print(number,end=" ")
    current = ent.get()
    ent.delete(0, END)
    ent.insert(0, str(current) + str(number))


def button_clear():
    ent.delete(0, END)
    # print("Clear clicked")


def addition():
    first_number = ent.get()
    global f_num
    global math
    math = "addition"
    f_num = int(first_number)
    ent.delete(0, END)


def result():
    second_number = ent.get()
    global s_num
    s_num = int(second_number)
    ent.delete(0, END)
    if math == "addition":
        ent.insert(0, f_num + s_num)
    elif math == "substract":
        ent.insert(0, f_num - s_num)
    elif math == "divide":
        ent.insert(0, f_num / s_num)
    elif math == "multiply":
        ent.insert(0, f_num * s_num)


def multiply():
    first_number = ent.get()
    global f_num
    global math
    math = "multiply"
    f_num = int(first_number)
    ent.delete(0, END)


def substract():
    first_number = ent.get()
    global f_num
    global math
    math = "substract"
    f_num = int(first_number)
    ent.delete(0, END)


def divide():
    first_number = ent.get()
    global f_num
    global math
    math = "divide"
    f_num = int(first_number)
    ent.delete(0, END)

button_1 = Button(root, text="1", padx=40, pady=20, command=lambda: clicked(1)).grid(row=3, column=2)
button_2 = Button(root, text="2", padx=40, pady=20, command=lambda: clicked(2)).grid(row=3, column=1)
button_3 = Button(root, text="3", padx=40, pady=20, command=lambda: clicked(3)).grid(row=3, column=0)

button_4 = Button(root, text="4", padx=40, pady=20, command=lambda: clicked(4)).grid(row=2, column=1)
button_5 = Button(root, text="6", padx=40, pady=20, command=lambda: clicked(6)).grid(row=2, column=0)

button_6 = Button(root, text="5", padx=40, pady=20, command=lambda: clicked(5)).grid(row=2, column=2)

button_7 = Button(root, text="7", padx=40, pady=20, command=lambda: clicked(7)).grid(row=1, column=2)
button_8 = Button(root, text="8", padx=40, pady=20, command=lambda: clicked(8)).grid(row=1, column=1)
button_9 = Button(root, text="9", padx=40, pady=20, command=lambda: clicked(9)).grid(row=1, column=0)

button_0 = Button(root, text="0", padx=40, pady=20, command=lambda: clicked(0)).grid(row=4, column=0)
button_add = Button(root, text="+", padx=39, pady=20, command=addition).grid(row=5, column=0)
button_clear = Button(root, text="Clear", padx=80, pady=20, command=button_clear).grid(row=4, column=1, columnspan=2)
button_equals = Button(root, text="=", padx=89, pady=20, command=result).grid(row=5, column=1, columnspan=2)
button_multiply = Button(root, text="*", padx=40, pady=20, command=multiply).grid(row=6, column=0)
button_substract = Button(root, text="-", padx=40, pady=20, command=substract).grid(row=6, column=1)
button_divide = Button(root, text="/", padx=40, pady=20, command=divide).grid(row=6, column=2)

# button_point=Button(root,text=".",padx=40,pady=20).grid(row=5,column=0)


root.mainloop()
