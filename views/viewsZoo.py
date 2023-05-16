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
            col2.header("Agregar animal a habitat")
            botonAccionAgregar=col2.button("Acceder a esta opcion", 6)


    def menu_crear_animales(self, idAnimal):
        st.divider()
        with st.container():
            st.subheader("Formulario para agregar animal al Zoo")
            habitats = ["Desertico", "Selvatico", "Acuatico", "Polar"]
            tiposDietas = ["Carnivoro", "Herbivoro", "Omnivoro"]
            id = idAnimal
            nombre = st.text_input("Nombre del animal: ")
            especie = st.text_input("Especie: ")
            estado = st.text.input("Describa el estado de salud del animal: ")
            habitat = st.selectbox("Habitat del animal: ", habitats)
            dieta = st.selectbox("Dieta del animal: ", tiposDietas)
            temperatura = st.slider("Temperatura soportada por el animal: ", min_value=-10, max_value=40, step=1 )
            edad = st.slider("Cual es la edad del animal?: ", min_value=0, max_value=15, step=1)
            horasDormir = st.slider("Cuantas horas necesita dormir el animal al dia: ", min_value=1, max_value=24, step=1)
            botonAccion = st.button("Crear animal")

            if botonAccion:
                nuevoAnimal = animalModel.Animal(nombre, especie, habitat, dieta, estado, id, edad, temperatura, horasDormir, True)
                st.success("Animal agregado al registro del Zoo correctamente")
                return nuevoAnimal

    def mostrar_mensaje_exitoso(self, mensaje):
        st.success(mensaje)
    def mostrar_mensaje_error(self, mensaje):
        st.error(mensaje)
