class Habitat:
    def __init__(self,nombre, tipo, numeroAnimales, dieta):
        self.nombre = nombre
        self.tipo = tipo
        self.numeroAnimales = numeroAnimales
        self.dieta = dieta
        self.mapaAnimales = dict()
    def agregarAnimal(self, Animal):
        id = Animal.id
        self.mapaAnimales[id] = Animal

    def imprimirAnimales(self):
        cont = 1

        print("En %s de tipo %s se encuentran %i animales:\n" %(self.nombre, self.tipo, self.numeroAnimales))

        for key in self.mapaAnimales:
            tempAnimal = self.mapaAnimales[key]
            print("\t%i) ID: %i | Nombre: %s | Especie: %s | Edad: %i | Estado de salud: %s | Dieta: %s | \n" %(cont, tempAnimal.id, tempAnimal.nombre, tempAnimal.especie, tempAnimal.edad, tempAnimal.salud, tempAnimal.dieta))
            print("\t Tipo de habitat: %s | Horas de sueño: %s" %(tempAnimal.tipoHabitat, tempAnimal.horasSueno))