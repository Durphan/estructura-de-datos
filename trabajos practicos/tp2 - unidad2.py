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
        vector = np.empty(longitudVector, int)
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
            nuevoVector = np.empty(len(vector), str)
            for i in range(len(vector)):
                nuevoVector[i] = vector[len(vector) - i -1]
            return nuevoVector
        vectorPrueba = np.array(["h", "o", "l", "a"])
        print(f"{bcolors.HEADER}Se crea vector {vectorPrueba}{bcolors.ENDC}")
        print(f"La funcion devuelve {vectorStringInverso(vectorPrueba)}")
    case 3:
        print(f"{bcolors.OKGREEN}Escribir la función sumaDeVectores que recibe dos vectores de enteros del mismo tamaño y retorna otro con la suma de ambos. La suma de vectores se realiza componente a componente.{bcolors.ENDC}")
        def vectorSumado(vectorA: np.int_, vectorB: np.int_) -> np.int_:
            if len(vectorA) != len(vectorB):
                print(f"{bcolors.FAIL} Ambos vectores deben tener la misma longitud{bcolors.ENDC}")
                return np.empty(1, int)
            nuevoVector = np.empty(len(vectorA), int)
            for i in range(len(vectorA)):
                print(i)
                nuevoVector[i] = vectorA[i] + vectorB[i]
            return nuevoVector
        vectorA = np.array([1,2,3,4])
        vectorB = np.array([1,2,3,4])
        print(f"Se crea el vectorA con los elementos {vectorA} y vector B con los elementos {vectorB}")
        print(f"La funcion devuelve {vectorSumado(vectorA, vectorB)}")
    case 4:
        print(f"{bcolors.OKGREEN}Escribir una función que recibe un vector y desplaza todos sus elementos una posición hacia la derecha.{bcolors.ENDC}")
        def desplazarADerecha(vector):
            nuevoVector = np.copy(vector)
            for i in range(0, len(vector)):
                if i == len(vector)-1:
                    nuevoVector[0] = vector[i]
                    continue
                nuevoVector[i+1] = vector[i]
            return nuevoVector
        vector = np.array([1,2,3,4])
        print(f"{bcolors.HEADER}Se crea vector {vector}{bcolors.ENDC}")
        print(f"La funcion devuelve {desplazarADerecha(vector)}")
    case 5:
        print(f"{bcolors.OKGREEN} Desarrollar una función que inserte un elemento en una posición en un vector. Al insertar el elemento, se debe producir un desplazamiento a la derecha de todos los elementos en las posiciones siguientes, el último elemento se pierde. {bcolors.ENDC}")
        def agregarElementoAPosicion(vector, elemento, posicion):
            nuevoVector = np.copy(vector)
            nuevoVector[posicion] = elemento
            for i in range(posicion, len(vector)):
                if i == len(vector)-1:
                    continue
                nuevoVector[i+1] = vector[i]
            return nuevoVector
        vector = np.array([1,2,3,4])
        print(f"{bcolors.HEADER}Se crea vector {vector}{bcolors.ENDC}")
        print(f"Si se quiere agregar un 5 en la posicion 1 entonces la funcion devuelve {agregarElementoAPosicion(vector, 5, 1)}")
    case 6:
        print(f"{bcolors.OKGREEN}Escribir una función que elimine el elemento que ocupa una determinada posición de un vector. Al eliminar, los elementos a la derecha del eliminado, deben desplazarse a la izquierda un lugar y agregar un cero en la última posición.{bcolors.ENDC}")
        def eliminarPosicion(vector, posicion):
            nuevoVector = np.copy(vector)
            for i in range(posicion, len(vector)):
                if i == len(vector)-1:
                    nuevoVector[i] = 0
                    continue
                nuevoVector[i] = vector[i+1]
            return nuevoVector
        vector = np.array([1,2,3,4])
        print(f"{bcolors.HEADER}Se crea vector {vector}{bcolors.ENDC}")
        print(f"Si quiero eliminar la posicion 1 entonces daria {eliminarPosicion(vector, 1)}")
    case 7:
        print(f"{bcolors.OKGREEN}Escribir una función que elimine todas las apariciones de un determinado elemento de un vector. Al eliminar se deben insertar tantos ceros al final como elementos se eliminaron.{bcolors.ENDC}")
        def eliminarElemento(vector, elemento):
            nuevoVector = np.copy(vector)
            for i in range(len(vector)):
                while nuevoVector[i] == elemento:
                    for j in range(i, len(vector)):
                        if j == len(vector)-1:
                            nuevoVector[j] = 0
                            continue
                        nuevoVector[j] = nuevoVector[j+1] # A mejorar
            return nuevoVector
        vector = np.array([1,2,5,4,5,5])
        print(f"{bcolors.HEADER}Se crea vector {vector}{bcolors.ENDC}")
        print(f"Si quiero eliminar el 5 entonces daria {eliminarElemento(vector, 5)}")
    case 8:
        print(f"{bcolors.OKGREEN} Escribir un procedimiento que recibe un vector y retorna subvectores{bcolors.ENDC}")
        def subvectores(vector):
            print(vector[0:2:1])
            print(vector[0:3:1])
            print(vector[2:5:1])
            print(vector[0::2])
        vector = np.array([2,1,4,5,2,7,9])
        print(f"{bcolors.HEADER}Se crea vector {vector}{bcolors.ENDC}")
        subvectores(vector)
    case 9:
        print(f"{bcolors.OKGREEN} Escribir una función que recibe las dimensiones y retorna una matriz rellena de la siguiente forma: En la posición ( n , m ) debe contener n + m. {bcolors.ENDC}")
        def rellenarMatriz(x, y):
            matriz = np.zeros([x,y], int)
            for i in range(len(matriz)):
                for j in range(len(matriz[i])):
                    print(matriz[j], " j")
                    matriz[i,j] = i+j
            print(matriz)
        rellenarMatriz(5,5)
    case 10:
        print(f"{bcolors.OKGREEN}Escribir una función que recibe una matriz cuadrada (N x N) y calcula la suma de los elementos que están por encima de la diagonal principal{bcolors.ENDC}")
        def sumaDiagonalDerecha(matriz):
            total = 0
            for i in range(len(matriz)):
                total += matriz[i, i+1:].sum()
            return total
        matriz = np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12], [1,2,3,4]])
        print(f"Se define matriz {bcolors.LINE_SPACE} {matriz}")
        print(f"La suma de los diagonales es {sumaDiagonalDerecha(matriz)}")
    case 11:
        print(f"{bcolors.OKGREEN} Escribir una función que retorna True si una matriz cuadrada es matriz diagonal y False en caso contrario")
        def esDiagonal(matriz):
            matrizAComparar = np.zeros([len(matriz), len(matriz[0:len(matriz):1])], int)
            for i in range(1, len(matriz)-1):
                matrizAComparar[i,i] = matriz[i,i]
            return (matriz == matrizAComparar).all()
        matriz = np.array([[0, 0, 0, 0],[0, 2, 0, 0],[0, 0, 4, 0],[0, 0, 0, 0]])
        print(f"Se define matriz {bcolors.LINE_SPACE} {matriz}")
        print(f"El resultado en este caso de la funcion es {esDiagonal(matriz)}")
    case 12:
        print(f"{bcolors.OKGREEN} Escribir una función que retorna True si una matriz cuadrada de enteros es simétrica y False en caso contrario.")
        def esSimetrica(matriz) -> bool:
            for i in range(len(matriz)):
                for j in range(i+1, len(matriz[i])):
                    if matriz[i,j] != matriz[j,i]:
                        return False
            return True
        matriz = np.array([[1, 2, 3],[2, 4, 5],[3, 5, 6]])
        print(f"Se define matriz {bcolors.LINE_SPACE} {matriz}")
        print(esSimetrica(matriz))