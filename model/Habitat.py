import streamlit as st
class Habitat:
    def __init__(self,nombre, tipo, capacidad, dieta, temperatura):
        self.nombre = nombre
        self.tipo = tipo
        self.capacidad = capacidad
        self.numeroAnimales = 0
        self.dieta = dieta
        self.temperatura = temperatura
        self.mapaAnimales = {}


    def agregarAnimal(self, Animal):
        id = Animal.id
        self.mapaAnimales[id] = Animal
        self.numeroAnimales += 1
    
    def eliminarAnimal(self, id):
        self.mapaAnimales.pop(id)
        self.numeroAnimales -= 1
        st.session_state["cantidad"] = self.numeroAnimales

class desertico(Habitat):
    def __init__(self, nombre, tipo, capacidad, dieta, temperatura):
        super().__init__(nombre, tipo, capacidad, dieta, temperatura)
        self.tormentaArena = False
        self.sequia = True

class selvatico(Habitat):
    def __init__(self, nombre, tipo, capacidad, dieta, temperatura):
        super().__init__(nombre, tipo, capacidad, dieta, temperatura)
        self.vegetacion = False
        self.llueve = True

class polar(Habitat):
    def __init__(self, nombre, tipo, capacidad, dieta, temperatura):
        super().__init__(nombre, tipo, capacidad, dieta, temperatura)
        self.derretimiento = False
        self.nieva = True

class acuatico(Habitat):
    def __init__(self, nombre, tipo, capacidad, dieta, temperatura):
        super().__init__(nombre, tipo, capacidad, dieta, temperatura)
        self.corrientesMarinas = False
        self.limpieza = True

## Hacer sobrecarga de imprimir habitats para las clases hijas