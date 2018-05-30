from tkinter import *

def bntClick(numbers):
    global operator
    operator=operator + str(numbers)
    text_input.set(operator)

def btnClearDisplay():
    # global operator
    # operator=operator + str(numbers)
    text_input.set("")

def btnEqualsInput(numbers):
    global operator
    sumOp=str(eval(operator))
    text_input.set(sumOp)
    operator = ""


root = Tk()
root.title("Calculator")

operator = ""
text_input = StringVar()

txtDisplay = Entry(root, font=('arial', 20, "bold"), textvariable=text_input, bd=30, insertwidth=4, bg="powder blue", justify="right").grid(columnspan=4)

btn7 = Button(root, text="7", padx=16, bd=8, fg="black", font=('arial', 20, "bold"), command=lambda:bntClick(7)).grid(row=0, column=0)
btn8 = Button(root, text="8", padx=16, bd=8, fg="black", font=('arial', 20, "bold"), command=lambda:bntClick(8)).grid(row=0, column=1)
btn9 = Button(root, text="9", padx=16, bd=8, fg="black", font=('arial', 20, "bold"), command=lambda:bntClick(9)).grid(row=0, column=2)
btnPlus = Button(root, text="+", padx=16, bd=8, fg="black", font=('arial', 20, "bold"), command=lambda:bntClick("+")).grid(row=0, column=3)
btn4 = Button(root, text="4", padx=16, bd=8, fg="black", font=('arial', 20, "bold"), command=lambda:bntClick(4)).grid(row=1, column=0)
btn5 = Button(root, text="5", padx=16, bd=8, fg="black", font=('arial', 20, "bold"), command=lambda:bntClick(5)).grid(row=1, column=1)
btn6 = Button(root, text="6", padx=16, bd=8, fg="black", font=('arial', 20, "bold"), command=lambda:bntClick(6)).grid(row=1, column=2)
btnMinus = Button(root, text="-", padx=16, bd=8, fg="black", font=('arial', 20, "bold"), command=lambda:bntClick("-")).grid(row=1, column=3)
btn1 = Button(root, text="1", padx=16, bd=8, fg="black", font=('arial', 20, "bold"), command=lambda:bntClick(1)).grid(row=2, column=0)
btn2 = Button(root, text="2", padx=16, bd=8, fg="black", font=('arial', 20, "bold"), command=lambda:bntClick(2)).grid(row=2, column=1)
btn3 = Button(root, text="3", padx=16, bd=8, fg="black", font=('arial', 20, "bold"), command=lambda:bntClick(3)).grid(row=2, column=2)
btnMult = Button(root, text="*", padx=16, bd=8, fg="black", font=('arial', 20, "bold"), command=lambda:bntClick("*")).grid(row=2, column=3)
btn0 = Button(root, text="0", padx=16, bd=8, fg="black", font=('arial', 20, "bold"), command=lambda:bntClick(0)).grid(row=3, column=0)
btnClear = Button(root, text="C", padx=16, bd=8, fg="black", font=('arial', 20, "bold"), command=btnClearDisplay).grid(row=3, column=1)
btnEqual = Button(root, text="=", padx=16, bd=8, fg="black", font=('arial', 20, "bold"), command=btnEqualsInput).grid(row=3, column=2)
btnDiv = Button(root, text="/", padx=16, bd=8, fg="black", font=('arial', 20, "bold"), command=lambda:bntClick("/")).grid(row=3, column=3)






def printName():
    print("s")

def leftClickEvent(event):
    print("left")

def middleClickEvent(event):
    print("miggle")

def rightClickEvent(event):
    print("right")
#
# topFrame = Frame(root)
# topFrame.pack()
# secondFrame = Frame(root)
# secondFrame.pack()
# thirdFrame = Frame(root)
# thirdFrame.pack()
# bottomFrame = Frame(root)
# bottomFrame.pack(side=BOTTOM)
#
# # one = Label(root, text="", bg="red", fg="white")
# # one.pack(fill=X)
#

#
#
# button1.pack(side=LEFT)
# button2.pack(side=LEFT)
# button3.pack(side=LEFT)
# button4.pack(side=LEFT)
#
# button5.pack(side=LEFT)
# button6.pack(side=LEFT)
# button7.pack(side=LEFT)
# button8.pack(side=LEFT)

# button9.pack(side=LEFT)
# button10.pack(side=LEFT)
# button11.pack(side=LEFT)
# button12.pack(side=LEFT)
#
# button13.pack(side=LEFT)
# button14.pack(side=LEFT)
# button15.pack(side=LEFT)
# button16.pack(side=LEFT)
# button4.bind("<Button-3>", rightClickEvent)




root.mainloop()