


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
    elif opcion == 1045:
        # Ejercicio 1045
        lados = input("Ingrese los lados del triangulo [A B C] \n").split(" ")
        lado1 = float(lados[0])
        lado2 = float(lados[1])
        lado3 = float(lados[2])
        lista = [lado1, lado2, lado3]
        lista.sort(reverse=True)
        A = lista[0]
        B = lista[1]
        C = lista[2]

        if A >= (B+C):
            print("NAO FORMA TRIANGULO")
        elif A**2 == (B**2+C**2):
            print("TRIANGULO RETANGULO")
        elif A**2 > (B**2+C**2):
            print("TRIANGULO OBTUSANGULO")
        elif A**2 < (B**2+C**2):
            print("TRIANGULO ACUTANGULO")
            
        if A == B == C:
            print("TRIANGULO EQUILATERO")
        elif A == B or B == C:
            print("TRIANGULO ISOSCELES")
    elif opcion == 1046:
        # Ejercicio 1046
        tiempo = input("Ingrese tiempo del comienzo 'A' y el tiempo del final del juego 'B': [A B] \n").split(" ")
        a = int(tiempo[0])
        b = int(tiempo[1])

        if a < b:
            print(f"O JOGO DUROU {b-a} HORA(S)")
        else:
            print(f"O JOGO DUROU {b+24-a} HORA(S)")
    elif opcion == 1047:
        # Ejercicio 1047
        tiempo = input("Ingrese datos del juego: [hora inicial, minuto inicial, hora final, minuto final] \n").split(" ")
        a = int(tiempo[0])
        b = int(tiempo[1])
        c = int(tiempo[2])
        d = int(tiempo[3])

        inicio = a * 60 + b
        fin = c * 60 + d
        diferencia = fin - inicio

        if diferencia <= 0:
            diferencia = diferencia + 24 * 60

        hora = diferencia // 60
        minutos = diferencia % 60

        print(f"O JOGO DUROU {hora} HORA(S) E {minutos} MINUTO(S)")
    elif opcion == 1048:
        salario = float(input("Ingrese salario \n"))

        if salario <= 400:
            porcentaje = 15
        elif salario <= 800:
            porcentaje = 12
        elif salario <= 1200:
            porcentaje = 10
        elif salario <= 2000:
            porcentaje = 7
        else:
            porcentaje = 4

        aumento = salario * porcentaje / 100
        nuevo = salario + aumento

        print(f'Novo salario: {nuevo:.2f}\nReajuste ganho: {aumento:.2f}\nEm percentual: {porcentaje} %')
    elif opcion == 1049:
        # Ejercicio 1049
        a = input("Ingrese clase 1 de animal en base a la tabla: \n")
        b = input("Ingrese clase 2 de animal en base a la tabla: \n")
        c = input("Ingrese clase 3 de animal en base a la tabla: \n")

        if a == 'vertebrado':
            if b == 'ave':
                if c == 'carnivoro':
                    print("aguia")
                else:
                    print("pomba")
            else:
                if c == 'onivoro':
                    print("homem")
                else:
                    print("vaca")
        else:
            if b == 'inseto':
                if c == 'hematofago':
                    print("pulga")
                else:
                    print("lagarta")
            else:
                if c == 'hematofago':
                    print("sanguessuga")
                else:
                    print("minhoca")
    elif opcion == 1050:
        # Ejercicio 1050
        codigo = int(input("Ingrese codigo de área para marcación telefónica: \n"))
        diccionario = {61:'Brasilia',71:'Salvador',11:'Sao Paulo',21:'Rio de Janeiro',32:'Juiz de Fora',19:'Campinas',27:'Vitoria',31:'Belo Horizonte'}

        if codigo in diccionario:
            print(diccionario[codigo])
        else:
            print("DDD nao cadastrado")
    elif opcion == 1051:
        # Ejercicio 1051
        salario = float(input("Ingrese salario: \n")) - 2000

        if salario <= 0:
            print("Isento")
        elif salario <= 1000:
            impuesto = salario * 0.08
            print(f"R$ {impuesto:.2f}")
        elif salario <= 2500:
            impuesto = 1000 * 0.08 + (salario - 1000) * 0.18
            print(f"R$ {impuesto:.2f}")
        else:
            impuesto = 1000 * 0.08 + 1500 * 0.18 + (salario - 2500) * 0.28
            print(f"R$ {impuesto:.2f}")
    elif opcion == 1052:
        # Ejercicio 1052
        numero = int(input("Ingrese número del mes a imprimir: \n"))
        diccionario = {1:'January',2:'February',3:'March',4:'April',5:'May',6:'June',7:'July',8:'August',9:'September',10:'October',11:'November',12:'December'}
        print(diccionario[numero])
    elif opcion == 1059:
        # Ejercicio 1059
        print("Los números pares entre 1 y 100 son:")
        for numero in range(2,101,2):
            print(numero)
    elif opcion == 1060:
        # Ejercicio 1060
        contador = 0
        for i in range(6):
            numeros = float(input("Ingrese número: \n"))
            if numeros > 0:
                contador += 1
        print(f"{contador} valores positivos")
    elif opcion == 1061:
        # Ejercicio 1061
        dia_1 = int(input("Ingrese dia del inicio del evento: (Escribir 'Dia' antes del numero separado por espacio : [Dia n]) \n").split()[1])
        tiempo_1 = input("Ingrese hora,minuto,segundo del inicio del evento [h : m : s] \n").split(" : ")
        h1 = int(tiempo_1[0])
        m1 = int(tiempo_1[1])
        s1 = int(tiempo_1[2])

        dia_2 = int(input("Ingrese dia del fin del evento: (Escribir 'Dia' antes del numero separado por espacio : [Dia n]) \n").split()[1])
        tiempo_2 = input("Ingrese hora,minuto,segundo del fin del evento [h : m : s] \n").split(" : ")
        h2 = int(tiempo_2[0])
        m2 = int(tiempo_2[1])
        s2 = int(tiempo_2[2])

        d = dia_2 - dia_1
        h = h2 - h1
        m = m2 - m1
        s = s2 - s1

        if s < 0:
            s = s + 60
            m = m -1
        if m < 0:
            m = m + 60
            h = h -1
        if h < 0:
            h = h + 24
            d = d - 1
        print(f"{d} dia(s)\n{h} hora(s)\n{m} minuto(s)\n{s} segundo(s)")
    elif opcion == 1064:
        # Ejercicio 1064
        contador = 0
        suma = 0
        for i in range(6):
            numeros = float(input("Ingrese número: \n"))
            if numeros > 0:
                contador += 1
                suma += numeros
        promedio = suma / contador
        print(f"{contador} valores positivos\n{promedio:.1f}")
    elif opcion == 1065:
        # Ejercicio 1065
        contador = 0
        for i in range(5):
            numeros = int(input("Ingrese número: \n"))
            if numeros % 2 == 0:
                contador += 1

        print(f"{contador} valores pares")
    elif opcion == 1066:
        # Ejercicio 1066
        contador_1 = 0
        contador_2 = 0
        contador_3 = 0
        contador_4 = 0
        for i in range(5):
            numeros = int(input("Ingrese número: \n"))
            if numeros % 2 == 0:
                contador_1 += 1
            else:
                contador_2 += 1
            if numeros > 0:
                contador_3 += 1
            elif numeros < 0:
                contador_4 += 1

        print(f"{contador_1} valor(es) par(es)")
        print(f"{contador_2} valor(es) impar(es)")
        print(f"{contador_3} valor(es) positivo(s)")
        print(f"{contador_4} valor(es) negativo(s)")
    elif opcion == 1067:
        # Ejercicio 1067
        valor = int(input("Ingrese el limite hasta donde quiere que se impirma los numeros impares del 1 a X\n"))
        for numero in range(1,valor+1,2):
            print(numero)
    elif opcion == 1070:
        # Ejercicio 1070
        valor = int(input("Ingrese número desde donde que empiece a imprimir los números impares: \n"))
        lista = []

        while True:
            if valor % 2 == 1:
                print(valor)
                lista.append(valor)
                if len(lista) == 6:
                    break
            valor += 1
    elif opcion == 1071:
        # Ejercicio 1071
        X = int(input("Ingrese el valor mayor desde donde inicie la sumatoria: \n"))
        Y = int(input("Ingrese el valor menor hasta donde termine la sumatoria: \n"))
        suma = 0
        for i in range(X-1,Y,-1):
            if i % 2 == 1:
                suma += i
                
        print(suma)
    elif opcion == 1072:
        # Ejercicio 1072
        dentro = 0
        fuera = 0
        for i in range(int(input("Ingrese el número de valores que serán leídos: \n"))):
            numero = int(input("Ingrese número \n"))
            if numero >= 10 and numero <= 20:
                dentro += 1
            else:
                fuera += 1

        print(f"{dentro} in")
        print(f"{fuera} out")
    elif opcion == 1073:
        # Ejercicio 1073
        numero = int(input("Ingrese el valor hasta donde quiere calcular el cuadrado de los números pares: \n"))
        for i in range(1,numero+1):
            if i % 2 == 0:
                print(f"{i}^2 = {i**2}")
    else:
        print("La opcion seleccionada no existe")
    