import pickle
import os

class Persona():

    def __init__(self, nombre, apellido, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
    
    def __str__(self):
        return "Nombre: {} \nApellido: {} \nEdad: {}".format(self.nombre, self.apellido, self.edad) 

class miLista():

    def __init__(self, direccion) -> None:
        self.direccion = direccion
        self.lista = []

        try:
            file = open(self.direccion, "rb")
            file.seek(0)
            if os.path.getsize(self.direccion) != 0:
              self.lista = pickle.load(file)
        except FileNotFoundError:
            print("Fichero no encontrado")
            file = open(self.direccion, "wb+")
            file.seek(0)
        finally:
            file.close()


    def agregar_Pesona(self, persona):
        self.lista.append(persona)
    
    def guardar_Personas(self):
        file = open(self.direccion, "wb")
        try:
            pickle.dump(file=file, obj=self.lista)
        except: print("Error de volcado")
        finally: file.close()
    
    def mostrar_Personas(self):
        cad = ''
        for elemento in self.lista:
            cad += str(elemento.__str__())
        return "Lista: " + cad

Lista = miLista(r"Serialización\Data")
Lista.agregar_Pesona(Persona(nombre="Pedro", apellido="Manero", edad=30))
Lista.agregar_Pesona(Persona(nombre="Milano", apellido="Manero", edad=24))
Lista.agregar_Pesona(Persona(nombre="María", apellido="De Mir", edad=18))
Lista.guardar_Personas()
Lista.mostrar_Personas()
