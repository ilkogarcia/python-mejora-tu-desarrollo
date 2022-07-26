'''
Los metodos de instancia....
'''

class Persona():
    def __init__ (self, nombre, nacionalidad):
        self.nombre = nombre
        self.nacionalidad = nacionalidad
    def nadar(self):
        print("Estoy nadando")

persona_1 = Persona("Jose", "Mexicano")
persona_1.nadar()

print(persona_1.nombre, persona_1.nacionalidad)

