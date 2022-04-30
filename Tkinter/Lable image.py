from tkinter import *
from PIL import Image,ImageTk
arsenic_root = Tk()
arsenic_root.geometry("1100x1100")
# photo=PhotoImage(file="1.png")

# For JPG Format
image=Image.open("3.jpg")
photo=ImageTk.PhotoImage(image)


shivam_lable=Label(image=photo)
shivam_lable.pack()


arsenic_root.mainloop()