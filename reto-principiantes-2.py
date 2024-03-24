


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
    elif opcion == 1038:
        # Ejercicio 1038
        valores = input("Ingrese el código X y la cantidad Y del producto 'X Y' \n").split(" ")
        precio = [0,4,4.5,5,2,1.5]
        total = precio[int(valores[0])] * int(valores[1])
        print(f"Total: R$ {total:.2f}")
    elif opcion == 1040:
        # Ejercicio 1040
        notas = input("Ingrese notas: [N1 N2 N3 N4] \n").split(" ")
        N1 = float(notas[0])
        N2 = float(notas[1])
        N3 = float(notas[2])
        N4 = float(notas[3])

        media = (N1*2+N2*3+N3*4+N4*1)/(2+3+4+1)
        print(f"Media: {media:.1f}")

        if media >= 7:
            print("Aluno aprovado.")
        elif media < 5:
            print("Aluno reprovado.")
        elif media >= 5 and media <= 6.9:
            print("Aluno em exame.")
            examen = float(input("Ingrese nota de examen: \n"))
            print(f"Nota do exame: {examen:.1f}")
            nota_final = (media + examen) / 2
            if nota_final >= 5:
                print("Aluno aprovado.")
            elif nota_final <= 4.9:
                print("Aluno reprovado.")
            print(f"Media final: {nota_final:.1f}")
    else:
        print("La opcion seleccionada no existe")
    