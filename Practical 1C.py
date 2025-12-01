from tkinter import * 
 
win = Tk() 
win.title("Ekta - F077" ) 
win.geometry("300x300") 
 
lbl = Label(win,text="Enter your age:") 
lbl.grid() 
 
def age(): 
     age = int(ent.get()) 
 
     if age < 13: 
        category = "Minor" 
     elif age < 20: 
        category = "Teenager" 
     elif age < 60: 
        category = "Adult" 
     else: 
        category ="Senior Citizen"
        
     reslbl.configure(text=f"Category :{category}")
     
ent = Entry(win,width=10) 
ent.focus() 
ent.grid() 

btn = Button(win,text="Check age",command=age) 
btn.grid()
 
reslbl = Label(win,text="") 
reslbl.grid() 
win.mainloop()
