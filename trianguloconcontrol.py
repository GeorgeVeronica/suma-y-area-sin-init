def obtener_numero(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Error: El valor ingresado no es un número. Por favor, inténtelo de nuevo.")

def area_triangulo():
    base = obtener_numero("Ingresa la base: ")
    altura = obtener_numero("Ingrese la altura: ")
    area = base*altura/2
    print(f"La area del triangulo es: {area}")

area_triangulo()