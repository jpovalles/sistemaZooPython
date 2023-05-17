import streamlit as st


class Zoo:
    def __init__(self, idAnimal):

        self.idAnimal = idAnimal
        self.comida = {}

        if "habitats" in st.session_state:
            self.habitats = st.session_state["habitats"]
        else:
            self.habitats = []
            st.session_state["habitats"] = []
    
        if "animales" in st.session_state:
            self.animales = st.session_state["animales"]
        else:
            self.animales = {}
            st.session_state["animales"] = {}

        self.tipos = ["Desertico", "Selvatico", "Polar", "Acuatico"]
        self.dietas = ["Carnivoro", "Omnivoro", "Herbivoro"]
        self.comida["Carnivoro"] = ["Cerdo", "Pavo", "Pollo"]
        self.comida["Herbivoro"] = ["Semillas", "Frutas", "Hojas"]
        self.comida["Omnivoro"] = ["Pescado", "Huevos", "Frutas"]
    
    def agregarHabitat(self, habitat):
        self.habitats.append(habitat)
        st.session_state["habitats"] = self.habitats
        return True

    def agregarAnimal(self, animal):
        self.animales[animal.id]=animal
        st.session_state["animales"] =self.animales
        self.idAnimal = self.idAnimal + 1
        return True
    
    def buscarComida(self, tipoDieta, alimento):
        if alimento in self.comida[tipoDieta]:
            return self.comida[tipoDieta].index(alimento)
        else:
            return -1
    
    def agregarAlimento(self, tipoDieta, alimento):
        self.comida[tipoDieta].append(alimento)
    
    def eliminarAlimento(self, tipoDieta, index):
        self.comida[tipoDieta].pop(index)

    def mostrarDieta(self, tipoDieta):
        print("Dieta %s:" %tipoDieta)
        for alimento in self.comida[tipoDieta]:
            print("\t%s" % alimento)
        print("-------------------------------")