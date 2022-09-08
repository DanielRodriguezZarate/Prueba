from cgitb import text
from tkinter import *
raiz =Tk()
raiz.title("Ventana de prueba")
raiz.resizable(False, False)
raiz.iconbitmap("python2.ico")
raiz.geometry("650x350")

num = IntVar()
num2 = IntVar()
n2 = IntVar()
diccionario = {}

def miFuncion():
    diccionario[caja.get()] = caja2.get()
    print(diccionario)


label = Label(raiz, text="Ingresa la clave")
label.pack()

caja = Entry(raiz, textvariable = num)
caja.pack()

label2 = Label(raiz, text = "Ingresa el valor")
label2.pack()

caja2 = Entry(raiz, textvariable = num2) 
caja2.pack()

boton2 = Button (raiz, text = "Enviar", command= miFuncion)
boton2.pack()

raiz .mainloop()