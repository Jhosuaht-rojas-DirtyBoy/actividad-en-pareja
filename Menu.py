while True:
    
    print("\n=== Calculadora de Multiplicación y División ===")
    print("3. Multiplicación")
    print("4. División")
  

    opcion = input("Elige una opción (3, 4): ")

    if opcion in ["3", "4"]:
      
        try:
            num1 = float(input("Ingrese el primer número: "))
            num2 = float(input("Ingrese el segundo número: "))
        except ValueError:
            print("Error: Debes ingresar solo números.")
            continue

        
        if opcion == "3":
            print(f"El resultado de la multiplicación es {multiplicacion(num1, num2)}")
        else:
            print(f"El resultado de la división es {division(num1, num2)}")
