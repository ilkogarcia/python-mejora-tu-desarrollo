class Intro():
    Introver = 9
    def __init__(self, valor) -> None:
        self.valor = valor
    def segundo(self):
        print("segundo")
    def tercero(self):
        print("tercero")

dato = Intro("valor")
dir(dato)
print(dir(dato))

print(isinstance(dato, Intro))
print(hasattr(dato, "Introver"))

