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
    def __init__(self, nombre, tipo, capacidad, dieta, temperatura, tipoDesierto, uv):
        super().__init__(nombre, tipo, capacidad, dieta, temperatura)
        self.tipoDesierto = tipoDesierto
        self.uv = uv

class selvatico(Habitat):
    def __init__(self, nombre, tipo, capacidad, dieta, temperatura, precipitación, humedad):
        super().__init__(nombre, tipo, capacidad, dieta, temperatura)
        self.precipitación = precipitación
        self.humedad = humedad

class polar(Habitat):
    def __init__(self, nombre, tipo, capacidad, dieta, temperatura, porHielo, grosorHielo):
        super().__init__(nombre, tipo, capacidad, dieta, temperatura)
        self.porHielo = porHielo
        self.grosorHielo = grosorHielo

class acuatico(Habitat):
    def __init__(self, nombre, tipo, capacidad, dieta, temperatura, pH, salinidad):
        super().__init__(nombre, tipo, capacidad, dieta, temperatura)
        self.pH = pH
        self.salinidad = salinidad

## Hacer sobrecarga de imprimir habitats para las clases hijas