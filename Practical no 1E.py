from tkinter import *

win = Tk()
win.title("Ekta buneti - F077")
win.geometry("300x200")

lbl = Label(win, text="Hello", font=("Times New Roman", 15))
lbl.grid(pady=10)

txt = StringVar()

rad = Radiobutton(win, text='Click here', variable=txt, value="clicked")
rad.grid(sticky="w", padx=10)

win.mainloop()


