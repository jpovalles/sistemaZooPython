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

    def infoAnimal(self):
        print("Id: ", self.id, " | Nombre: ", self.nombre, " | Especie: ", self.especie, " | Edad: ", self.edad, " | Tipo de habitat: ", self.tipoHabitat)
        print(" | Dieta: ", self.dieta, "\n")

    def juego(self):
        if self.jugar:
            print(self.nombre, " esta cansado para jugar\n")
        else:
            print(self.nombre, " se divirtio jugando\n")
        self.jugar = not self.jugar

    def dormir(self):
        horas = 0
        if self.horasDormir != 0:
            while(horas > self.horasDormir):
                print("Ingresa las horas a dormir: ")
                int(input(horas))
                if(horas > self.horasDormir):
                    print(self.nombre, " deberia dormir menos!\n")
        else:
            print(self.nombre, " ya durmio lo suficiente hoy\n")

        print("Muy bien! ", self.nombre, " descanso lo suficiente\n")
        self.horasDormir -= horas

    def comer(self, alimento, dieta):
        if dieta :
            print(self.nombre, " esta comiendo ", alimento, "\n")
        else:
            print(alimento, " no pertenece a la dieta de ", self.nombre, "\n")

