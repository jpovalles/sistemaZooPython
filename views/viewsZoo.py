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
                botonEliminarComida = False
                botonAgregarComida = False
    
                botonCrearAnimal = st.button("Crear animal",key=1, use_container_width = True)
                botonCrearHabitat = st.button("Crear habitat",key=2, use_container_width = True)
                botonListarHabitats = st.button("Listar habitats/animales",key=3, use_container_width = True)
                botonAccionAnimales = st.button("Ejecuta una accion",key=4, use_container_width = True)
                botonEliminarComida = st.button("Eliminar comida", key=5, use_container_width = True)
                botonAgregarComida = st.button("Agregar comida", key=6, use_container_width = True)
                botonAccionAgregar=st.button("Animal al habitat", key=7, use_container_width = True)
                botonListarPorHabitat = st.button("Listar animales por habitat", key=10, use_container_width=True)

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


    def menu_crear_animales(self, idAnimal, zoo):
        st.divider()

        with st.container():
            st.subheader("Formulario para agregar animal al Zoo")
            nombre = st.text_input("Nombre del animal: ")
            especie = st.text_input("Especie: ")
            estado = st.text_input("Describa el estado de salud del animal: ")
            habitat = st.selectbox("Habitat del animal: ", zoo.tipos)
            dieta = st.selectbox("Dieta del animal: ", zoo.dietas)
            temperatura = st.slider("Temperatura soportada por el animal: ", min_value=-10, max_value=40, step=1 )
            edad = st.slider("Cual es la edad del animal?: ", min_value=0, max_value=15, step=1)
            horasDormir = st.slider("Cuantas horas necesita dormir el animal al dia: ", min_value=1, max_value=24, step=1)
            botonAccion = st.button("Crear animal")

            if botonAccion:
                nuevoAnimal = animalModel.Animal(nombre, especie, habitat, dieta, estado, idAnimal, edad, temperatura, horasDormir, True)
                st.success("Animal agregado al registro del Zoo correctamente")
                return nuevoAnimal

        
    def menuCrearHabitat(self):
        arrNums = list(range(-10, 41))
        st.divider()
        with st.container():
            st.subheader("Formulario para crear e ingresar un nuevo habitat")
            nombre = st.text_input("Nombre del habitat:", key=8)
            tipoHabitat = st.selectbox("Elige el tipo de habitat:", self.zoologico.tipos)
            capacidad = st.slider("Ingresa la capacidad del habitat:", key = 9, min_value = 1, max_value = 10, step = 1)
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
            else:
                id = st.selectbox("Animal que desea agregar: ", animales.keys())
                animalSel = self.getInfo(id, animales)
                datos = pd.DataFrame(
                    [[animalSel.id, animalSel.nombre, animalSel.tipoHabitat, animalSel.dieta, animalSel.temperatura]],
                    columns=["Id del animal", "Nombre", "Habitat", "Dieta", "Temperatura optima"]
                )
                st.table(datos)
                opcionesHabitats = []
                for habitat in habitats:
                    if habitat.tipo == animalSel.tipoHabitat:
                        opcionesHabitats.append(habitat.nombre)
                if len(opcionesHabitats)==0:
                    self.mostrar_mensaje_error("No hay habitats disponibles para este animal")
                else:
                    nombreH = st.selectbox("Seleccione el habitat del animal: ", opcionesHabitats)
                    habitatSel = self.obtenerHabitat(nombreH, habitats)
                    datosH = pd.DataFrame(
                        [[habitatSel.nombre, habitatSel.tipo, habitatSel.capacidad, habitatSel.numeroAnimales,habitat.dieta, habitat.temperatura]],
                        columns=["Nombre Habitat", "Tipo", "Capacidad", "Numero Animales", "Dieta", "Rango Temperatura"]
                    )
                    st.table(datosH)
                    botonAgregar = st.button("Agregar a este habitat")
                    if botonAgregar:
                        if habitatSel.capacidad == habitatSel.numeroAnimales:
                            self.mostrar_mensaje_error("El habitat esta lleno")
                        elif animalSel.temperatura < habitatSel.temperatura[0] or animalSel.temperatura > habitatSel.temperatura[1]:
                            self.mostrar_mensaje_error("El animal no soportaría la temperatura del habitat")
                        elif animalSel.dieta != habitatSel.dieta:
                            self.mostrar_mensaje_error("Este habitat no está diseñado para un animal con esta alimentación")
                        else:
                            habitatSel.agregarAnimal(animalSel)
                            self.mostrar_mensaje_exitoso("El animal se agregó al habitat")
    
    def eliminarComida(self):
        st.divider()

        tipoDieta = st.selectbox("Selecciona el tipo de dieta", self.zoologico.dietas)

        with st.container():
            if len(self.zoologico.comida[tipoDieta]) == 1:
                st.error("La dieta debe contener al menos un alimento")
            else:
                alimento = st.selectbox("Seleccione la comida a eliminar", self.zoologico.comida[tipoDieta])
                boton = st.button("Eliminar alimento")
                if boton:
                    return (tipoDieta, alimento)

    
    def agregarComida(self):
        st.divider()
        with st.container():
            st.subheader("Agregar alimento")
            tipoDieta = st.selectbox("Selecciona el tipo de dieta", self.zoologico.dietas)
            alimento = st.text_input("Ingresa el alimento a agregar")

            boton = st.button("Agregar comida")
            if boton:
                return (tipoDieta, alimento)

    def imprimirDieta(self, tipoDieta):
        st.divider()
        with st.container():
            if len(self.zoologico.comida[tipoDieta]) == 0:
                st.error("La dieta esta vacia")
            else:
                datoDieta = pd.DataFrame(
                    self.zoologico.comida[tipoDieta],
                    columns = [tipoDieta]
                )
                st.table(datoDieta)

    def getInfo(self, id, animales):
        for animal in animales.keys():
            if animal == id:
                return animales[animal]

    def obtenerHabitat(self, nombreH, habitats):
        for habitat in habitats:
            if nombreH == habitat.nombre:
                return habitat
    def mostrar_mensaje_exitoso(self, mensaje):
        st.success(mensaje)

    def mostrar_mensaje_error(self, mensaje):
        st.error(mensaje)