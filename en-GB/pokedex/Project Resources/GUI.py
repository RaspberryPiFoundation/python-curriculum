from tkinter import *

#create a new GUI window
window = Tk()
window.title("A Window")

#a label
lbl = Label(window,text="A Label")
lbl.pack()

#an 'entry' textbox
txt = Entry(window)
txt.pack()

#a button
btn = Button(window,text="A Button")
btn.pack()

window.mainloop()

    
