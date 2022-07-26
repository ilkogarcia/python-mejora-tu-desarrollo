class Persona():
    def __init__(self):
        pass

    def despedir(self):
        print("Adios")

    @classmethod
    def saludar(cls, nombre):
        # Este será nuestro método de clase
        print(f"Hola, me llamo {nombre}, ¿que tal?")


Persona.saludar("Juan")
