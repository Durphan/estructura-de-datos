import math

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    LINE_SPACE = '\n'

actividad = int(input("¿Qué actividad quieres Ver (Del 1 al 14)"))
match actividad:
    case 1:
        print(f"{bcolors.OKGREEN}Escribir un procedimiento que muestre por pantalla hola mundo{bcolors.ENDC}")
        def hola_mundo():
            print("Hola Mundo")
        hola_mundo()
    case 2:
        print(f"{bcolors.OKGREEN}Escribir un procedimiento que se le pase como argumento la cadena nombre y lo salude {bcolors.ENDC}")
        def saludar(nombre):
            print(f"Hola {nombre}")
        nombre = input(f"¿Cuál es tu nombre? {bcolors.LINE_SPACE}")
        saludar(nombre)
    case 3:
        print(f"{bcolors.OKGREEN}Escribir una funcion que calcule y retorne el factorial de un numero entero positivo{bcolors.ENDC}")
        def factorial(n: int):
            total = 1
            for i in range(n,1,-1):
                total *=i
            return total
        def factorialRecursivo(n: int) -> int:
            if n == 1:
                return 1
            print(n)
            return n*factorialRecursivo(n-1)
        numero = int(input(f"Escriba un numero entero positivo {bcolors.LINE_SPACE}"))
        print(f"Este es el factorial recursivo {factorialRecursivo(numero)}")
    case 4:
        print(f"{bcolors.OKGREEN}Escribir una función que calcule el total de una factura tras aplicarle el IVA{bcolors.ENDC}")
        def totalFactura(montoTotal: float, porcentajeIva: float):
            return(montoTotal * (porcentajeIva/100)) + montoTotal
        porcentajeIva = input(f"Ingrese un porcentaje de IVA {bcolors.LINE_SPACE}")
        if porcentajeIva == "":
            porcentajeIva = 21
        montoTotal = float(input(f"Ingrese el monto total de la factura {bcolors.LINE_SPACE}"))
        print(f"El monto total con IVA es igual a {totalFactura(montoTotal, float(porcentajeIva))}")
    case 5:
        print(f"{bcolors.OKGREEN}Escribir una función que calcule el area de un circulo y otra el volumen de un cilindro invocando la funcion anterior {bcolors.ENDC}")
        def areaCirculo(radio: float):
            return math.pi * (radio**2)
        def volumenCilindro(radio: float, altura: float):
            return areaCirculo(radio) * altura
        radio = float(input("Ingrese el radio del cilindro"))
        altura = float(input("Ingrese la altura del cilindro"))
        print(f"El area del circulo es {areaCirculo(radio)}")
        print(f"El volumen del cilindro es {volumenCilindro(radio, altura)}")
    case 6:
        print(f"{bcolors.OKGREEN}Escribir una función que reciba de argumentos tres numeros positivos, calcule el promedio y diga si el alumno aprobo o no{bcolors.ENDC}")
        def promedio(n1: float, n2: float, n3: float):
            return (n1 + n2 + n3) / 3
        n1 = float(input("Ingrese la primera nota"))
        n2 = float(input("Ingrese la segunda nota"))
        n3 = float(input("Ingrese la tercera nota"))
        prom = promedio(n1, n2, n3)
        print(f"El promedio es {prom}")
        if prom >= 7:
            print("El alumno aprobo")
        else:
            print(f"{bcolors.FAIL}El alumno no aprobo{bcolors.ENDC}")
    case 7:
        print(f"{bcolors.OKGREEN}Escribir una función que reciba de argumentos dos numeros enteros mayores a 1 y retorna n potencia de m{bcolors.ENDC}")
        def potencia(n: int, m: int):
            return n**m
        n = int(input("Ingrese un numero entero mayor a 1"))
        m = int(input("Ingrese otro numero entero mayor a 1"))
        print(f"La potencia de {n} elevado a {m} es igual a {potencia(n, m)}")
    case 8:
        print(f"{bcolors.OKGREEN}Escribir una función que reciba de argumentos dos numeros enteros y retorne el maximo y luego pedir 10 numeros y mostrar el maximo{bcolors.ENDC}")
        def maximo(n1: int, n2: int):   
            if n1 < n2:
                return n1
            return n2
        numeros = []
        while(len(numeros) < 10): # Forma 1 (Lista dinamica) 0(n log n) menos eficiente para el proposito del ejercicio, almacena numeros cuando no necesita (forma fea)
            numeros.append(int(input("Seleccione un numero al azar")))
            numeros.sort(reverse=True)
        print(f"El mayor de los numeros con lista es {numeros.__getitem__(0)}")
        numeroMayor = 0
        for i in range(11): # Forma 2 Bucle for 0(n), no almacena numeros adicionales, mas eficiente
            numero = input("Seleccione un numero")
            if numero == "":
                numero = 0
            numeroMayor = maximo(numeroMayor, int(numero))
        print(f"El numero mayor con for es {numeroMayor}")
    case 9:
        print(f"{bcolors.OKGREEN}Escribir una función que reciba de argumentos una hora, un minuto y un segundo y retorne el tiempo total en segundos{bcolors.ENDC}")
        def tiempoEnSegundos(hora: int, minuto: int, segundo: int):
            return (hora * 3600) + (minuto * 60) + segundo
        hora = int(input("Ingrese la hora"))
        minuto = int(input("Ingrese el minuto"))
        segundo = int(input("Ingrese el segundo"))
        print(f"El tiempo total en segundos es {tiempoEnSegundos(hora, minuto, segundo)}")
    case 10:
        print(f"{bcolors.OKGREEN}Escribir una función que reciba de argumento un año y retorne si es bisiesto o no{bcolors.ENDC}")
        def esBisiesto(anio: int):
            return anio % 4 == 0 and (anio % 100 != 0 or anio % 400 == 0)
        anio = int(input("Ingrese un año"))
        if esBisiesto(anio):
            print(f"{bcolors.OKGREEN}El año {anio} es bisiesto{bcolors.ENDC}")
        else:
            print(f"{bcolors.FAIL}El año {anio} no es bisiesto{bcolors.ENDC}")
    case 11:
        print(f"{bcolors.OKGREEN}Escribir una función que reciba de argumento dos años y retorne la cantidad de años bisiestos entre ellos{bcolors.ENDC}")
        def esBisiesto(anio: int):
            return anio % 4 == 0 and (anio % 100 != 0 or anio % 400 == 0)
        def cantidadBisiestos(anio1: int, anio2: int):
            cantidad = 0
            if anio1 > anio2:
                for i in range(anio2, anio1 + 1):
                    if esBisiesto(i):
                        cantidad += 1
            else:
                for i in range(anio1, anio2 + 1):
                    if esBisiesto(i):
                        cantidad += 1
            return cantidad
        anio1 = int(input("Ingrese un año"))
        anio2 = int(input("Ingrese otro año"))
        print(f"La cantidad de años bisiestos entre {anio1} y {anio2} es {cantidadBisiestos(anio1, anio2)}")
    case 12:
        print(f"{bcolors.OKGREEN}Escribir una función que reciba de argumento un numero entero y retorne la suma de sus digitos{bcolors.ENDC}")
        def digitosSumados(numero:int):
            suma = 0
            while numero != 0:
                suma += int(numero%10)
                numero = int(numero/10)
            return suma
        numero = int(input("Ingrese un numero"))
        print (f"La suma de los digitos es {digitosSumados(numero)}")
    case 13:
        print(f"{bcolors.OKGREEN}Escribir un programa que pida numeros positivos a un usuario y mostrar el numero cuya suma de digitos fue mayor y otro cuya suma de digitos fue menor a 10 {bcolors.ENDC}")
        def digitosSumados(numero:int) -> int:
            suma = 0
            while numero > 0:
                suma += int(numero%10)
                numero = int(numero/10)
            return suma
        numeros = []
        while len(numeros) < 4:
            numero = input("Ingrese un numero")
            if numero == "":
                numero = 0
            numeros.append(int(numero))
            print(numeros)
        contadorMenores = 0
        maximoNumero = 0
        maximoContador = 0
        for i in numeros:
            if max(maximoContador, digitosSumados(i)) == digitosSumados(i):
                maximoContador = digitosSumados(i)
                maximoNumero = i
            if digitosSumados(i) < 10:
                contadorMenores += 1
        print(f"El maximo es {maximoNumero}")
        print(f"La cantidad de numeros cuya suma de digitos fue menor a 10 es {contadorMenores}")
    case 14:
        print(f"{bcolors.OKGREEN}Escribir un programa que pida al usuario sucesivamente numeros hasta que ingrese un numero no primo y luego mostrar el del mayor primo ingresado{bcolors.ENDC}")
        def esPrimo(numero:int) -> bool:
            for i in range(numero-1, 1, -1):
                if numero % i == 0:
                    return False
            return True
        def factorial(numero:int) -> int:
            if numero == 1:
                return 1
            else:
                return numero*factorial(numero-1)
        primoMayor = 0
        numero = input("Ingrese un numero")
        print(numero)
        print(esPrimo(int(numero)))
        while esPrimo(int(numero)):
            primoMayor = max(primoMayor, int(numero))
            numero = input("Ingrese un numero")
        if primoMayor == 0:
            print("No se ingresaron numeros primos")
        else:
            print(f"El mayor primo es {primoMayor}")
            print(f"El factorial del mayor primo es {factorial(primoMayor)}")   