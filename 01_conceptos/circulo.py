class Circulo:
    
    @property
    def area(self):
        return 3.1416 * (self.radio ** 2)

    def __init__(self, radio) -> None:
        self.radio = radio

c = Circulo(10)
print(c.area)
