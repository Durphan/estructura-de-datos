import numpy as np

ejercicio = int(input("Seleccione el ejercicio a realizar"))

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
    LINE_SPACE = '\n\n'

match ejercicio:
    case 1:
        print(f"{bcolors.OKGREEN}Escribir una función que recibe un numero entero N y le pide al usuario que ingrese N numeros. Al final, el programa debe retornar un vector contiendo los números que fueron ingresados. Tambien debe imprimir por pantalla la suma total de los valores y el promedio. Se deben hacer funciones para resolver el promedio y la suma total.{bcolors.ENDC}")
        longitudVector = int(input(f"{bcolors.OKBLUE}Coloque el numero de longitud que debe tener el arreglo{bcolors.ENDC}"))
        vector = np.zeros((longitudVector))
        for i in range(0, len(vector)):
            vector[i] = int(input("Coloque un numero que quiera que tenga el vector"))
        print(f"El vector construido es {vector}")
        def sumaAElementosVector(vector: np.int_) -> int:
            total = 0
            for i in vector:
                total += int(i)
            return total
        print(f"La suma de todos los numeros de los vectores es {sumaAElementosVector(vector)}")
        print(f"El promedio del vector es {sumaAElementosVector(vector) / len(vector)}")
    case 2:
        print(f"{bcolors.OKGREEN}Escribir una función que recibe un vector de strings y retorna otro con los mismos elementos del vector de entrada pero en orden inverso.{bcolors.ENDC}")
        def vectorStringInverso(vector: np.str_) -> np.str_:
            nuevoVector = np.copy(vector)
            posicionAReemplazar = 0
            for i in range(len(vector)-1, -1, -1):
                nuevoVector[posicionAReemplazar] = vector[i]
                posicionAReemplazar +=1
            return nuevoVector
        vectorPrueba = np.array(["h", "o", "l", "a"])
        print(f"{bcolors.HEADER}Se crea vector {vectorPrueba}{bcolors.ENDC}")
        print(f"La funcion devuelve {vectorStringInverso(vectorPrueba)}")
    case 3:
        print(f"{bcolors.OKGREEN}Escribir la función sumaDeVectores que recibe dos vectores de enteros del mismo tamaño y retorna otro con la suma de ambos. La suma de vectores se realiza componente a componente.{bcolors.ENDC}")
        def vectorSumado(vectorA: np.int_, vectorB: np.int_) -> np.int_:
            if len(vectorA) != len(vectorB):
                print(f"{bcolors.FAIL} Ambos vectores deben tener la misma longitud{bcolors.ENDC}")
            nuevoVector = np.copy(vectorA)
            posicionAReemplazar = 0
            for i in range(0, len(vectorA)):
                nuevoVector[posicionAReemplazar] = vectorA[i] + vectorB[i]
                posicionAReemplazar += 1
            return nuevoVector
        vectorA = np.array([1,2,3,4])
        vectorB = np.array([1,2,3,4])
        print(f"Se crea el vectorA con los elementos {vectorA} y vector B con los elementos {vectorB}")
        print(f"La funcion devuelve {vectorSumado(vectorA, vectorB)}")
