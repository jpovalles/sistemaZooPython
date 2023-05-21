import streamlit as st
import time
import requests

class zooController:
    def __init__(self, modelo, vista):
        self.modelo = modelo
        self.vista = vista
    
    def ejecutarOpcion(self, opcion):
        if opcion == 1:
            try:
                nuevoAnimal =self.vista.menu_crear_animales(self.modelo.idAnimal, self.modelo)
                if nuevoAnimal:
                    self.modelo.agregarAnimal(nuevoAnimal)
            except ValueError:
                self.vista.mostrar_mensaje_error("Se presento un error al crear el animal")
        if opcion == 2: #CrearHabitat
            try:
                nuevoHabitat = self.vista.menuCrearHabitat(self.modelo)
                if nuevoHabitat:
                    self.modelo.agregarHabitat(nuevoHabitat)
            except ValueError:
                self.vista.mostrar_mensaje_error("Se presento un error al crear el habitat")
        if opcion == 3: #ListarHabitats y animales
            self.vista.listarAnimalesHabitats(self.modelo.animales, self.modelo.habitats)
        if opcion == 4: #AccionAnimales
            self.vista.realizarAccion(self.modelo.habitats, self.modelo)
            pass
        if opcion == 5: #agregarAlimento
            try:
                tuplaComida = self.vista.menuAgregarComida()
                if tuplaComida:
                    self.modelo.agregarAlimento(tuplaComida[0], tuplaComida[1])
                    self.vista.imprimirDieta(tuplaComida[0])
            except ValueError:
                self.vista.mostrar_mensaje_error("Se presento un error al crear la comida")
        if opcion == 6: #eliminarAlimento
            try:
                tuplaComida = self.vista.menuEliminarComida()
                if tuplaComida:
                    self.modelo.eliminarAlimento(tuplaComida[0], tuplaComida[1])
                    self.vista.imprimirDieta(tuplaComida[0])
                    time.sleep(3)
                    st.experimental_rerun()
            except ValueError:
                self.vista.mostrar_mensaje_error("Se presento un error al eliminar la comida")
        if opcion == 7:
            self.vista.agregarAnimalHabitat(self.modelo.animales, self.modelo.habitats, self.modelo)
        if opcion ==8:
            self.vista.menuListarPorHabitat()
        if opcion == 9:
            self.vista.menuAnimalAleatorio()
    
    @staticmethod
    def consultarAnimal(nombreAnimal):
        api_url = 'https://api.api-ninjas.com/v1/animals?name=%s' % nombreAnimal
        response = requests.get(api_url, headers={'X-Api-Key': 'zXTgRqeX7ZRefVaI5Z2Htw==I2Jov3xhZCOO9qQe'})

        if response.status_code == requests.codes.ok:
            response_json = response.json()
            print(response_json)
            if len(response_json) == 0:
                st.error("Ingresa una especie valida")
                st.error("NOTA: Recuerda ingresarla en ingles")
                return 0
            else:
                print(len(response_json))
                print(response_json[0])
                return response_json[0]
        else:
            print("Error:", response.status_code, response.text)
            return 0

    def aplicarFormatoA(self, animales):
        datos = []
        for key in animales:
            datos.append([animales[key].id, animales[key].nombre, animales[key].especie, animales[key].tipoHabitat, animales[key].dieta, animales[key].estado, animales[key].edad, animales[key].temperatura, animales[key].horasDormir])
        return datos

    def aplicarFormatoAnimales(self, animales):
        datos = []
        for animal in animales:
            datos.append([animal.id, animal.nombre, animal.especie, animal.tipoHabitat, animal.dieta, animal.estado, animal.edad, animal.temperatura, animal.horasDormir])
        return datos

    def aplicarFormatoH(self, habitats):
        datos = []
        for habitat in habitats:
            datos.append([habitat.nombre, habitat.tipo, habitat.numeroAnimales, habitat.capacidad, habitat.dieta, habitat.temperatura[0], habitat.temperatura[1]])
        return datos
    
    @staticmethod
    def arrNums(min, max):
        return list(range(min, max+1))
