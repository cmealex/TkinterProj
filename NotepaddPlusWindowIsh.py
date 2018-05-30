from tkinter import *
import tkinter.messagebox

def doNothing():
    print("sample")

root = Tk()

tkinter.messagebox.showinfo("MsgBoxTitle", "Some text")

answer = tkinter.messagebox.askquestion("question 1", "Are u kidding")
if answer == "yes":
    print(" 8===D~")

photo = PhotoImage(file="img.png")
label = Label(root, image=photo)
label.pack()

### MAIN MEMU
menu = Menu(root)
root.config(menu=menu)

### DropDown MENUS
fileMenu = Menu(menu)
menu.add_cascade(label="File", menu=fileMenu)
fileMenu.add_cascade(label="New Project...", command=doNothing)
fileMenu.add_cascade(label="New...", command=doNothing)
fileMenu.add_separator()
fileMenu.add_cascade(label="Exit...", command=quit)

editMenu = Menu(menu)
menu.add_cascade(label="Edit", menu=editMenu)
editMenu.add_cascade(label="New Project...", command=doNothing)
editMenu.add_cascade(label="New...", command=doNothing)
editMenu.add_separator()
editMenu.add_cascade(label="Exit...", command=quit)

### TOOLBAR
toolbar = Frame(root, bg="blue")

insertButt = Button(toolbar, text="InsertImg", command=doNothing)
insertButt.pack(side=LEFT, padx=2, pady=2) #padding=extra spaces
printButt = Button(toolbar, text="Print", command=doNothing)
printButt.pack(side=LEFT, padx=2, pady=2) #padding=extra spaces

toolbar.pack(side=TOP, fill=X)
#################################

## STATUS BAR

status = Label(root, text="Prep", bd=1, relief=SUNKEN, anchor=W) # bd = border
status.pack(side=BOTTOM, fill=X)






root.mainloop()