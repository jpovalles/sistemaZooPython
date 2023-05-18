class Animal:
    def __init__(self, nombre, especie, tipoHabitat, dieta, estado, id, edad, temperatura ,horasDormir, jugar):
        self.nombre = nombre
        self.especie = especie
        self.tipoHabitat = tipoHabitat
        self.dieta = dieta
        self.estado = estado
        self.id = id
        self.edad = edad
        self.temperatura = temperatura
        self.horasDormir = horasDormir
        self.jugar = jugar

    def juego(self):
        if self.jugar:
            return False
        else:
            self.jugar = True
            return True


    def dormir(self, cantHoras):
        self.horasDormir -= cantHoras
        return True

    def comer(self, alimento, dieta):
        if dieta :
            print(self.nombre, " esta comiendo ", alimento, "\n")
        else:
            print(alimento, " no pertenece a la dieta de ", self.nombre, "\n")
