import streamlit as st


class Zoo:
    def __init__(self, idAnimal):

        if "idAnimal" in st.session_state:
            self.idAnimal = st.session_state["idAnimal"]
        else:
            self.idAnimal = 0
            st.session_state["idAnimal"] = 0

        if "comida" in st.session_state:
            self.comida = st.session_state["comida"]
        else:
            self.comida = {}
            self.comida["Carnivoro"] = ["Cerdo", "Pavo", "Pollo"]
            self.comida["Herbivoro"] = ["Semillas", "Frutas", "Hojas"]
            self.comida["Omnivoro"] = ["Pescado", "Huevos", "Frutas"]

        if "habitats" in st.session_state:
            self.habitats = st.session_state["habitats"]
        else:
            self.habitats = []
            st.session_state["habitats"] = []
    
        if "animales" in st.session_state:
            self.animales = st.session_state["animales"]
        else:
            self.animales = []
            st.session_state["animales"] = []

        self.tipos = ["Desertico", "Selvatico", "Polar", "Acuatico"]
        self.dietas = ["Carnivoro", "Omnivoro", "Herbivoro"]
    
    def agregarHabitat(self, habitat):
        self.habitats.append(habitat)
        st.session_state["habitats"] = self.habitats
        return True

    def eliminarAnimal(self, id):
        del self.animales[id]
        st.session_state["animales"] = self.animales
        return True


    def agregarAnimal(self, animal):
        self.animales.append(animal)
        self.idAnimal = self.idAnimal + 1
        st.session_state["animales"] =self.animales
        st.session_state["idAnimal"] =self.idAnimal
        return True
    
    def buscarComida(self, tipoDieta, alimento):
        if alimento in self.comida[tipoDieta]:
            return self.comida[tipoDieta].index(alimento)
        else:
            return -1

    def agregarAlimento(self, tipoDieta, alimento):
        self.comida[tipoDieta].append(alimento)
        st.session_state["comida"] = self.comida
        st.success("%s ha sido agregado con exito a la dieta %s" % (alimento, tipoDieta))
    
    def eliminarAlimento(self, tipoDieta, alimento):
        self.comida[tipoDieta].remove(alimento)
        st.session_state["comida"] = self.comida
        st.success("%s ha sido eliminado con exito a la dieta %s" % (alimento, tipoDieta))

    def mostrarDieta(self, tipoDieta):
        print("Dieta %s:" %tipoDieta)
        for alimento in self.comida[tipoDieta]:
            print("\t%s" % alimento)
        print("-------------------------------")

    def animalesEnHabitats(self):
        idAnimales=[]
        for habitat in self.habitats:
            for animal in habitat.mapaAnimales.values():
                idAnimales.append(animal.id)
        return idAnimales

    def obtenerAnimal(self, id):
        for habitat in self.habitats:
            if id in habitat.mapaAnimales:
                return habitat.mapaAnimales[id]
