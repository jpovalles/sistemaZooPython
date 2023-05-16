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
            botonEditarDietas = col1.button("Acceder a esta opcion",5)
        
        if botonCrearAnimal:
            st.session_state["opcion"] = 1
        elif botonCrearHabitat:
            st.session_state["opcion"] = 2
        elif botonListarHabitats:
            st.session_state["opcion"] = 3
        elif botonAccionAnimales:
            st.session_state["opcion"] = 4
        elif botonEditarDietas:
            st.session_state["opcion"] = 5
        
        if "opcion" in st.session_state:
            self.controlador.ejecutarOpcion(st.session_state["opcion"])
        
    def menuCrearHabitat(self, Zoo):
        st.divider()
        with st.container:
            st.subheader("Formulario para crear e ingresar un nuevo habitat")
            nombre = st.text_input("Nombre del habitat:", key=6)
            tipoHabitat = st.selectbox("Elige el tipo de habitat:", Zoo.tipos)
            capacidad = st.slider("Ingresa la capacidad del habitat:", key = 7, min_value = 1, max_value = 10, step = 1)
            dieta = st.selectbox("Elige el tipo de dieta del habitat:", Zoo.dietas)
            temp = st.select_slider("Ingresa el rango de temperatura",value=(-10, 40))
            botonAccion = st.button("Ingresar habitat")

        if botonAccion:
            pass
