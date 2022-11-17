from tkinter import *
root=Tk()
e=Entry(root, width)
e.pack()

def myclick():
    mylabel=Label(root,text="LOOK!I clicked a button,")
    mylabel.pack()

# Create a button widget
mybutton = Button(root, text="Click Me!", command=myclick, fg="blue", bg="red")
mybutton.pack()

#create an event loop
root.mainloop()