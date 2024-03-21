


menu = """"
       ****************************************************
       *        MENU PRINCIPAL DE LA APLICACION           * 
       ****************************************************

        Elija la opcion del reto que desea ejecutar: 
        1038 : Snack
        1040 : Promedio 3
        1041 : Coordenadas de un Punto
        1042 : Clasificación Simple
        1043 : Triángulo
        1044 : Múltiplos
        1045 : Tipos de Triángulos
        1046 : Tiempo de Juego
        1047 : Tiempo de Juego con Minutos
        1048 : Incremento Salarial
        1049 : Animal
        1050 : DDD
        1051 : Impuestos
        1052 : Mes
        1059 : Números Pares
        1060 : Números Positivos
        1061 : Tiempo Del Evento
        1064 : Positivos y Promedio
        1065 : Pares Entre Cinco Números
        1066 : Par, Impar, Postivo y Negativo
        1067 : Números Impares
        1070 : Seis Números Impares
        1071 : Suma de Números Consecutivos Impares I
        1072 : Intervalo 2
        1073 : Cuadrado de un Par
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
    