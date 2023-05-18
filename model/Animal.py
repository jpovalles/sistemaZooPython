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
        self.horasDormidas = 0
        self.jugar = jugar

    def juego(self):
        if self.jugar:
            return False
        else:
            self.jugar = True
            return True


    def dormir(self, cantHoras):
        self.horasDormidas += cantHoras
        return True
