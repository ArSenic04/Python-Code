from tkinter import *

arsenic_root = Tk()

# width x height
arsenic_root.geometry("644x434")

# when we minimize this will be width and height
arsenic_root.minsize(300, 100)

# when we maximize this will be width and height
arsenic_root.maxsize(1200,900)

arsenic=Label(text="This is Made by ArSenic")
arsenic.pack()

arsenic_root.mainloop()
