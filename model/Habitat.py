class Habitat:
    def __init__(self,nombre, tipo, capacidad, dieta, temperatura):
        self.nombre = nombre
        self.tipo = tipo
        self.capacidad = capacidad
        self.numeroAnimales = 0
        self.dieta = dieta
        self.temperatura = temperatura
        self.mapaAnimales = dict()

    def agregarAnimal(self, Animal):
        id = Animal.id
        self.mapaAnimales[id] = Animal

    def imprimirAnimales(self):
        cont = 1
        print("En %s de tipo %s se encuentran %i animales:\n" %(self.nombre, self.tipo, self.numeroAnimales))

        for key in self.mapaAnimales:
            tempAnimal = self.mapaAnimales[key]

            print("%i)" % cont)
            tempAnimal.mostrarAnimal
            cont += 1
    
    def mostrarHabitats(self):
        cont = 1
        print("%i)" % cont)
        
        print("Nombre: %s\nTipo de habitat: %s\nCapacidad: %i/%i animales\nDieta: %s\nTemperatura: %i" %(self.nombre, self.tipo, self.numeroAnimales, self.capacidad, self.dieta, self.temperatura))
        print("-------------------------------")