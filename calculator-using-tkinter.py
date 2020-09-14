
from tkinter import *
import tkinter.messagebox
import parser

root = Tk()
root.title('Calculator')

def fact(num):
	if(num>1):
		return num*fact(num-1)
	else:
		return 1

# Writing on the display

i=0

def get_data(num):
	global i
	display.insert(i, num)
	i+=1

def calculate():
	entire_string = display.get()
	try:
		a = parser.expr(entire_string).compile()
		result = eval(a)
		clear_all()
		display.insert(0, result)
	
	except Exception:
		clear_all()
		display.insert(0, "ERROR")

def factorial(num):
	global i
	entire_string = display.get()
	#length = len(entire_string)
	variable = int(entire_string)
	result = fact(variable)
	result = str(result)
	length = len(result)
	clear_all()
	display.insert(0, result)
	i += length


def get_operation(operation):
	global i
	length = len(operation)
	display.insert(i, operation)
	i+= length

def clear_all():
	display.delete(0, END)
	i=0

def undo():
	entire_string = display.get()
	if len(entire_string):
		entire_string = entire_string[:-1]
		clear_all()
		display.insert(0, entire_string)
	else:
		display.insert(0, "ERROR")

#Adding the input field
display = Entry(root)
display.grid(row = 1, columnspan = 12, sticky = W+E)

#Adding the buttons to the calculator

Button(root, text="1", command= lambda : get_data(1)).grid(row=2, column=0, columnspan =2)
Button(root, text="2", command= lambda : get_data(2)).grid(row=2, column=2, columnspan =2)
Button(root, text="3", command= lambda : get_data(3)).grid(row=2, column=4, columnspan =2)
Button(root, text="4", command= lambda : get_data(4)).grid(row=3, column=0, columnspan =2)
Button(root, text="5", command= lambda : get_data(5)).grid(row=3, column=2, columnspan =2)
Button(root, text="6", command= lambda : get_data(6)).grid(row=3, column=4, columnspan =2)
Button(root, text="7", command= lambda : get_data(7)).grid(row=4, column=0, columnspan =2)
Button(root, text="8", command= lambda : get_data(8)).grid(row=4, column=2, columnspan =2)
Button(root, text="9", command= lambda : get_data(9)).grid(row=4, column=4, columnspan =2)

#Adding other buttons to the calculator

Button(root, text= "AC", command = clear_all).grid(row=5, column=0, columnspan =2)
Button(root, text= "0", command= lambda : get_data(0)).grid(row=5, column=2, columnspan =2)
Button(root, text= "=", command = calculate).grid(row=5, column=4, columnspan =2)

Button(root, text= "+", bg= "Orange", command= lambda : get_operation("+")).grid(row= 2, column= 6, columnspan =2)
Button(root, text= "-", bg= "Orange", command= lambda : get_operation("-")).grid(row= 3, column= 6, columnspan =2)
Button(root, text= "*", bg= "Orange", command= lambda : get_operation("*")).grid(row= 4, column= 6, columnspan =2)
Button(root, text= "/", bg= "Orange", command= lambda : get_operation("/")).grid(row= 5, column= 6, columnspan =2)

#Adding new operations

Button(root, text= "pi", bg= "Orange", command= lambda : get_operation("*3.14257")).grid(row= 2, column= 8, columnspan =2)
Button(root, text= "%", bg= "Orange", command= lambda : get_operation("%")).grid(row= 3, column= 8, columnspan =2)
Button(root, text= "(", bg= "Orange", command= lambda : get_operation("(")).grid(row= 4, column= 8, columnspan =2)
Button(root, text= "exp", bg= "Orange", command= lambda : get_operation("**")).grid(row= 5, column= 8, columnspan =2)

Button(root, text= "<-", bg= "Orange", command = undo).grid(row= 2, column= 10, columnspan =2)
Button(root, text= "x!", bg= "Orange", command = lambda : factorial(int(display.get()))).grid(row= 3, column= 10, columnspan =2)
Button(root, text= ")", bg= "Orange", command= lambda : get_operation(")")).grid(row= 4, column= 10, columnspan =2)
Button(root, text= "^2", bg= "Orange", command= lambda : get_operation("**2")).grid(row= 5, column= 10, columnspan =2)


root.mainloop()
