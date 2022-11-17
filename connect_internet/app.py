# Import required libraries
from tkinter import *
from PIL import ImageTk, Image  

# Create an instance of tkinter window
root = Tk()

# Define the geometry of the window
root.geometry("700x500")

frame = Frame(root, width=100, height=200)
frame.pack()
frame.place(anchor='center', relx=0.5, rely=0.5)

# Create an object of tkinter ImageTk
img = ImageTk.PhotoImage(Image.open("kgx.jpg"))


# Create a Label Widget to display the text or Image
label = Label(frame, image = img)
label.place(x=700, y=500, relwidth=0.5, relheight=0.5)
label.pack()

root.mainloop()