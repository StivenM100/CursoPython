


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
    elif opcion == 1041:
        # Ejercicio 1041
        punto = input("Ingrese coordenada [X Y] \n").split(" ")
        X = float(punto[0])
        Y = float(punto[1])

        if X == 0 and Y == 0:
            print("Origem")
        elif X == 0 and Y != 0:
            print("Eixo Y")
        elif X != 0 and Y == 0:
            print("Eixo X")
        elif X > 0 and Y > 0:
            print("Q1")
        elif X > 0 and Y < 0:
            print("Q4")
        elif X < 0 and Y > 0:
            print("Q2")
        elif X < 0 and Y < 0:
            print("Q3")
    elif opcion == 1042:
        # Ejercicio 1042
        numeros = input("Ingrese tres numeros enteros [A B C] \n").split(" ")
        A = int(numeros[0])
        B = int(numeros[1])
        C = int(numeros[2])
        lista = [A, B, C]
        lista.sort()
        print(f"{lista[0]}\n{lista[1]}\n{lista[2]}\n")
        print(f"{A}\n{B}\n{C}")
    elif opcion == 1043:
        # Ejercicio 1043
        valores = input("Ingrese valores [A B C] \n").split(" ")
        a = float(valores[0])
        b = float(valores[1])
        c = float(valores[2])

        if a+b>c and b+c>a and c+a>b:
            print(f"Perimetro = {(a+b+c):.1f}")
        else:
            print(f"Area = {(0.5*(a+b)*c):.1f}")
    elif opcion == 1044:
        # Ejercicio 1044
        valores = input("Ingrese valores para conocer si son multiplos o no [A B] \n").split(" ")
        A = int(valores[0])
        B = int(valores[1])

        if A%B == 0 or B%A == 0:
            print("Sao Multiplos")
        else:
            print("Nao sao Multiplos")
    else:
        print("La opcion seleccionada no existe")
    