import math
from tkinter import *
root = Tk()
root.iconbitmap("Calc.ico")
root.configure(bg = "light grey")
root.title("Calculator")
e = Entry(root,font = "Times 10 italic ",width = 50, borderwidth = 5)
e.grid(row = 0, column = 0 , columnspan=4, padx = 10,  pady = 10)

def button_click(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0,str(current)+str(number))

def button_clear():
    e.delete(0, END)

def button_add():
    first_number = e.get()
    global f_num
    global math
    math = "Add"
    f_num = int(first_number)
    e.delete(0,END)

def button_div():
    first_number = e.get()
    global f_num
    global math
    math = "Div"
    f_num = int(first_number)
    e.delete(0,END)

def button_mul():
    first_number = e.get()
    global f_num
    global math
    math = "Mul"
    f_num = int(first_number)
    e.delete(0,END)


def button_sub():
    first_number = e.get()
    global f_num
    global math
    math = "Sub"
    f_num = int(first_number)
    e.delete(0,END)


def button_equal():
    second_number = e.get()
    e.delete(0, END)
    if math == "Add":
        e.insert(0, f_num + int(second_number))
    elif math == "Sub":
        e.insert(0,f_num - int(second_number))
    elif math == "Div":
        e.insert(0,f_num / int(second_number))
    elif math == "Mul":
        e.insert(0, f_num * int(second_number))
    




button_1 = Button(root, text = "1",fg = "white",bg = "grey", font = "Times 20 italic bold", padx = 40, pady = 20, command = lambda : button_click(1))
button_2 = Button(root, text = "2",fg = "white",bg = "grey", font = "Times 20 italic bold",padx = 40, pady = 20, command = lambda : button_click(2))
button_3 = Button(root, text = "3",fg = "white",bg = "grey", font = "Times 20 italic bold",padx = 40, pady = 20, command = lambda : button_click(3))
button_4 = Button(root, text = "4",fg = "white",bg = "grey", font = "Times 20 italic bold",padx = 40, pady = 20, command = lambda : button_click(4))
button_5 = Button(root, text = "5",fg = "white",bg = "grey", font = "Times 20 italic bold",padx = 40, pady = 20, command = lambda : button_click(5))
button_6 = Button(root, text = "6",fg = "white",bg = "grey", font = "Times 20 italic bold", padx = 40, pady = 20, command = lambda : button_click(6))
button_7 = Button(root, text = "7",fg = "white",bg = "grey", font = "Times 20 italic bold", padx = 40, pady = 20, command = lambda : button_click(7))
button_8 = Button(root, text = "8",fg = "white",bg = "grey", font = "Times 20 italic bold",padx = 40, pady = 20, command = lambda : button_click(8))
button_9 = Button(root, text = "9",fg = "white",bg = "grey", font = "Times 20 italic bold",padx = 40, pady = 20, command = lambda : button_click(9))
button_0 = Button(root, text = "0",fg = "white",bg = "grey", font = "Times 20 italic bold",padx = 40, pady = 20, command = lambda : button_click(0))
button_add = Button(root, text = "+",fg = "Blue", bg = "sky blue",font = "Times 20 italic bold", padx = 40, pady = 20, command = button_add)
button_clear = Button(root,text = "C",fg = "white",bg = "light green",font = "Times 20 italic bold", padx = 40, pady = 20, command = button_clear)
button_mul = Button(root, text = "*",fg = "blue", bg = "sky blue",font = "Times 20 italic bold", padx=40,pady= 20, command=button_mul)
button_div = Button(root, text = "÷",fg = "blue", bg = "sky blue",font = "Times 20 italic bold", padx= 40, pady= 20, command = button_div)
button_sub = Button(root, text = '−',fg = "blue", bg = "sky blue",font = "Times 20 italic bold", padx = 40, pady = 20, command = button_sub )
button_equal = Button(root, text = "=",fg = "Green", bg = "light yellow",font = "Times 20 italic bold", padx = 165, pady = 20, command = button_equal)




button_1.grid(row = 3, column = 0)
button_2.grid(row = 3, column = 1)
button_3.grid(row = 3, column = 2)

button_4.grid(row = 2, column = 0)
button_5.grid(row = 2, column = 1)
button_6.grid(row = 2, column = 2)

button_7.grid(row = 1, column = 0)
button_8.grid(row = 1, column = 1)
button_9.grid(row = 1, column = 2)

button_0.grid(row = 4, column = 1)
button_clear.grid(row = 4, column = 0)
button_add.grid(row = 4, column = 2)
button_sub.grid(row= 5, column=0)
button_div.grid(row = 5, column=1)
button_mul.grid(row = 5, column=2)
button_equal.grid(row = 6, column = 0, columnspan= 3)

root.mainloop()

