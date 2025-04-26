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