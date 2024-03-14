
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
        1005 :
        1006 :
        1007 :
        1008 :
        1009 :
        1010 : 
        
        1037 : 
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
                print("")
        elif opcion == 1010:
                # Ejercicio 1010
                valores_1 = input().split(" ")
                valores_2 = input().split(" ")
                
                suma_total_p1 = float(valores_1[1]) * float(valores_1[2])
                suma_total_p2 = float(valores_2[1]) * float(valores_2[2])
                
                suma_final = suma_total_p1 + suma_total_p2
                
                print(f"VALOR A PAGAR: R$ {suma_final:.2f}")
        else:
                print("La opcion seleccionada no existe")
 
