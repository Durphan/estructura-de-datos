import numpy as np

actividad = int(input("Seleccione una actividad"))

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


match actividad:
    case 1:
        print(f"{bcolors.OKGREEN}Implementar una función que calcule el factorial de un número de forma recursiva {bcolors.ENDC}")
        def factorial(n: int) -> int:
            if n == 1:
                return 1
            return n*factorial(n-1)
        numero = int(input("Seleccione un numero para obtener el factorial"))
        print(f"{bcolors.OKCYAN}el factorial de {numero} es {factorial(numero)}{bcolors.ENDC}")
    case 2:
        print(f"{bcolors.OKGREEN}Una canilla de una casa pierde agua de forma que todos los días pierde 2 gotas más que el día anterior. Escribir una función recursiva que calcule cuantas gotas perderá la canilla el día N. El primer día solo perdía dos gotas.{bcolors.ENDC}")
        def gotasPerdidas(n:int) -> int:
            if n == 1:
                return 2
            return n*2+gotasPerdidas(n-1)
        numero = int(input("Escriba la cantidad de dias"))
        print(f"{bcolors.OKCYAN}La cantidad de gotas perdidas en {numero} dias es {gotasPerdidas(numero)}{bcolors.ENDC}")
    case 3:
        print(f"{bcolors.OKGREEN} Implementar una función recursiva que calcule los números de la serie de Fibonacci{bcolors.ENDC}")
        def fibonacci(n:int) -> int:
            if n == 0:
                return 0
            if n == 1:
                return 1
            print(f"{n-1} - {n}")
            return fibonacci(n-1) + fibonacci(n-2)
        numero = int(input("Escriba un numero"))
        print(f"El fibonacci de {numero} es {fibonacci(numero)}")
    case 4:
        print(f"{bcolors.OKGREEN}Escribir una función recursiva que calcule el número triangular de índice N. El número triangular de índice N es la suma de todos los números{bcolors.ENDC}")
        def numeroTriangular(n:int) -> int:
            if n == 1:
                return n
            return n + numeroTriangular(n-1)
        numero = int(input("Escriba un numero"))
        print(f"El numero triangular de {numero} es {numeroTriangular(numero)}")
    case 5:
        print(f"{bcolors.OKGREEN}En las redes sociales se produce una continua interacción y cada vez que un usuario realiza una acción, la comunidad se modifica, Durante los primeros 20 posteos, siempre suma una cantidad fija de 1000 (mil) seguidores en cada uno, A partir del posteo 21, la cantidad de seguidores duplica la cantidad previa de seguidores, mas 500 seguidores extra. {bcolors.ENDC}")
        def cantidadSeguidoresTotalConPosteos(posteos:int):
            if posteos == 0:
                return 1000
            if posteos <= 20:
                return 1000 + cantidadSeguidoresTotalConPosteos(posteos-1)
            return 500 + cantidadSeguidoresTotalConPosteos(posteos-1) * 2
        numero = int(input("Ingrese el numero de seguridores"))
        print(f"La cantidad de seguidores que tendra el influencer con {numero} posteos sera de {cantidadSeguidoresTotalConPosteos(numero)}")
    case 6:
        print(f"{bcolors.OKGREEN} mplementar una función que permita saber la cantidad de baldosas que se colocan en total luego de transcurrida una determinada cantidad de días.{bcolors.ENDC}")
        def cantidadBaldosas(dias:int) -> int:
            if dias <= 0:
                raise ValueError("La cantidad de dias no puede ser menor o igual a 0")
            if dias == 1:
                return 100
            if dias % 2 == 1:
                return cantidadBaldosas(dias-1) + cantidadBaldosas(dias-2)
            return cantidadBaldosas(dias-1)*2
        dias = int(input("Ingrese la cantidad de dias"))
        print(f"La cantidad de baldosas que se colocan en {dias} dias es {cantidadBaldosas(dias)}")
    case 7:
        print(f"{bcolors.OKGREEN}Escriba una función recursiva que calcule la cantidad de algas en el tanque en un día N.{bcolors.ENDC}")
        def cantidadAlgas(dias:int) -> int:
            if dias <= 0:
                raise ValueError("La cantidad de dias no puede ser menor o igual a 0")
            if dias == 1:
                return 12
            if dias > 1 and dias < 12:
                return cantidadAlgas(dias-1) + 15
            return cantidadAlgas(dias-1) * 3 + 100
        dias = int(input("Ingrese la cantidad de dias"))
        print(f"La cantidad de algas en el tanque en {dias} dias es {cantidadAlgas(dias)}")
    case 8:
        print(f"{bcolors.OKGREEN}Escribir una función recursiva que calcule la potencia N de un número M {bcolors.ENDC}")
        def potencia(base:int, exponente:int) -> int:
            if exponente == 0:
                return 1
            return base * potencia(base, exponente-1)
        base = int(input("Ingrese la base"))
        exponente = int(input("Ingrese el exponente"))
        print(f"La potencia de {base} elevado a {exponente} es {potencia(base, exponente)}")
    case 9:
        print(f"{bcolors.OKGREEN}Escribir una funcion recursiva que cumpla con la leyenda del trigo{bcolors.ENDC}")
        def leyendaDelTrigo(casilla:int) -> int:
            if casilla == 1:
                return 1
            return 2 * leyendaDelTrigo(casilla-1)
        casillas = int(input("Ingrese la cantidad de casillas"))
        print(f"La cantidad de trigo en la casilla {casillas} es {leyendaDelTrigo(casillas)}")
    case 10:
        print(f"{bcolors.OKGREEN} Escribir una función recursiva que calcule la cantidad de cucarachas en un edificio en función de la cantidad de pisos.{bcolors.ENDC}")
        def cantidadCucarachas(pisos:int) -> int:
            if pisos == 1:
                return 2
            if pisos % 2 == 0:
                return 2*pisos
            return cantidadCucarachas(pisos-1) + cantidadCucarachas(pisos-2)
    case 11:
        print(f"{bcolors.OKGREEN}Escribir la función recursiva repetirPalabra, que recibe como parámetro una palabra (cadena de caracteres) y un número N. La función debe retornar una nueva cadena que contenga la palabra repetida N veces{bcolors.ENDC}")
        def repetirPalabra(palabra:str, cantidad:int) -> str:
            if cantidad == 1:
                return palabra
            return palabra + " " + repetirPalabra(palabra, cantidad-1)
        palabra = input("Ingrese la palabra")
        cantidad = int(input("Ingrese la cantidad de veces que quiere repetir la palabra"))
        print(f"La palabra {palabra} repetida {cantidad} veces es {repetirPalabra(palabra, cantidad)}")
    case 12:
        print(f"{bcolors.OKGREEN} Calcular recursivamente los sueldos de Juan y de María luego de transcurridos una cantidad determinada de meses.{bcolors.ENDC}")
        def calcularSueldo(sueldo:int, meses:int, actualizacion:int) -> int:
            if meses == 1:
                return sueldo
            return calcularSueldo(sueldo, meses-1, actualizacion) + (sueldo * actualizacion / 100)
        sueldo = int(input("Ingrese el sueldo"))
        meses = int(input("Ingrese la cantidad de meses"))
        actualizacion = int(input("Ingrese la cantidad de actualizacion"))
        print(f"El sueldo luego de {meses} meses es {calcularSueldo(sueldo, meses, actualizacion)}")
        def cantidadDeMesesParaSuperarSueldo(sueldo:int, sueldoObjetivo:int, actualizacion:int) -> int:
            if sueldo >= sueldoObjetivo:
                return 0
            return 1 + cantidadDeMesesParaSuperarSueldo(sueldo + (sueldo * actualizacion / 100), sueldoObjetivo, actualizacion)
        sueldo = int(input("Ingrese el sueldo"))
        sueldoObjetivo = int(input("Ingrese el sueldo objetivo"))
        actualizacion = int(input("Ingrese la cantidad de actualizacion"))
        print(f"La cantidad de meses para superar el sueldo objetivo es {cantidadDeMesesParaSuperarSueldo(sueldo, sueldoObjetivo, actualizacion)}")
    case 13:
        print(f"{bcolors.OKGREEN} Escribir una función recursiva que reciba un vector como parámetro y retorne la suma de todos sus elementos.{bcolors.ENDC}")
        def sumaVector(vector:np.asarray) -> int:
            if len(vector) == 1:
                return vector[0]
            return vector[len(vector)-1] + sumaVector(vector[:len(vector)-1])
        vector = np.array([1,2,3,4,5])
        print(f"El vector es {vector}")
        print(f"La suma de los elementos del vector es {sumaVector(vector)}")
    case 14:
        print(f"{bcolors.OKGREEN} Escribir una función recursiva que retorna True si un string es un palindromo y False en caso contrario.{bcolors.ENDC}")
        def esPalindromo(palabra:str) -> bool:
                if len(palabra) <= 1:
                    return True
                if palabra[0] != palabra[-1]:
                    return False
                return esPalindromo(palabra[1:-1:])
        palabra = input("Escriba una palabra")
        print(esPalindromo(palabra))
    case 15:
        print(f"{bcolors.OKGREEN} Escribir una función que implemente de forma recursiva el algoritmo de búsqueda binaria sobre un vector.{bcolors.ENDC}")
        def hayElemento(vector:np.ndarray, elemento:any, max:int, min:int) -> bool:
            centro: int = (max+min)//2
            if max < min:
                return False
            if vector[centro] == elemento:
                return True
            if elemento < vector[centro]:
                return hayElemento(vector, elemento, centro-1, min)
            return hayElemento(vector, elemento, max, centro+1)
        vector = np.array([1,2,3,4,5,6,7,8,9])
        print(f"El vector es {vector}")
        elemento = int(input("Ingrese el elemento a buscar"))
        if hayElemento(vector, elemento, len(vector)-1, 0):
            print(f"El elemento {elemento} se encuentra en el vector")
        else:
            print(f"El elemento {elemento} no se encuentra en el vector")
    case 16:
        print(f"{bcolors.OKGREEN} Escribir una función que implemente de forma recursiva el algoritmo de ordenamiento por inserción.{bcolors.ENDC}")
        def ordenamientoPorInsercion(vector:np.ndarray, n:int) -> np.ndarray:
            if n <= 1:
                return vector
            for i in range(n-1):
                if vector[i] > vector[i+1]:
                    vector[i], vector[i+1] = vector[i+1], vector[i]
            return ordenamientoPorInsercion(vector, n-1)
        vector = np.array([5,4,3,2,1])
        print(f"El vector es {vector}")
        print(f"El vector ordenado es {ordenamientoPorInsercion(vector, len(vector))}")