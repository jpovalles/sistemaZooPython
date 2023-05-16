class Zoo:
    def __init__(self, idAnimal):
        self.idAnimal = idAnimal
        self.comida = {}
        self.habitats = []
        self.animales = []
        self.comida["Carnivoro"] = []
        self.comida["Omnivoro"] = []
        self.comida["Herbivoro"] = []
    
    def agregarHabitat(self, habitat):
        self.habitats.append(habitat)
        return True

    def agregarAnimal(self, animal):
        self.animales.append(animal)
        self.idAnimal = self.idAnimal + 1
        return True
    
    def buscarComida(self, tipoDieta, alimento):
        if alimento in self.comida[tipoDieta]:
            return self.comida[tipoDieta].index(alimento)
        else:
            return -1
    
    def agregarAlimento(self, tipoDieta, alimento):
        self.comida[tipoDieta].append(alimento)
    
    def eliminarAlimento(self, tipoDieta, index):
        self.comida[tipoDieta].pop(index)

    def mostrarDieta(self, tipoDieta):
        print("Dieta %s:" %tipoDieta)
        for alimento in self.comida[tipoDieta]:
            print("\t%s" % alimento)
        print("-------------------------------")