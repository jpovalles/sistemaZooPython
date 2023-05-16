class zooController:
    def __init__(self, modelo, vista):
        self.modelo = modelo
        self.vista = vista
    
    def ejecutarOpcion(self, opcion):
        if opcion == 1:
            try:
                nuevoAnimal =self.vista.menu_crear_animales(self.modelo.idAnimal)
                if nuevoAnimal:
                    self.modelo.agregarAnimal(nuevoAnimal)
            except ValueError:
                self.vista.mostrar_mensaje_error("Se presento un error al crear el animal")

            pass
        if opcion == 2: #CrearHabitat
            pass
        if opcion == 3: #ListarHabitats y animales
            pass
        if opcion == 4: #AccionAnimales
            pass
        if opcion == 5: #editarDietas
            pass
