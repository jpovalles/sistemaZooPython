import model.Animal as animalModel
import model.Habitat as habitatModel
import model.Zoo as zooModel
import controller.zooController as zooControl
import streamlit as st
import pandas as pd
import requests
import time





class sistema:
    def __init__(self):
        self.zoologico = zooModel.Zoo(0)
        self.controlador = zooControl.zooController(self.zoologico, self)

    def mostrarMenu(self):
        st.title("Bienvenido al GlizzyZoo 🐾")

        with st.sidebar:
                botonmenuEliminarComida = False
                botonmenuAgregarComida = False
    
                botonCrearAnimal = st.button("Crear animal",key=1, use_container_width = True)
                botonCrearHabitat = st.button("Crear habitat",key=2, use_container_width = True)
                botonAccionAgregar=st.button("Animal al habitat", key=7, use_container_width = True)
                botonListarHabitats = st.button("Listar habitats/animales",key=3, use_container_width = True)
                botonListarPorHabitat = st.button("Listar animales por habitat", key=10, use_container_width=True)
                botonAccionAnimales = st.button("Ejecuta una accion",key=4, use_container_width = True)
                botonmenuEliminarComida = st.button("Eliminar comida", key=5, use_container_width = True)
                botonmenuAgregarComida = st.button("Agregar comida", key=6, use_container_width = True)
                botonAnimalAleatorio = st.button("Datos curiosos", key=11, use_container_width = True)

        if botonCrearAnimal:
            st.session_state["opcion"] = 1
        elif botonCrearHabitat:
            st.session_state["opcion"] = 2
        elif botonListarHabitats:
            st.session_state["opcion"] = 3
        elif botonAccionAnimales:
            st.session_state["opcion"] = 4
        elif botonmenuAgregarComida:
            st.session_state["opcion"] = 5
        elif botonmenuEliminarComida:
            st.session_state["opcion"] = 6
        elif botonAccionAgregar:
            st.session_state["opcion"] = 7
        elif botonListarPorHabitat:
            st.session_state["opcion"] = 8
        elif botonAnimalAleatorio:
            st.session_state["opcion"] = 9
            
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
                st.success("NOTA: Recuerda agregar el animal a un habitat")
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
    
    def menuEliminarComida(self):
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

    
    def menuAgregarComida(self):
        st.divider()
        with st.container():
            st.subheader("Agregar alimento")
            tipoDieta = st.selectbox("Selecciona el tipo de dieta", self.zoologico.dietas)
            alimento = st.text_input("Ingresa el alimento a agregar")

            boton = st.button("Agregar comida")
            if boton:
                return (tipoDieta, alimento)
            
    def menuListarPorHabitat(self):
        st.divider()
        with st.container():
            st.subheader("Animales en el GlizzyZoo 🐾")
            if len(self.zoologico.habitats) == 0:
                st.error("No hay habitats para listar animales")
            else:
                nombreHabitats = []
                for habitat in self.zoologico.habitats:
                    opcion = habitat.nombre + " | " + habitat.tipo + " | " + habitat.dieta
                    nombreHabitats.append(opcion)

                habitat = st.selectbox("Selecciona el habitat a listar", nombreHabitats)

                animales = self.zoologico.habitats[nombreHabitats.index(habitat)].mapaAnimales

                if len(animales) == 0:
                    st.error("No hay animales para mostrar en este habitat")
                else:
                    boton = st.button("Listar animales")
                    if boton:
                        datoAnimales = pd.DataFrame(
                            self.controlador.aplicarFormatoA(animales),
                            columns = ["ID del animal", "Nombre", "Especie", "Tipo del habitat", "Dieta", "Estado de salud", "Edad", "Temperatura optima", "Horas de sueño"]
                        )
                        st.table(datoAnimales)

    def menuAnimalAleatorio(self):
        st.divider()
        with st.container():
            st.subheader("Genera datos curiosos sobre animales")

            animal = st.text_input("Escribe una especie sobre la que te gustaria conocer más!")
            st.warning("NOTA: Recuerda ingresar la especie en ingles")

            boton = st.button("Consultar")

            if boton:
                animalApi = self.controlador.consultarAnimal(animal)

                if animalApi != 0:
                    listaAtributos = [animalApi['name'], animalApi['taxonomy']['kingdom'], animalApi['taxonomy']['phylum'], animalApi['taxonomy']['class'], animalApi['taxonomy']['order'], animalApi['taxonomy']['family'], animalApi['taxonomy']['genus'], animalApi['taxonomy']['scientific_name'], animalApi['locations'][0]]

                    st.divider()
                    with st.container():
                        st.markdown('# This is the %s!' % listaAtributos[0])
                        st.markdown('## Location: %s' % listaAtributos[8])
                        st.markdown('* **Kingdom:** %s\n* **Phylum:** %s\n* **Class:** %s\n* **Order:** %s\n* **Family:** %s\n* **Genus:** %s\n* **Scientific name:** %s' % (listaAtributos[1], listaAtributos[2], listaAtributos[3], listaAtributos[4], listaAtributos[5], listaAtributos[6], listaAtributos[7]))

                        '''
                        st.markdown('# This is the %s' % listaAtributos[0])
                        st.markdown('## %s' % listaAtributos[1])
                        st.markdown('It is a **%s** animal and its diet is based on **%s**, but their favorite is **%s**.' % (listaAtributos[2], listaAtributos[3], listaAtributos[4]))
                        st.markdown('It lives in %s and its habitat is the %s, and they lead a %s lifestyle.' % (listaAtributos[5], listaAtributos[6], listaAtributos[7]))
                        st.markdown('* **Top speed:** %s\n* **Life expectancy:** %s\n* **Weight:** %s' % (listaAtributos[8], listaAtributos[9], listaAtributos[10]))
                        '''
                    botonLimpiar = st.button("Limpiar busqueda")
                    if botonLimpiar:
                        st.experimental_rerun()

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