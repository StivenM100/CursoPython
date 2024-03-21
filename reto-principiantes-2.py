


menu = """"
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
    else:
        print("La opcion seleccionada no existe")
    