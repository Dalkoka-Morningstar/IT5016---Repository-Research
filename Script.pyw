# IT5016---Repository-Research

"""
Calculator
Author: Jacob Ian John Kerr

"""

from audioop import add
from tkinter import *
from turtle import right, width
from unittest import result

def btnEnter(num):
    global operator
    operator = operator + str(num)
    userinput.set(operator)

def clear():
    global operator
    operator =""
    userinput.set("")
    txtEntry.insert(0,"0")

def backspace():
    numLen = len(txtEntry.get())
    txtEntry.delete(numLen - 1, 'end')
    if numLen ==1:
        txtEntry.insert(0, "0")

def equals():
    try:
        global operator
        result = str(eval(operator))
        userinput.set(result)
    except:
        userinput.set("Error")
        operator=""

def intocm():
    global operator
    operator = operator + "*2.54"
    result = str(eval(operator))
    userinput.set(result)

def cmtoin():
    global operator
    operator = operator + "/2.54"
    result = str(eval(operator))
    userinput.set(result)




root =Tk()
root.title("Calculator")
root.config(bg="lightblue")

operator = ""
userinput = StringVar()


# row 0 

#Entry box
# txtEntry = Entry(root, font=('arial',20,'bold'), fg="#fff",bg="#202020",bd=18,width=28,justify=RIGHT)

txtEntry = Entry(root, font=('arial',20,'bold'), fg="#000",bg="#fff",bd=4,width=25,justify=RIGHT,textvariable=userinput)
txtEntry.grid(row = 0, column = 0, columnspan= 5, pady =1)
txtEntry.insert(0,"0")

#row 1 
btn_addition = Button(root, text="+",width= 5, font = ("Helvetica",16, "bold"), relief="flat", bg="#DBDFF7", command=lambda:btnEnter("+"))
btn_addition.grid(row = 1, column=0, padx= 4, pady=4)


btn_substraction = Button(root, text="-",width= 5, font = ("Helvetica",16), relief="flat", bg="#DBDFF7", command=lambda:btnEnter("-"))
btn_substraction.grid(row = 1, column=1 , padx= 4)


btn_division = Button(root, text="/",width= 5, font = ("Helvetica",16), relief="flat", bg="#DBDFF7",command=lambda:btnEnter("/"))
btn_division.grid(row = 1, column=2, padx= 4)

btn_multiplication = Button(root, text="x",width= 5, font = ("Helvetica",16), relief="flat", bg="#DBDFF7", command=lambda:btnEnter("*"))
btn_multiplication.grid(row = 1, column=3, padx= 4)

btn_equal = Button(root, text="=",width= 5, height= 9, font = ("Helvetica",16), relief="flat", bg="#DBDFF7", command=equals)
btn_equal.grid(row = 1, column=4, rowspan= 5, padx= 4)


#row 2
btn_one = Button(root, text="1",width= 5, font = ("Helvetica",16), relief="flat", bg="#DBDFF7", command=lambda:btnEnter(1))
btn_one.grid(row = 2, column=0, padx= 4, pady=4)

btn_two = Button(root, text="2",width= 5, font = ("Helvetica",16), relief="flat", bg="#DBDFF7", command=lambda:btnEnter(2))
btn_two.grid(row = 2, column=1, padx= 4)

btn_three = Button(root, text="3",width= 5, font = ("Helvetica",16), relief="flat", bg="#DBDFF7", command=lambda:btnEnter(3))
btn_three.grid(row = 2, column=2, padx= 4)

btn_four = Button(root, text="4",width= 5, font = ("Helvetica",16), relief="flat", bg="#DBDFF7", command=lambda:btnEnter(4))
btn_four.grid(row = 2, column=3, padx= 4)

#row 3
btn_five = Button(root, text="5",width= 5, font = ("Helvetica",16), relief="flat", bg="#DBDFF7", command=lambda:btnEnter(5))
btn_five.grid(row = 3, column=0, padx= 4, pady=4)

btn_six = Button(root, text="6",width= 5, font = ("Helvetica",16), relief="flat", bg="#DBDFF7", command=lambda:btnEnter(6))
btn_six.grid(row = 3, column=1, padx= 4)

btn_seven = Button(root, text="7",width= 5, font = ("Helvetica",16), relief="flat", bg="#DBDFF7", command=lambda:btnEnter(7))
btn_seven.grid(row = 3, column=2, padx= 4)

btn_eight = Button(root, text="8",width= 5, font = ("Helvetica",16), relief="flat", bg="#DBDFF7", command=lambda:btnEnter(8))
btn_eight.grid(row = 3, column=3, padx= 4)


#row 4
btn_nine = Button(root, text="9",width= 5, font = ("Helvetica",16), relief="flat", bg="#DBDFF7", command=lambda:btnEnter(9))
btn_nine.grid(row = 4, column=0, padx= 4, pady=4)

btn_zero = Button(root, text="0",width= 5, font = ("Helvetica",16), relief="flat", bg="#DBDFF7", command=lambda:btnEnter(0))
btn_zero.grid(row = 4, column=1, padx= 4)

btn_dot = Button(root, text="•",width= 5, font = ("Helvetica",16), relief="flat", bg="#DBDFF7", command=lambda:btnEnter("."))
btn_dot.grid(row = 4, column=2, padx= 4)

btn_clear = Button(root, text="C", width= 5, font = ("Helvetica",16), relief="flat", bg="#DBDFF7", command=clear)
btn_clear.grid(row = 4, column=3, padx= 4)

#row 6

btn_in2cm = Button(root, text="IN to CM",width= 12, font = ("Helvetica",16), relief="flat", bg="#DBDFF7", command=intocm)
btn_in2cm.grid(row = 5, column=0, columnspan= 2, padx= 4, pady=4)

btn_cm2in = Button(root, text="CM to IN",width= 12, font = ("Helvetica",16), relief="flat", bg="#DBDFF7", command=cmtoin)
btn_cm2in.grid(row = 5, column=2, columnspan= 2, padx= 4)

root.mainloop()
