from tkinter import *

root = Tk()

def printName():
    print("s")

def leftClickEvent(event):
    print("left")

def middleClickEvent(event):
    print("miggle")

def rightClickEvent(event):
    print("right")

# one = Label(root, text="Sample1", bg="red", fg="white")
# one.pack()
# two = Label(root, text="Sample2", bg="green", fg="black")
# two.pack(fill=X)
# three = Label(root, text="Sample3", bg="blue", fg="white")
# three.pack(side=LEFT, fill=Y)
#
#
topFrame = Frame(root)
topFrame.pack()
bottomFrame = Frame(root)
bottomFrame.pack(side=BOTTOM)
#
button1 = Button(topFrame, text="PrintMyName", fg="red", command=printName)
button2 = Button(topFrame, text="PrintMyNameOnEventMouseClick", fg="blue")
button3 = Button(topFrame, text="Btn3", fg="green")
button4 = Button(bottomFrame, text="Btn4", fg="purple")

button1.pack(side=LEFT)
button2.bind("<Button-1>", leftClickEvent)
button2.pack(side=LEFT)

button3.bind("<Button-2>", middleClickEvent)
button3.pack(side=LEFT)

button4.bind("<Button-3>", rightClickEvent)
button4.pack(side=BOTTOM)

# label_1 = Label(root, text="Name")
# label_2 = Label(root, text="Pass")
# entry_1 = Entry(root)
# entry_2 = Entry(root)
#
# label_1.grid(row=0, sticky=W)
# label_2.grid(row=1, sticky=W)
# entry_1.grid(row=0, column=1)
# entry_2.grid(row=1, column=1)

# c = Checkbutton(root, text="Keep me logged in")
# c.grid(columnspan=2)



root.mainloop()