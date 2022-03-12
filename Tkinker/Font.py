from tkinter import *
import tkinter.ttk as ttk
from numpy import pad, place
import sqlite3 as sql 

font = {
    "font": "sans-serif",
    "size": 15,
}

Root = Tk()
Root.title("Creador de fichas")
Root.config(borderwidth=5, background="purple")
Root.resizable(False, False)

miFrame = Frame(Root, bg="light grey", border=5, relief="groove")
miFrame.pack(fill="both")
miFrame.grid_propagate(True)

Titulo = Label(miFrame, text="Datos", font=(20), background="light grey")
Titulo.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

i = 1
for etiqueta in ["Nombre: ", "Apellido: ", "Contraseña: "]:
    Label(miFrame, font=font, text=etiqueta, background="light grey", justify="right", padx=5, pady=5).grid(row=i, column=0, sticky="e")
    i += 1

Entry(miFrame, textvariable="Nombre completo", background="white", justify="left").grid(row=1, column=1, columnspan=2, sticky="w")
Entry(miFrame, textvariable="Apellido", background="white", justify="left").grid(row=2, column=1, columnspan=2, sticky="w")
Entry(miFrame, textvariable="Contraseña", background="white", justify="left").grid(row=3, column=1, columnspan=2, sticky="w")


Comentario = Text(miFrame, background="white", foreground="black")
Comentario.grid(row=4, column=1)
Label(miFrame, text="Comentario", background="light grey", justify="right", font=font, padx=5, pady=5).grid(row=4, column=0, sticky="wn")

Barra = ttk.Scrollbar(miFrame, orient="vertical", command=Comentario.yview)
Barra.grid(row=4, column=2, sticky="nsew")
Comentario['yscrollcommand'] = Barra.set

def Guardar():
    try:
        Bd = sql.connect(database=r"Tkinker\BaseDeDatos.db")
        Bd("create")
    except sql.DatabaseError:
        print("Error en la base de datos")
    Bd.commit()

Boton = Button(miFrame, background="grey", font=font, text="Guardar en BBDD", command=Guardar)


Root.mainloop()