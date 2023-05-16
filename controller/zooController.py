import streamlit as st
import time

class zooController:
    def __init__(self, modelo, vista):
        self.modelo = modelo
        self.vista = vista
    
    def ejecutarOpcion(self, opcion):
        if opcion == 1: #CrearAnimal
            pass
        if opcion == 2: #CrearHabitat
            self.vista.menuCrearHabitat(self.modelo.Zoo)
        if opcion == 3: #ListarHabitats y animales
            pass
        if opcion == 4: #AccionAnimales
            pass
        if opcion == 5: #editarDietas
            pass
