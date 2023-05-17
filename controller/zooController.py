import streamlit as st
import time

class zooController:
    def __init__(self, modelo, vista):
        self.modelo = modelo
        self.vista = vista
    
    def ejecutarOpcion(self, opcion):
        if opcion == 1:
            try:
                nuevoAnimal =self.vista.menu_crear_animales(self.modelo.idAnimal, self.modelo)
                if nuevoAnimal:
                    self.modelo.agregarAnimal(nuevoAnimal)
            except ValueError:
                self.vista.mostrar_mensaje_error("Se presento un error al crear el animal")
        if opcion == 2: #CrearHabitat
            try:
                nuevoHabitat = self.vista.menuCrearHabitat()
                if nuevoHabitat:
                    self.modelo.agregarHabitat(nuevoHabitat)
            except ValueError:
                self.vista.mostrar_mensaje_error("Se presento un error al crear el habitat")
        if opcion == 3: #ListarHabitats y animales
            self.vista.listarAnimalesHabitats(self.modelo.animales, self.modelo.habitats)
        if opcion == 4: #AccionAnimales
            pass
        if opcion == 5: #agregarAlimento
            try:
                tuplaComida = self.vista.agregarComida()
                if tuplaComida:
                    self.modelo.agregarAlimento(tuplaComida[0], tuplaComida[1])
                    self.vista.imprimirDieta(tuplaComida[0])
            except ValueError:
                self.vista.mostrar_mensaje_error("Se presento un error al crear la comida")
        if opcion == 6: #eliminarAlimento
            try:
                tuplaComida = self.vista.eliminarComida()
                if tuplaComida:
                    self.modelo.eliminarAlimento(tuplaComida[0], tuplaComida[1])
                    self.vista.imprimirDieta(tuplaComida[0])
            except ValueError:
                self.vista.mostrar_mensaje_error("Se presento un error al eliminar la comida")
        if opcion == 7:
            self.vista.agregarAnimalHabitat(self.modelo.animales, self.modelo.habitats)
    
    def aplicarFormatoA(self, animales):
        datos = []
        for key in animales:
            datos.append([animales[key].id, animales[key].nombre, animales[key].especie, animales[key].tipoHabitat, animales[key].dieta, animales[key].estado, animales[key].edad, animales[key].temperatura, animales[key].horasDormir])
        return datos

    def aplicarFormatoH(self, habitats):
        datos = []
        for habitat in habitats:
            datos.append([habitat.nombre, habitat.tipo, habitat.numeroAnimales, habitat.capacidad, habitat.dieta, habitat.temperatura[0], habitat.temperatura[1]])
        return datos
    
