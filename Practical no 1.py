from tkinter import * 

win = Tk() 
win.geometry("500x400") 
win.title("Ekta - F077") 
lbl = Label(win, text="Hello", font=("Times New Roman",19)) 
lbl.grid(column=10, row=10) 

def click(): 
    lbl.configure(text="Learning Python") 
btn = Button(win, text="Click here", bg="light blue", font=("Arial",15), command=click) 
btn.grid(column=15, row=15) 

win.mainloop() 
