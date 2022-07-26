class Persona():
    def __init__(self):
        pass

    @classmethod
    def correr(clos): # Este es un método de clase
        print("Estoy corriendo")

    def brincar(self): # Este es un método de instancia
        print("Estoy brincando")

    @staticmethod    
    def nadar(): # Este es un método estático
        print("Estoy nadando")
    
jose = Persona()
jose.nadar()

juan = Persona()
juan.brincar()

Persona.correr()

