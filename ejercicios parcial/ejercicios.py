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

class Cola:
    def __init__(self, listaInicial = None):
        self.items = listaInicial
        if self.items is None:
            self.items = []

    def push(self, item):
        self.items.insert(0, item)
        print("Se agrega el elemento ", item, " a la cola")

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError("La cola está vacía")
        
    def first(self):
        if not self.is_empty():
            return self.items[len(self.items) - 1]
        else:
            raise IndexError("La cola está vacía")
        
    def is_empty(self):
        return len(self.items) == 0
    
    def size(self):
        return len(self.items)
    
    def clone(self):
        new_queue = Cola()
        new_queue.items = self.items.copy()
        return new_queue
    
    

match actividad:
    case 1:
        print(f"{bcolors.OKGREEN} Escribir la función recursiva posicionCima(arreglo), que retorna la posición de la cima de un arreglo. {bcolors.ENDC}")
        def posicionCima(arreglo:np.asarray, posicion:int, posicionActual:int) -> int:
            if posicionActual == len(arreglo):
                return posicion
            if arreglo[posicionActual] > arreglo[posicion]:
                return posicionCima(arreglo, posicionActual, posicionActual+1)
            return posicionCima(arreglo, posicion, posicionActual+1)
        arreglo = np.array([1, 2, 3, 4, 5])
        print(f"{bcolors.OKCYAN}El arreglo es {arreglo}{bcolors.ENDC}")
        print(f"{bcolors.OKBLUE}La posicion de la cima es {posicionCima(arreglo, 0, 0)}{bcolors.ENDC}")
    case 2:
        print(f"{bcolors.OKGREEN} crear el TDA CajaDeSupermercado {bcolors.ENDC}")
        
        class Horario:
            def __init__(self, horas, minutos, segundos):
                if horas > 21:
                    raise ValueError("No se pueden realizar compras luego de las 21 horas")
                self._horas = horas
                self._minutos = minutos
                self._segundos = segundos
            
            def __str__(self):
                return str(self._horas) + ":" + str(self._minutos) + ":" + str(self._segundos)
            
            def horas(self):
                return self._horas

            def minutos(self):
                return self._minutos
            
            def segundos(self):
                return self._segundos
            
            def equals(self, horario2):
                return horario2.horas() == self._horas and horario2.minutos() == self._minutos and horario2.segundos() == self._segundos
        
        class Venta:
            def __init__(self, horario:Horario, monto:float):
                self._horario = horario
                self._monto = monto
            
            def monto(self):
                return self._monto
            
            def horario(self):
                return self._horario
        
        
        class CajaDeSupermercado:
            def __init__(self, cajero:str, numero:int, colaCompras:Cola = None) -> None:
                self._cola = colaCompras
                if self._cola is None:
                    self._cola = Cola()
                self._cajero = cajero
                self._numero = numero
                
            def __str__(self) -> str:
                return "Esta caja tiene de numero " + str(self._numero) + " el nombre del cajero es " + self._cajero
            
            def agregar_venta(self, monto:float, horario:Horario) -> None:
                ventaNueva = Venta(horario, monto)
                self._cola.push(ventaNueva)
            
            def cantidad_de_ventas_grandes(self, montoMinimo:float) -> int:
                colaAux = self._cola.clone()
                cantidadMontoMinimo = 0
                while not colaAux.is_empty():
                    if colaAux.first().monto() > montoMinimo:
                        cantidadMontoMinimo +=1
                    colaAux.pop()
                return cantidadMontoMinimo

            def ultimas_n_ventas(self,n:int) -> float:
                colaAux = self._cola.clone()
                monto = 0
                while colaAux.size() != n:
                    colaAux.pop()
                while not colaAux.is_empty():
                    monto += colaAux.first().monto()
                    colaAux.pop()
                return monto
            
            def vaciar_historial(self) -> int:
                ventasEliminadas = 0
                while not self._cola.is_empty:
                    ventasEliminadas -= 1
                    self._cola.pop()
                return ventasEliminadas
            
            def monto_ventas_horario(self, horario:Horario) -> float:
                colaAux = self._cola.clone()
                monto = 0
                while not colaAux.is_empty():
                    if colaAux.first().horario().equals(horario):
                        monto += colaAux.first().monto()
                    colaAux.pop()
                return monto
        caja = CajaDeSupermercado("Juan", 1)
        caja.agregar_venta(100, Horario(20, 30, 0))
        caja.agregar_venta(200, Horario(20, 30, 0))
        caja.agregar_venta(300, Horario(20, 30, 0))
        caja.agregar_venta(400, Horario(20, 30, 0))
        print(f"{bcolors.OKCYAN}La informacion de la caja es {caja.__str__()}{bcolors.ENDC}")
        print(f"{bcolors.OKCYAN}La cantidad de ventas grandes es {caja.cantidad_de_ventas_grandes(200)}{bcolors.ENDC}")
        print(f"{bcolors.OKCYAN}El monto de las ultimas 2 ventas es {caja.ultimas_n_ventas(2)}{bcolors.ENDC}")
        Horario1 = Horario(20, 30, 0)
        Horario2 = Horario(20, 30, 0)
        print(f"{bcolors.OKCYAN}El horario 1 es {Horario1} y el horario 2 es {Horario2}{bcolors.ENDC}")
        print(f"{bcolors.OKCYAN}El horario 1 es igual al horario 2: {Horario1.equals(Horario2)}{bcolors.ENDC}")
        print(f"{bcolors.OKCYAN}El monto de las ventas en el horario 20:30:00 es {caja.monto_ventas_horario(Horario(20, 30, 0))}{bcolors.ENDC}")
                           
        
                
            
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

    
