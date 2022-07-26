class Perro():
    def avanzar(self):
        print("4 patas")

class Perico():
    def avanzar(self):
        print("volar")

def mover(animal): # Es en esta parte es donde se aprovecha el polimorfismo
    animal.avanzar()

perro = Perro()
perico = Perico()
perro.avanzar()
perico.avanzar()

mover(perro)
mover(perico)
