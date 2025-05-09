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
                self.peso = peso
                self.contenido = contenido
            
            def __str__(self) -> str:
                return "El paquete tiene de peso " + str(self.peso) + " y de contenido tiene " + {self.contenido}
            
            def peso(self) -> int:
               return self.peso
            
            def contenido(self) -> str:
               return self.contenido
        
        class ElCorreoNoCierra:
            def __init__(self, paquetes:Pila[Paquete]) -> None:
               self.paquetes = paquetes
            
            def pila_paquetes(self) -> Pila:
               pilaAux:Pila = self.paquetes.clone()
               return pilaAux
            
            def agregarPaquete(self, contenido:str, peso:str):
               pilaAux = Pila()
               paquete = Paquete(peso,contenido)
               pilaClon = self.paquetes.clone()
               while not pilaClon.is_empty():
                  if paquete.peso() > pilaClon.peek().peso():
                     pilaAux.push(paquete)
                  pilaAux.push(pilaClon.pop())
               self.paquetes = pilaAux

               if self.paquetes.is_empty():
                  self.paquetes.push(paquete)

            def juntarCorreos(self, correoB) -> None:
               pilaClon = correoB.pila_paquetes()
               while not pilaClon.is_empty():
                  self.agregarPaquete(pilaClon.peek().contenido(), pilaClon.peek().peso())
                  pilaClon.pop()
               
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
        print(estaIncluido(arr1,arr2))
        arr3 = [2, 5, 1, 6, 1, 8, 5]
        arr4 = [4, 3, 2, 5, 1, 8, 2]
        print(estaIncluido(arr1,arr3))
        print(estaIncluido(arr1,arr4))

    
