from tkinter import *

root = Tk()
root.title("Basic Calculator")
font = ("arial", 20, "bold")
root.configure(bg="gray")
e=Entry(root,width=30 , borderwidth = "3")
e.grid(row=0 , column=0 , columnspan=5 , padx=30, pady=30)
def button_click(number):
    current= e.get()
    e.delete(0,END)
    e.insert(0 , str(current+str(number)))

def button_del():
    e.delete(0,END)

def button_add():
    first_number = e.get()
    global f_num
    global math
    math = "Addition"
    f_num = float(first_number)
    e.delete(0 ,END)

def button_equal():
    second_number = e.get()
    e.delete(0, END)
    if math == "Addition":
        e.insert(0, f_num + float(second_number))
    if math == "Subtraction":
        e.insert(0, f_num - float(second_number))
    if math == "Multiplication":
        e.insert(0, f_num * float(second_number))
    if math == "Division":
        e.insert(0, f_num / float(second_number))
    if math == "Exponent":
        e.insert(0, f_num ** float(second_number))
def button_div():
    first_number = e.get()
    global f_num
    f_num = int(first_number)
    e.delete(0, END)
def button_sub():
    first_number = e.get()
    global f_num
    f_num = int(first_number)
    e.delete(0, END)


def button_mul():
    first_number = e.get()
    global f_num
    global math
    math = "Multiplication"
    f_num = float(first_number)
    e.delete(0, END)


def button_sub():
    first_number = e.get()
    global f_num
    global math
    math = "Subtraction"
    f_num = float(first_number)
    e.delete(0, END)


def button_div():
    first_number = e.get()
    global f_num
    global math
    math = "Division"
    f_num = float(first_number)
    e.delete(0, END)





button_1 = Button(root, text="1", padx=40, pady=40, command = lambda : button_click(1) , bg = "yellow")
button_2 = Button(root, text="2", padx=40, pady=40, command = lambda : button_click(2), bg = "yellow")
button_3 = Button(root, text="3", padx=40, pady=40, command = lambda : button_click(3) , bg = "yellow")
button_4 = Button(root, text="4", padx=40, pady=40, command = lambda : button_click(4),bg = "yellow")
button_5 = Button(root, text="5",padx=40 , pady=40, command = lambda : button_click(5) , bg = "yellow")
button_6 = Button(root, text="6", padx=40, pady=40, command = lambda : button_click(6), bg = "yellow")
button_7 = Button(root, text="7", padx=40, pady=40, command = lambda : button_click(7), bg = "yellow")
button_8 = Button(root, text="8", padx=40, pady=40, command = lambda : button_click(8), bg = "yellow")
button_9 = Button(root, text="9", padx=40, pady=40, command = lambda : button_click(9) , bg = "yellow")
button_0 = Button(root, text="0", padx=40, pady=40, command = lambda : button_click(0) , bg="yellow")
button_add = Button(root, text="+", padx= 39, pady=40, command = button_add)
button_equal = Button(root, text="=", padx=40 , pady=40, command = button_equal)
button_del = Button(root, text="del", padx=40 , pady=40, command = button_del , bg= "red")
button_div = Button(root, text="/" , padx=40 , pady=40 , command= button_div)
button_sub = Button(root, text="-" , padx=40 , pady=40 , command= button_sub)
button_mul = Button(root, text="*" , padx=40 , pady=40 , command= button_mul)

button_1.grid(row=3,column=0)
button_2.grid(row=3,column=1)
button_3.grid(row=3,column=2)

button_4.grid(row=2,column=0)
button_5.grid(row=2,column=1)
button_6.grid(row=2,column=2)

button_7.grid(row=1,column=0)
button_8.grid(row=1,column=1)
button_9.grid(row=1,column=2)

button_0.grid(row=4,column=0)
button_del.grid(row=4,column=1 )
button_add.grid(row=2,column=4)
button_equal.grid(row=4,column=4)
button_div.grid(row=1 , column=4)
button_sub.grid(row=3 , column=4)
button_mul.grid(row=4 , column=2)

root.mainloop()
