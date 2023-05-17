import streamlit as st
class Habitat:
    def __init__(self,nombre, tipo, capacidad, dieta, temperatura):
        self.nombre = nombre
        self.tipo = tipo
        self.capacidad = capacidad
        if "cantidad" in st.session_state:
            self.numeroAnimales = st.session_state["cantidad"]
        else:
            self.numeroAnimales = 0
            st.session_state["cantidad"] = 0
        self.dieta = dieta
        self.temperatura = temperatura
        if "mapaAnimales" in st.session_state:
            self.mapaAnimales = st.session_state["mapaAnimales"]
        else:
            self.mapaAnimales = {}
            st.session_state["mapaAnimales"] = {}

    def agregarAnimal(self, Animal):
        id = Animal.id
        self.mapaAnimales[id] = Animal
        st.session_state["mapaAnimales"] = self.mapaAnimales
        self.numeroAnimales += 1
        st.session_state["cantidad"] = self.numeroAnimales
    
    def eliminarAnimal(self, id):
        self.mapaAnimales.pop(id)
        self.numeroAnimales -= 1
        st.session_state["cantidad"] = self.numeroAnimales

    def imprimirAnimales(self):
        cont = 1
        print("En %s de tipo %s se encuentran %i animales:\n" %(self.nombre, self.tipo, self.numeroAnimales))

        for key in self.mapaAnimales:
            tempAnimal = self.mapaAnimales[key]

            print("%i)" % cont)
            tempAnimal.mostrarAnimal
            cont += 1
    
    def mostrarHabitats(self):
        cont = 1
        print("%i)" % cont)
        
        print("Nombre: %s\nTipo de habitat: %s\nCapacidad: %i/%i animales\nDieta: %s\nTemperatura: %i" %(self.nombre, self.tipo, self.numeroAnimales, self.capacidad, self.dieta, self.temperatura))
        print("-------------------------------")

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