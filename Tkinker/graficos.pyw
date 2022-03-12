from tkinter import *
from typing import Tuple

Raiz = Tk()
Raiz.title("Ventana de pruebas")
Raiz.resizable(True, True)
try:
    Raiz.iconbitmap(r"Tkinker\calculator-icon_34473.ico")
except:
    Raiz.iconbitmap(r"C:\Users\kikof\Desktop\VsCode_Python\Tkinker\calculator-icon_34473.ico")

Raiz.geometry("850x450")
Raiz.config(border=10)

miFrame = Frame()
miFrame.pack(fill="both", expand="1")
miFrame.config(background="light grey")

Etiquieta_1 = Label(Raiz, text="Calculadora", padx=50, pady=50)

boton_1 = Button(master=Raiz, text="1", activebackground="grey",  bg="light grey", borderwidth=2, \
    padx=0, pady=50)



Raiz.mainloop()