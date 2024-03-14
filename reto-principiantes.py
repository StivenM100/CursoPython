
# Estructuras de Control

menu = """
       ****************************************************
       *        MENU PRINCIPAL DE LA APLICACION           * 
       ****************************************************

        Elija la opcion del reto que desea ejecutar: 
        1000 : Hello World!
        1001 : Suma Simple
        1002 : Area de un Circulo   
        1003 : Suma 2 numeros
        1004 : Multiplicacion 2 numeros
        1005 : Promedio 1
        1006 : Promedio 2
        1007 : Diferencia
        1008 : Salario
        1009 : Salario con Bonus
        1010 : Cálculo Simple
        1011 : Esfera
        1012 : Área
        1013 : El Mayor
        1014 : Consumo
        1015 : Distancia Entre dos Puntos
        1016 : Distancia
        1017 : Combustible Gastado
        1018 : Billetes
        1019 : Conversión de Tiempo
        1020 : Edad en Días
        1021 : Billetes y Monedas
        1035 : Prueba de Selección 1
        1036 : Fórmula de Bhaskara
        1037 : Intervalo
        0 : Salir programa
"""
bandera = True

while bandera:
        print(menu)
        opcion = int(input("Elija una opción: \n"))
        if opcion == 0:
                print("Hasta pronto!!")
                break
        elif opcion == 1000:
                # Ejercicio 1000
                print("Hello World!")
        elif opcion == 1001:
                # Ejercicio 1001
                A = int(input("Ingrese #1 de la suma : \n"))
                B = int(input("Ingrese #2 de la suma : \n"))
                X = A + B
                print(f"X = {X}")
        elif opcion == 1002:
                # Ejercicio 1002
                pi = 3.14159
                radio = float(input("Ingrese el radio de la circunferencia : \n"))
                area = pi * radio**2
                print (f"A={area:.4f}")
        elif opcion == 1003:
                # Ejercicio 1003
                A = int(input("Ingrese #1 de la suma : \n"))
                B = int(input("Ingrese #2 de la suma : \n"))
                
                SOMA = A + B
                print(f"SOMA = {SOMA}")
        elif opcion == 1004:
                # Ejercicio 1004
                A = int(input("Ingrese #1 de la multiplicación : \n"))
                B = int(input("Ingrese #1 de la multiplicación : \n"))
                
                PROD = A * B
                print(f"PROD = {PROD}")
        elif opcion == 1005:
                #Ejercicio 1005
                A = float(input("Ingrese nota A : \n")) 
                B = float(input("Ingrese nota B : \n"))
                
                media = (A * 3.5 + B * 7.5) / (3.5 + 7.5)
                
                print(f"MEDIA = {media:.5f}")
        elif opcion == 1006:
                # Ejercicio 1006
                A = float(input("Ingrese nota A \n"))
                B = float(input("Ingrese nota B \n"))
                C = float(input("Ingrese nota C \n"))
                
                media = (A * 2 + B * 3 + C * 5) / (2 + 3 + 5)
                
                print(f"MEDIA = {media:.1f}")
        elif opcion == 1007:
                # Ejercicio 1007
                A = int(input("Ingrese número A \n"))
                B = int(input("Ingrese número B \n"))
                C = int(input("Ingrese número C \n"))
                D = int(input("Ingrese número D \n"))
                
                diferencia = (A * B) - (C * D)
                
                print(f"DIFERENCA = {diferencia}")
        elif opcion == 1008:
                # Ejercicio 1008
                numero = int(input("Ingrese el número de empleado \n"))
                horas = int(input("Ingrese el número de horas trabajadas en el mes \n"))
                monto = float(input("Ingrese el monto recibido por hora \n"))
                
                salario = horas * monto
                
                print(f"NUMBER = {numero}")
                print(f"SALARY = U$ {salario:.2f}")
        elif opcion == 1009:
                # Ejercicio 1009
                nombre = input("Ingrese el nombre del vendedor \n")
                salario = float(input("Ingrese el salario fijo del vendedor \n"))
                ventas = float(input("Ingrese el total de las ventas realizadas por el vendedor en el mes \n"))
                
                total = salario + (ventas * 0.15)
                
                print(f"TOTAL = R$ {total:.2f}")
        elif opcion == 1010:
                # Ejercicio 1010
                valores_1 = input('Ingrese código(a), número de unidades(b) y el precio del producto(c) 1 "a b c" \n').split(" ")
                valores_2 = input('Ingrese código(a), número de unidades(b) y el precio del producto(c) 2 "a b c" \n').split(" ")
                
                suma_total_p1 = float(valores_1[1]) * float(valores_1[2])
                suma_total_p2 = float(valores_2[1]) * float(valores_2[2])
                
                suma_final = suma_total_p1 + suma_total_p2
                
                print(f"VALOR A PAGAR: R$ {suma_final:.2f}")
        elif opcion == 1011:
                # Ejercicio 1011
                R = int(input("Ingrese el radio de la esfera \n"))
                pi = 3.14159
                
                volumen = (4.0/3)*pi*R**3
                
                print(f"VOLUME = {volumen:.3f}")
        elif opcion == 1012:
                # Ejercicio 1012
                valores = input('Ingrese valores de la siguiente manera "a b c" \n').split(" ")
                A = float(valores[0])
                B = float(valores[1])
                C = float(valores[2])
                
                triangulo = (A * C) / 2
                circulo = 3.14159 * C**2
                trapecio = (A + B) * (C / 2)
                cuadrado = B**2
                rectangulo = A * B
                
                print(f"TRIANGULO: {triangulo:.3f}")
                print(f"CIRCULO: {circulo:.3f}")
                print(f"TRAPEZIO: {trapecio:.3f}")
                print(f"QUADRADO: {cuadrado:.3f}")
                print(f"RETANGULO: {rectangulo:.3f}")
        elif opcion == 1013:
                # Ejercicio 1013
                valores = input('Ingrese 3 numeros de la siguiente manera "a b c" \n').split(" ")
                
                A = int(valores[0])
                B = int(valores[1])
                C = int(valores[2])
                
                mayor_1 = (A + B + abs(A - B)) / 2
                mayor_2 = (mayor_1 + C + abs(mayor_1 - C)) / 2
                
                print(f"{int(mayor_2)} eh o maior")
        elif opcion == 1014:
                # Ejercicio 1014
                X = int(input("Ingrese la distancia total en km (número entero) \n"))
                Y = float(input("Ingrese el total de combustible gastado (con un decimal) \n"))
                
                consumo = X / Y
                
                print(f"{consumo:.3f} km/l")

        else:
                print("La opcion seleccionada no existe")
 
