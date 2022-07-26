'''
Las variables de clase son aquellas que pertenecen a la clase general
y no a sus instancias. En este ejemplo las variables nombre y nacionalidad son
variables de instancias. En este ejemplo agregamos una clase Persona con una
variable de clase de nombre Edad.
'''

class Persona():
    edad = 18
    def __init__ (self, nombre, nacionalidad):
        self.nombre = nombre
        self.nacionalidad = nacionalidad

persona_1 = Persona("Jose", "Mexicano")
print(persona_1) # esto imprime el tipo de objeto
print(persona_1.nombre, persona_1.nacionalidad) # imprime valor de variables de instancia
print(Persona.edad) # imprime la variable de la clase Persona
# print(Persona.nombre) Esto daría error porque la variable no se ha creado

