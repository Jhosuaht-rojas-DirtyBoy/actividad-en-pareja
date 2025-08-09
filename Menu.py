from Funciones import suma, resta  

while True:
    print("\n=== Calculadora Parte 1: Suma y Resta ===")
    print("1. Suma")
    print("2. Resta")
    print("3. Salir")

    opcion = input("Elige una opción (1-3): ")

    if opcion == "3":
        print("Saliendo de la calculadora parte 1...")
        break

    if opcion in ["1", "2"]:
        try:
            num1 = float(input("Ingrese el primer número: "))
            num2 = float(input("Ingrese el segundo número: "))
        except ValueError:
            print("Error: Debes ingresar solo números.")
            continue

        if opcion == "1":
            print(f"El resultado de la suma es {suma(num1, num2)}")
        elif opcion == "2":
            print(f"El resultado de la resta es {resta(num1, num2)}")
    else:
        print("Opción no válida. Intenta de nuevo.")
