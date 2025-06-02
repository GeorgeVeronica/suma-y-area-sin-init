class Triangulo:
    def _init_(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return (self.base * self.altura) / 2

try:
    base = float(input("Ingrese la base del triángulo: "))
    altura = float(input("Ingrese la altura del triángulo: "))
    triangulo = Triangulo(base, altura)
    print("El área del triángulo es:", triangulo.calcular_area())
except ValueError:
    print("Error: Ingrese solo números válidos.")