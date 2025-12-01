from tkinter import * 
win = Tk() 
win.geometry("300x300") 
win.title("Ekta Buneti - F077") 

lbl = Label(win, text="Enter your Name:") 
lbl.grid() 
lbl1 = Label(win, text="Enter your mobile no. :") 
lbl1.grid() 
lbl2 = Label(win, text="Enter your city :") 
lbl2.grid() 

lbl3 = Label(win) 
lbl3.grid() 
lbl4 = Label(win) 
lbl4.grid() 
lbl5 = Label(win) 
lbl5.grid() 

txt = Entry(win, width=20) 
txt.grid() 
txt.focus() 
txt1 = Entry(win, width=25) 
txt1.grid() 
txt2 = Entry(win, width=20) 
txt2.grid() 
def click(): 
    res = "Welcome " + txt.get() 
    lbl3.configure(text=res) 
    res1 = "Your mobile no. is: " + txt1.get() 
    lbl4.configure(text=res1) 
    res2 = "Your City is " + txt2.get() 
    lbl5.configure(text=res2) 

btn = Button(win, text="Display", command = click, font=("Arial",14,"underline"), bd=2, 
relief="groove") 
btn.grid() 
win.mainloop() 
