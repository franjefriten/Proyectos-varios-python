from tkinter import *
from typing import Sized

dic = {
    "font": "times new roman", 
    "size": 20
}

Raiz = Tk()

Raiz.iconbitmap(r"C:\Users\kikof\Desktop\VsCode_Python\Tkinker\calculator-icon_34473.ico")
Raiz.config(background="grey", relief="groove")
Raiz.title("Calculadora")
Raiz.geometry("300x550")

myLabel = Label(Raiz, text="Calculadora", background="light grey", \
    relief="groove", foreground="black", font=dic, borderwidth=2)
myLabel.pack(side='top', ipadx=350, ipady=30)

e = Entry(master=Raiz, bg="black", fg="white", borderwidth=4, relief="groove", textvariable="Inserar operaciones", \
    width=200, justify='center', font=dic, )
e.pack(fill='y', side='top', ipady=10)
e.config(justify="right")

Res = Label(Raiz, text="Resultado: ", background="light grey", \
     relief="groove", foreground="black", font=dic, borderwidth=2)
Res.pack(fill='y', side='top')

def B_add(n):
    try:
        actual = e.get()
    except:
        e.insert("ERROR")
    e.insert(len(e.get()), n)
    actual = str(actual) + str(n)

def B_mas(string):
    try:
        global num1
        num1 = e.get()
    except:
        e.insert("ERROR")
    else:
        e.delete(0, last=len(e.get()))
        global cad
        cad = string

def B_igual():
    try:
        global num2
        num2 = e.get()
    except:
        e.insert("ERROR")
    else:
        if cad == '+': Res.config(text="Resultado: " + str(int(num1)+int(num2)))
        if cad == '-': Res.config(text="Resultado: " + str(int(num1)-int(num2)))
        if cad == '*': Res.config(text="Resultado: " + str(int(num1)*int(num2)))
        try:
            if cad == '/': Res.config(text="Resultado: " + str(int(num1)/int(num2)))
        except ZeroDivisionError:
            Res.config(text="Resultado: ERROR")   

        e.delete(0, last=len(e.get()))

def B_clear():
    num1, num2 = None, None
    e.delete(0, last=len(e.get())) 
    Res.config(text="Resultado: ")   

        

Boton_1 = Button(master=Raiz, text="1", relief="groove", borderwidth=2, command= lambda: B_add(1))
Boton_1.place(height=50, width=50, x=40, y=250)
Boton_2 = Button(master=Raiz, text="2", relief="groove", borderwidth=2, command= lambda: B_add(2))
Boton_2.place(height=50, width=50, x=125, y=250)
Boton_3 = Button(master=Raiz, text="3", relief="groove", borderwidth=2, command= lambda: B_add(3))
Boton_3.place(height=50, width=50, x=210, y=250)
Boton_4 = Button(master=Raiz, text="4", relief="groove", borderwidth=2, command= lambda: B_add(4))
Boton_4.place(height=50, width=50, x=40, y=320)
Boton_5 = Button(master=Raiz, text="5", relief="groove", borderwidth=2, command= lambda: B_add(5))
Boton_5.place(height=50, width=50, x=125, y=320)
Boton_6 = Button(master=Raiz, text="6", relief="groove", borderwidth=2, command= lambda: B_add(6))
Boton_6.place(height=50, width=50, x=210, y=320)
Boton_7 = Button(master=Raiz, text="7", relief="groove", borderwidth=2, command= lambda: B_add(7))
Boton_7.place(height=50, width=50, x=40, y=390)
Boton_8 = Button(master=Raiz, text="8", relief="groove", borderwidth=2, command= lambda: B_add(8))
Boton_8.place(height=50, width=50, x=125, y=390)
Boton_9 = Button(master=Raiz, text="9", relief="groove", borderwidth=2, command= lambda: B_add(9))
Boton_9.place(height=50, width=50, x=210, y=390)
Boton_0 = Button(master=Raiz, text="0", relief="groove", borderwidth=2, command= lambda: B_add(0))
Boton_0.place(height=50, width=50, x=40, y=460)

Boton_mas = Button(master=Raiz, text="+", font=dic, relief="groove", borderwidth=2, command= lambda: B_mas('+'))
Boton_mas.place(height=50, width=40, x=10, y=170)
Boton_menos = Button(master=Raiz, text="-", font=dic, relief="groove", borderwidth=2, command= lambda: B_mas('-'))
Boton_menos.place(height=50, width=40, x=70, y=170)
Boton_por = Button(master=Raiz, text="*", font=dic, relief="groove", borderwidth=2, command= lambda: B_mas('*'))
Boton_por.place(height=50, width=40, x=130, y=170)
Boton_entre = Button(master=Raiz, text="/", font=dic, relief="groove", borderwidth=2, command= lambda: B_mas('/'))
Boton_entre.place(height=50, width=40, x=190, y=170)
Boton_igual = Button(master=Raiz, text="=", font=dic, relief="groove", borderwidth=2, command= lambda: B_igual())
Boton_igual.place(height=50, width=40, x=250, y=170)

Boton_clear = Button(master=Raiz, text="C", font=dic, relief="groove", borderwidth=2, command= lambda: B_clear())
Boton_clear.place(height=50, width=135, x=125, y=460)

Raiz.mainloop()
