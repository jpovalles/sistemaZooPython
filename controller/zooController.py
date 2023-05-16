import streamlit as st
import time

class zooController:
    def __init__(self, modelo, vista):
        self.modelo = modelo
        self.vista = vista
    
    def ejecutarOpcion(self, opcion):
        if opcion == 1:
            try:
                nuevoAnimal =self.vista.menu_crear_animales(self.modelo.idAnimal)
                if nuevoAnimal:
                    self.modelo.agregarAnimal(nuevoAnimal)
            except ValueError:
                self.vista.mostrar_mensaje_error("Se presento un error al crear el animal")
        if opcion == 2: #CrearHabitat
            self.vista.menuCrearHabitat()
        if opcion == 3: #ListarHabitats y animales
            pass
        if opcion == 4: #AccionAnimales
            pass
        if opcion == 5: #editarDietas
            pass
        if opcion == 6:
            self.vista.agregarAnimalHabitat(self.modelo.animales, self.modelo.habitats)
