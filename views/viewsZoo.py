import model.Animal as animalModel
import model.Habitat as habitatModel
import model.Zoo as zooModel
import controller.zooController as zooControl
import streamlit as st
import pandas as pd

class sistema:
    def __init__(self):
        self.zoologico = zooModel.Zoo(0)
        self.controlador = zooControl.zooController(self.zoologico, self)

    
    

    def mostrarMenu(self):

        st.title("Bienvenido al GlizzyZoo 🐾")

        with st.sidebar:
                st.header("Elige una opcion:")
                botonEliminarComida = False
                botonAgregarComida = False
    
                botonCrearAnimal = st.button("Crear animal",key=1, use_container_width = True)
                botonCrearHabitat = st.button("Crear habitat",key=2, use_container_width = True)
                botonListarHabitats = st.button("Listar habitats/animales",key=3, use_container_width = True)
                botonAccionAnimales = st.button("Ejecuta una accion",key=4, use_container_width = True)
                botonEliminarComida = st.button("Eliminar comida", key=5, use_container_width = True)
                botonAgregarComida = st.button("Agregar comida", key=6, use_container_width = True)
                botonAccionAgregar=st.button("Animal al habitat", key=7, use_container_width = True)
        if botonCrearAnimal:
            st.session_state["opcion"] = 1
        elif botonCrearHabitat:
            st.session_state["opcion"] = 2
        elif botonListarHabitats:
            st.session_state["opcion"] = 3
        elif botonAccionAnimales:
            st.session_state["opcion"] = 4
        elif botonAgregarComida:
            st.session_state["opcion"] = 5
        elif botonEliminarComida:
            st.session_state["opcion"] = 6
        elif botonAccionAgregar:
            st.session_state["opcion"] = 7

        if "opcion" in st.session_state:
            self.controlador.ejecutarOpcion(st.session_state["opcion"])


    def menu_crear_animales(self, idAnimal):
        st.divider()
        with st.container():
            st.subheader("Formulario para agregar animal al Zoo")
            habitats = ["Desertico", "Selvatico", "Acuatico", "Polar"]
            tiposDietas = ["Carnivoro", "Herbivoro", "Omnivoro"]
            id = idAnimal
            nombre = st.text_input("Nombre del animal: ")
            especie = st.text_input("Especie: ")
            estado = st.text_input("Describa el estado de salud del animal: ")
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

        
    def menuCrearHabitat(self):
        arrNums = list(range(-10, 41))
        st.divider()
        with st.container():
            st.subheader("Formulario para crear e ingresar un nuevo habitat")
            nombre = st.text_input("Nombre del habitat:", key=7)
            tipoHabitat = st.selectbox("Elige el tipo de habitat:", self.zoologico.tipos)
            capacidad = st.slider("Ingresa la capacidad del habitat:", key = 8, min_value = 1, max_value = 10, step = 1)
            dieta = st.selectbox("Elige el tipo de dieta del habitat:", self.zoologico.dietas)
            temperatura = st.select_slider("Ingresa el rango de temperatura", options = arrNums, value = (-10,40))
            botonAccion = st.button("Ingresar habitat")

        if botonAccion:
            if tipoHabitat == "Desertico":
                nuevoHabitat = habitatModel.desertico(nombre, tipoHabitat, capacidad, dieta, temperatura)
            elif tipoHabitat == "Selvatico":
                nuevoHabitat = habitatModel.selvatico(nombre, tipoHabitat, capacidad, dieta, temperatura)
            elif tipoHabitat == "Polar":
                nuevoHabitat = habitatModel.polar(nombre, tipoHabitat, capacidad, dieta, temperatura)
            elif tipoHabitat == "Acuatico":
                nuevoHabitat = habitatModel.acuatico(nombre, tipoHabitat, capacidad, dieta, temperatura)
            st.success("El habitat fue creado correctamente")
            return nuevoHabitat
        
    def listarAnimalesHabitats(self, animales, habitats):
        st.divider()
        with st.container():
            st.subheader("Listado de animales")
            if len(animales) == 0:
                st.error("No hay animales para listar")
            else:
                datoAnimales = pd.DataFrame(
                    self.controlador.aplicarFormatoA(animales),
                    columns = ["ID del animal", "Nombre", "Especie", "Tipo del habitat", "Dieta", "Estado de salud", "Edad", "Temperatura optima", "Horas de sueño"]
                )
                st.table(datoAnimales)
            
            st.subheader("Listado de habitats")
            if len(habitats) == 0:
                st.error("No hay habitats para listar")
            else:
                datosHabitats = pd.DataFrame(
                    self.controlador.aplicarFormatoH(habitats),
                    columns = ["Nombre", "Tipo de habitat", "Alojados", "Capacidad", "Dieta", "Temp minima", "Temp maxima"]
                )
                st.table(datosHabitats)

    def agregarAnimalHabitat(self, animales, habitats):
        st.divider()
        with st.container():
            st.subheader("Agregar animal a habitat")
            if len(animales)==0:
                st.error("No hay animales para agregar")
            #elif len(habitats)==0:
                #st.error("No hay habitats para recibir animales")
            else:
                id = st.selectbox("Animal que desea agregar: ", animales.keys())
                animalSeleccionado = self.getInfo(id, animales)
                datosAnimal = [animalSeleccionado.id, animalSeleccionado.nombre, animalSeleccionado.habitat, animalSeleccionado.dieta]
                datos = pd.DataFrame(
                    datosAnimal,
                    columns=["Id del animal", "Nombre", "Habitat", "dieta"]
                )
                st.table(datos)
                nombreH = st.selectbox("Seleccione el habitat del animal: ")
    
    def eliminarComida(self):
        pass

    
    def agregarComida(self):
        st.divider()
        with st.container():
            st.subheader("Agregar alimento")
            tipoDieta = st.selectbox("Selecciona el tipo de dieta", self.zoologico.dietas)
            alimento = st.text_input("Ingresa el alimento a agregar")

            boton = st.button("Agregar comida")
            if boton:
                return (tipoDieta, alimento)

    def getInfo(self, id, animales):
        for animal in animales:
            if animal.id == id:
                return animal

    def mostrar_mensaje_exitoso(self, mensaje):
        st.success(mensaje)

    def mostrar_mensaje_error(self, mensaje):
        st.error(mensaje)