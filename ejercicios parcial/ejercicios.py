import numpy as np

actividad = int(input("Seleccione la actividad que desea revisar"))


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

class Pila:
        def __init__(self, listaInicial=None):
            if listaInicial is not None:
                self.items = listaInicial
            else:
                self.items = []

        def is_empty(self):
         return len(self.items) == 0

        def push(self, item):
         self.items.append(item)

        def pop(self):
         return self.items.pop()

        def peek(self):
         return self.items[-1]

        def size(self):
         return len(self.items)

        def clear(self):
         self.items = []

        def clone(self):
         new_stack = Pila()
         new_stack.items = self.items.copy()
         return new_stack

        def __repr__(self):
         return str(self.items)

match actividad:
    case 6:
        print(f"{bcolors.OKGREEN} El Correo Argentino nos pidió ayuda para organizar los paquetes de cada sucursal. Todos los días llegan paquetes con diferente peso que son apilados para luego ser distribuidos{bcolors.ENDC}")
        class Paquete:
            def __init__(self, peso:int, contenido:str) -> None:
                self._peso = peso
                self._contenido = contenido
       
            
            def peso(self) -> int:
               return self._peso
            
            def contenido(self) -> str:
               return self._contenido
        
            def __str__(self) -> str:
                return f"El paquete tiene de peso {self._peso} y de contenido {self._contenido}"
        class ElCorreoNoCierra:
            def __init__(self, paquetes:Pila = None) -> None:
               self.paquetes = paquetes
               if self.paquetes is None:
                    self.paquetes = Pila()
            
            def pila_paquetes(self) -> Pila:
               pilaAux:Pila = self.paquetes.clone()
               return pilaAux
            
            def agregar_paquete(self, contenido:str, peso:int):
                nuevoPaquete = Paquete(peso, contenido)
                pilaAux = Pila()
                if self.paquetes.is_empty():
                    self.paquetes.push(nuevoPaquete)
                else:
                    while not self.paquetes.is_empty() and self.paquetes.peek().peso() < nuevoPaquete.peso():
                        pilaAux.push(self.paquetes.pop())
                    self.paquetes.push(nuevoPaquete)
                    while not pilaAux.is_empty():
                        self.paquetes.push(pilaAux.pop())

            def juntar_correos(self, correoB) -> None:
               pilaClon = correoB.pila_paquetes()
               while not pilaClon.is_empty():
                  self.agregar_paquete(pilaClon.peek().contenido(), pilaClon.peek().peso())
                  pilaClon.pop()
                  
            def __str__(self) -> str:
                pilaClon = self.paquetes.clone()
                while not pilaClon.is_empty():
                    print(f"{bcolors.OKCYAN}{pilaClon.peek().__str__()}{bcolors.ENDC}")
                    pilaClon.pop()
                return "Fin de la lista de paquetes"

            
        paquete = Paquete(5, "carta")
        correoA= ElCorreoNoCierra()
        correoA.agregar_paquete("carta", 5)
        correoA.agregar_paquete("carta", 3)
        correoA.agregar_paquete("carta", 7)
        correoA.agregar_paquete("carta", 1)
        print(f"{bcolors.OKCYAN}El correo A tiene los siguientes paquetes: {correoA.__str__()} {bcolors.ENDC}")
        correoB= ElCorreoNoCierra()
        correoB.agregar_paquete("carta", 2)
        correoB.agregar_paquete("carta", 4)
        correoB.agregar_paquete("carta", 6)
        correoB.agregar_paquete("carta", 8)
        print(f"{bcolors.OKCYAN}El correo B tiene los siguientes paquetes: {correoB.__str__()} {bcolors.ENDC}")
        correoA.juntar_correos(correoB)
        print(f"{bcolors.OKCYAN}El correo A tiene los siguientes paquetes: {correoA.__str__()} {bcolors.ENDC}")
        
        
        
               
    case 9:
        print(f"{bcolors.OKGREEN} Escribir la función recursiva estaIncluido(arreglo1, arreglo2), que retorna verdadero si el arreglo1 está incluido al inicio o al final del arreglo2.{bcolors.ENDC}")
        def estaIncluido(a:np.asarray, b:np.asarray) -> bool:
            if len(b) == 0 or len(a) == 0:
                return True
            if a[0] != b[0] and a[-1] != b[-1]:
                return False
            return (a[0] == b[0] or a[-1] == b[-1]) and estaIncluido(a[1:len(a)-1], b[1:len(b)-1])
        arr1 = [2, 5, 1] 
        arr2 = [1, 9, 3, 4, 2, 5, 1]
        print(f"{bcolors.OKCYAN}El arreglo 1 es {arr1} y el arreglo 2 es {arr2}{bcolors.ENDC}")
        print(f"{bcolors.OKBLUE}El arreglo 1 está incluido en el arreglo 2: {estaIncluido(arr1,arr2)}{bcolors.ENDC}")
        print(f"{bcolors.OKBLUE}El arreglo 2 está incluido en el arreglo 1: {estaIncluido(arr2,arr1)}{bcolors.ENDC}")
        arr3 = [2, 5, 1, 6, 1, 8, 5]
        arr4 = [4, 3, 2, 5, 1, 8, 2]
        print(f"{bcolors.OKCYAN}El arreglo 1 es {arr1} y el arreglo 3 es {arr3}{bcolors.ENDC}")
        print(f"{bcolors.OKCYAN}El arreglo 1 esta incluido en el arreglo 3: {estaIncluido(arr1,arr3)}{bcolors.ENDC}")
        print(f"{bcolors.OKCYAN}El arreglo 3 esta incluido en el arreglo 1: {estaIncluido(arr3,arr1)}{bcolors.ENDC}")

    
