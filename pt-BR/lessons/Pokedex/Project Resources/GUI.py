from tkinter import *

#criação de uma nova janela GUI
janela = Tk()
janela.title("Uma Janela")

#uma etiqueta
lbl = Label(janela,text="Uma etiqueta")
lbl.pack()

#um campo de entrada de texto 
texto = Entry(janela)
texto.pack()

#um botão
btn = Button(janela,text="Um Botão")
btn.pack()

janela.mainloop()

    
