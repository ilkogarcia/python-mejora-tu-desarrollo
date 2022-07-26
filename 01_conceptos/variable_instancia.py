'''
Las variables de instancias son aquellas que únicamente se relacionan con la
instancia de una clase. En este ejemplo las variables nombre y nacionalidad son
variables de instancias.
'''

class Persona():
    def __init__ (self, nombre, nacionalidad):
        self.nombre = nombre
        self.nacionalidad = nacionalidad

persona_1 = Persona("Jose", "Mexicano")
print(persona_1.nombre, persona_1.nacionalidad)

