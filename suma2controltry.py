def obtener_numero(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Error: El valor ingresado no es un número. Por favor, inténtelo de nuevo.")

def sumar_numeros():
    num1 = obtener_numero("Ingrese el primer número: ")
    num2 = obtener_numero("Ingrese el segundo número: ")
    suma = num1 + num2
    print(f"La suma es: {suma}")

sumar_numeros()