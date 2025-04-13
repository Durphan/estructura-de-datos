
import random

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

ejercicio = int(input("Selecciona el numero de ejercicio que quieres ver (del 1 al 32)"))

match ejercicio:
    case 1:
        print(f"{bcolors.OKGREEN}Consigna: Escribir un programa que imprima 'Hola Mundo'{bcolors.ENDC}")
        print("Hola mundo")
    case 2:
        print("Consigna: Escribir un programa que declare una variable saludo y le asigne el valor 'Hola Mundo'. Luego, imprimir el valor de la variable saludo.")
        saludo = "hola mundo"
        print(f"Se acaba de llamar a la variable saludo: {saludo}")
    case 3:
        print(f"{bcolors.OKGREEN}Consigna: Asignar dos variables con valores randomicos entre 0 y 10. Luego, imprimir el resultado de la suma, resta, multiplicación y el resto de la división.{bcolors.ENDC}")
        a = int(random.random() * 10)
        b = int(random.random() * 10)
        print(f"{bcolors.OKCYAN}El primer numero es: {a}{bcolors.ENDC}")
        print(f"{bcolors.OKCYAN}El segundo numero es: {b}{bcolors.ENDC}")
        print(f"El resultado de la suma es: {a+b}")
        print(f"El resultado de la resta es: {a-b}")
        print(f"El resultado de la multiplicacion es: {a*b}")
        try:
            print(f"El resultado de la division es: {a/b}")
            print(f"El resto de la division es: {a%b}")
        except ZeroDivisionError:
            print(f"{bcolors.FAIL}No se puede dividir por cero{bcolors.ENDC}")
    case 4:
        print("{bcolors.OKGREEN} Consigna: Escribir un programa que permita calcular el area de un triangulo y el de un circulo{bcolors.ENDC}")
        eleccion = int(input("Selecciona 1 si quieres saber el perimetro y area de un triangulo dado su base y alture, 2 si de un circulo dado su radio"))
        def calcularAreaTriangulo(base, altura):
            return (base * altura) / 2
        def calcularPerimetroTriangulo(base, altura):
            return base + altura + ((base**2 + altura**2)**0.5)
        def calcularAreaCirculo(radio):
            return 3.14 * (radio**2)
        def calcularPerimetroCirculo(radio):
            return 2 * 3.14 * radio
        match eleccion:
            case 1:
                base = int(input("Ingrese la base del triangulo"))
                altura = int(input("Ingrese la altura del triangulo"))
                print(f"El area del triangulo es: {calcularAreaTriangulo(base, altura)}")
                print(f"El perimetro del triangulo es: {calcularPerimetroTriangulo(base, altura)}")
            case 2:
                radio = int(input("Ingrese el radio del circulo"))
                print(f"El area del circulo es: {calcularAreaCirculo(radio)}")
                print(f"El perimetro del circulo es: {calcularPerimetroCirculo(radio)}")
    case 5:
        print(f"{bcolors.OKGREEN}Consigna: Escribir un programa que convierta grados celsius a fahrenheit{bcolors.ENDC}")
        celsius = int(input("Ingrese la temperatura en grados celsius"))
        fahrenheit = (celsius * 9/5) + 32
        print(f"La temperatura en grados fahrenheit es: {fahrenheit}")
    case 6:
        print(f"{bcolors.OKGREEN}Consigna: Escribir un programa que muestre el numero de horas trabajadas y el costo por hora {bcolors.ENDC}")
        def sueldoPorHora(horasTrabajadas: int, costoPorHora: int):
            return horasTrabajadas * costoPorHora
        horasTrabajadas = int(input("Ingrese el numero de horas trabajadas"))
        costoPorHora = int(input("Ingrese el costo por hora"))
        sueldo = sueldoPorHora(horasTrabajadas, costoPorHora)
        print(f"El sueldo es: {sueldo}")
    case 7:
        print(f"{bcolors.OKGREEN}Consigna: Escribir un programa que de el IMC{bcolors.ENDC}")
        def numeroIMC(peso: int, altura: int):
            return peso / (centimetrosAMetros(altura)**2)
        def centimetrosAMetros(altura: int):
            return altura / 100
        peso = int(input("Ingrese su peso en kg"))
        altura = int(input("Ingrese su altura en metros"))
        print(f"{bcolors.OKCYAN}Su IMC es: {numeroIMC(peso, altura)}{bcolors.ENDC}")
    case 8:
        print(f"{bcolors.OKGREEN} Escribir un programa que pregunte una cantidad a invertir, el interés anual y el número de años, y muestre por pantalla el capital obtenido en la inversión.{bcolors.ENDC}")
        def numeroDeIntereses(cantidadInvertir: int, interesAnual: float, numeroDeAnios: int):
            return cantidadInvertir * (1 + interesAnual) ** numeroDeAnios
        cantidadInvertir = int(input("Ingrese la cantidad a invertir"))
        interesAnual = float(input("Ingrese el interes anual"))
        numeroDeAnios = int(input("Ingrese el numero de anios"))
        print(f"{bcolors.OKCYAN}El capital obtenido es: {numeroDeIntereses(cantidadInvertir, interesAnual, numeroDeAnios)}{bcolors.ENDC}")
    case 9:
        print(f"{bcolors.OKGREEN}Escribir un programa que pregunte un nombre completo en la consola y después muestre por pantalla ese nombre tres veces, una con todas las letras minúsculas, otra con todas las letras mayúsculas y otra solo con la primera letra del nombre y de los apellidos en mayúscula. {bcolors.ENDC}")
        nombre = input("ingrese su nombre completo")
        print(f"El nombre en minusculas es: {nombre.lower()}")
        print(f"El nombre en mayusculas es: {nombre.upper()}")
        print(f"El nombre capitalizado es: {nombre.title()}")
    case 10:
        print(f"{bcolors.OKGREEN}Escribir un programa que pregunte un nombre en la consola y después muestre por pantalla la cantidad de letras que tiene ${bcolors.ENDC}")
        nombre = input("ingrese su nombre")
        print(f"El nombre tiene {len(nombre)} letras")
    case 11:
        print(f"{bcolors.OKGREEN} Escribir un programa que pida una palabra, reemplace todas las letras `a` por `z` y muestre el resultado por pantalla.{bcolors.ENDC}")
        palabra = input("Ingrese una palabra")
        palabra = palabra.replace("a", "z")
        print(f"La nueva palabra es: {palabra}")
    case 12:
        print(f"{bcolors.OKGREEN}Escribir un programa que pida dos palabras y muestre por pantalla su concatenacion.{bcolors.ENDC}")
        palabra1 = input("Ingrese la primera palabra")
        palabra2 = input("Ingrese la segunda palabra")
        print(f"La nueva palabra es: {palabra1 + palabra2}")
    case 13:
        print(f"{bcolors.OKGREEN}Escribir un programa que pida una palabra, un numero n y muestre por pantalla la palabra n veces.{bcolors.ENDC}")
        palabra = input("Ingrese una palabra")
        n = int(input("Ingrese un numero "))
        for i in range(n):
            print(f"{bcolors.OKCYAN}{palabra}{bcolors.ENDC}")
    case 14:
        print(f"{bcolors.OKGREEN}Escribir un programa que pida una edad y muestre en pantalla si es mayor de edad o no.{bcolors.ENDC}")
        def esMayorDeEdad(edad: int):
            return edad >= 18
        edad = int(input("Ingrese su edad"))
        if esMayorDeEdad(edad):
            print(f"{bcolors.OKCYAN}Es mayor de edad{bcolors.ENDC}")
        else:
            print(f"{bcolors.FAIL}No es mayor de edad{bcolors.ENDC}")
    case 15:
        print(f"{bcolors.OKGREEN} Escribir un programa que almacene la cadena de caracteres `contraseña` en una variable y luego pregunte por la contraseña e imprima por pantalla si la contraseña introducida en la consola coincide con la guardada {bcolors.ENDC}")
        contraseniaFalsa = "contraseña"
        contrasenia = input("Escribe una contraseña")
        if(contrasenia.lower() == contraseniaFalsa):
            print("La contraseña es correcta")
    case 16:
        print(f"{bcolors.OKGREEN}Escribir un programa que pida un numero entero y muestre por pantalla si es par o impar.{bcolors.ENDC}")
        numero = int(input("Ingrese un numero "))
        if numero % 2 == 0:
            print(f"{bcolors.OKCYAN}El numero es par{bcolors.ENDC}")
        else:
            print(f"{bcolors.FAIL}El numero es impar{bcolors.ENDC}")
    case 17:
        print(f"{bcolors.OKGREEN}Escribir un programa que diga si una persona debe pagar un impuesto si es mayor de edad y sus ingresos mensuales son iguales o mayores a 100000.{bcolors.ENDC}")
        def debePagarImpuesto(edad: int, ingresos: int):
            return edad >= 18 and ingresos >= 100000
        edad = int(input("Ingrese su edad"))
        ingresos = int(input("Ingrese sus ingresos mensuales"))
        if debePagarImpuesto(edad, ingresos):
            print(f"{bcolors.OKCYAN}Debe pagar impuesto{bcolors.ENDC}")
        else:
            print(f"{bcolors.FAIL}No debe pagar impuesto{bcolors.ENDC}")
    case 18:
        print(f"{bcolors.OKGREEN}Escribir un programa que pida un numero entero entre 1 y 7 y muestre por pantalla el dia de la semana correspondiente.{bcolors.ENDC}")
        diasDeSemana = ["lunes", "martes", "miercoles", "jueves", "viernes", "sabado", "domingo"]
        numero = int(input("Ingrese un numero entre 1 y 7"))
        if numero >= 1 and numero <= 7:
            print(f"{bcolors.OKCYAN}El dia de la semana es: {diasDeSemana[numero-1]}{bcolors.ENDC}")
        else:
            print(f"{bcolors.FAIL}El numero no es valido{bcolors.ENDC}")
    case 19:
        print(f"{bcolors.OKGREEN}Escribir un programa que indique a que grupo pertenece un alumno de acuerdo al genero y nombre, siendo que el grupo A esta formado por mujeres con una inicial anterior a la M y los hombres con un inicial posterior a la N y el grupo B el resto.{bcolors.ENDC}")
        def esGrupoA(nombre: str, genero:str):
            return (nombre.lower()[0] < "m" and genero.lower() == "femenino") or (nombre.lower()[0] > "n" and genero.lower() == "masculino")
        nombre = input("Ingrese el nombre del alumno")
        genero = input("Ingrese si el genero es masculino o femenino")
        if esGrupoA(nombre, genero):
            print("Es grupo A")
        else: print("Es grupo B")
    case 20:
        print(f"{bcolors.OKGREEN} definir el precio de entrada de un cliente segun su edad {bcolors.ENDC}")
        def precioDeEntradaParaEdad(edad: int):
            if edad < 4:
                return 0
            elif edad > 4 and edad < 18:
                return 5
            return 10
        edad = int(input("Escriba la edad del cliente"))
        print(f"El cliente debe de pagar {precioDeEntradaParaEdad(edad)} euros")
    case 21:
        print(f"{bcolors.OKGREEN} Escribir un programa que imprima por pantalla todos los numeros entre 1 y 100 con un bucle while y luego con un bucle for.{bcolors.ENDC}")
        print("Con while")
        i = 1
        while i <= 100:
            print(i)
            i += 1
        print("Con for")
        for i in range(1, 101):
            print(i)
    case 22:
        print(f"{bcolors.OKGREEN}Escribir un programa que pida dos numeros enteros y muestre por pantalla todos los numeros entre ellos.{bcolors.ENDC}")
        numero1 = int(input("Ingrese el primer numero"))
        numero2 = int(input("Ingrese el segundo numero"))
        if numero1 < numero2:
            for i in range(numero1+1, numero2):
                print(i)
        else:
            for i in range(numero2+1, numero1):
                print(i)
    case 23:
        print(f"{bcolors.OKGREEN}Escribir un programa pregunte un nombre y un numero entero y muestre por pantalla el nombre tantas veces como el numero introducido.{bcolors.ENDC}")
        nombre = input("Ingrese su nombre")
        numero = int(input("Ingrese un numero"))
        for i in range(numero):
            print(nombre)
    case 24:
        print(f"{bcolors.OKGREEN}Escribir un programa que pida un numero entero y muestre por pantalla todos los numeros impares desde 1 hasta el numero introducido.{bcolors.ENDC}")
        numero = int(input("Introduzca un numero entero positivo"))
        for i in range(1, numero):
            if i%2 == 0:
                print(i)
    case 25:
        print(f"{bcolors.OKGREEN}Escribir un programa que pida un numero entero y muestre por pantalla un triangulo de altura n con asteriscos.{bcolors.ENDC}")
        numero = int(input("Ingrese un numero entero"))
        asteriscos = ""
        for i in range(numero):
            asteriscos += "*"
            print(asteriscos)
    case 26:
        print(f"{bcolors.OKGREEN}Escribir un programa que imprima todas las fichas de domino posibles.{bcolors.ENDC}")
        for i in range(7):
            for j in range(i, 7):
                print(f"{i} | {j}")
    case 27:
        print(f"{bcolors.OKGREEN}Escribir un programa que pida un numero entero y muestre por pantalla un triangulo rectangulo {bcolors.ENDC}")
        numero = int(input("Ingrese un numero entero"))
        for i in range(1, numero):
            numeros = ""
            for j in range((i*2)):
                if j%2 == 1:
                    numeros += (f"{j}")
            print(numeros)
    case 28:
        print(f"{bcolors.OKGREEN} Escribir un programa que pida un número natural N e imprima por pantalla la suma de los números naturales de 1 hasta N. {bcolors.ENDC}")
        numero = int(input("Ingrese un numero"))
        suma = 0
        for i in range(1, numero+1):
            suma += i
        print(suma)
    case 29:
        print(f"{bcolors.OKGREEN} Construir un programa que lea un número natural N y calcule la suma de los primeros N números pares. {bcolors.ENDC}")
        numero = int(input("Ingrese un numero"))
        contador = 0
        numeroAEvaluar = 1
        suma = 0
        while contador < numero:
            if numeroAEvaluar % 2 == 0:
                print(numeroAEvaluar)
                suma += numeroAEvaluar
                contador += 1
            numeroAEvaluar+=1
        print(f"El resultado es {suma}")
    case 30:
        print(f"{bcolors.OKGREEN} Escribir un programa que pida dos números enteros e informa por pantalla todos los números pares entre ellos. {bcolors.ENDC}")
        numeroA = int(input("Ingrese un numero"))
        numeroB = int(input("Ingrese el segundo numero"))
        if numeroA < numeroB:
            for i in range(numeroA+1, numeroB):
                if i % 2 == 0:
                    print(i)
        else:
            for i in range(numeroB+1, numeroA):
                if i % 2 == 0:
                    print(i)
    case 31:
        print(f"{bcolors.OKGREEN} Escribir un programa que pida un número entero y muestre por pantalla la cantidad de cifras de dicho número. Se debe resolver con divisiones sucesivas por 10 usando un bucle while. ${bcolors.ENDC}")
        numero = int(input("Ingrese un numero"))
        cifras = 1
        while int(numero / 10) > 0:
            numero /= 10
            cifras += 1
        print(f"El numero tiene {cifras} cifras")
    case 32:
        print(f"{bcolors.OKGREEN} Escribir un programa que pida un número entero y muestre por pantalla si es numero primo o compuesto {bcolors.ENDC}")
        numero = int(input("Ingrese un numero"))
        if numero < 2:
            print(f"{bcolors.FAIL}El numero no es primo ni compuesto{bcolors.ENDC}")
        else:
            esPrimo = True
            for i in range(2, int(numero/2)+1):
                if numero % i == 0:
                    esPrimo = False
                    break
            if esPrimo:
                print(f"{bcolors.OKCYAN}El numero es primo{bcolors.ENDC}")
            else:
                print(f"{bcolors.FAIL}El numero es compuesto{bcolors.ENDC}")
    case _:
        print(f"{bcolors.FAIL}No existe el ejercicio {ejercicio}{bcolors.ENDC}")