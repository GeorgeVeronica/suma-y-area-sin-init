def calcular_area(base, altura):
    return (base * altura) / 2

def main():
    base = float(input("Ingrese la base del triángulo: "))
    altura = float(input("Ingrese la altura del triángulo: "))
    area = calcular_area(base, altura)
    print(f"El área del triángulo es: {area}")

if __name__ == "__main__":
    main()