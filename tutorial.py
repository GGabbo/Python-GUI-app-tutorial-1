import tkinter
from tkinter import *
app = Tk()
app.geometry("300x300")
def cliccato():
    ciao = Label(app, text="Mi hai trovato!")
    ciao.pack()
testo1 = Label(app, text="Ciao! Questa è la mia app!")
testo1.pack()
pulsante = Button(app, text="cliccami", command=cliccato)
pulsante.pack()
app.mainloop()
