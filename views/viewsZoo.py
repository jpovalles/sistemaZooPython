import model.Animal as animalModel
import model.Habitat as habitatModel
import model.Zoo as zooModel
import controller.zooController as zooControl
import streamlit as st

class sistema:
    def __init__(self):
        self.zoologico = zooModel.Zoo(0)
        self.controlador = zooControl.zooController(self.zoologico, self)
    
    def mostrarMenu(self):
        st.title("Bienvenido al GlizzyZoo 🐾")
        with st.container():
            col1, col2 = st.columns(2)
            col1.header("Crear animal")
            botonCrearAnimal = col1.button("Acceder a esta opcion",1)
            col2.header("Crear habitat")
            botonCrearHabitat = col2.button("Acceder a esta opcion",2)
        
        with st.container():
            col1, col2 = st.columns(2)
            col1.header("Listar habitats/animales")
            botonListarHabitats = col1.button("Acceder a esta opcion",3)
            col2.header("Ejecuta una accion")
            botonAccionAnimales = col2.button("Acceder a esta opcion",4)

        with st.container():
            col1, col2 = st.columns(2)
            col1.header("Editar dietas")
            botonEditarDietas = col1.button("Acceder a esta opcion",)