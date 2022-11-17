from tkinter import *
root = Tk()

# Create a Label Widget to display the text or Image
myLabel = Label(root,text="Hello World!")
myLabel1=Label(root, text="My name is Devansh!", fg="blue", bg="yellow")
myLabel.pack()
myLabel1.grid(row=1,column=0)



# Create an event loop
root.mainloop()