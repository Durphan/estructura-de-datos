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
    
    def clear(self):
         self.items = []
    
    

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
                colaAux = self._cola.clone()
                self._cola.clear()
                if self._cola.is_empty():
                    self._cola.push(ventaNueva)
                while not colaAux.is_empty() and ventaNueva.horario().horas() >= colaAux.first().horario().horas() and ventaNueva.horario().minutos() >= colaAux.first().horario().minutos() and ventaNueva.horario().segundos() >= colaAux.first().horario().segundos():
                    self._cola.push(colaAux.pop())
                self._cola.push(ventaNueva)
                while not colaAux.is_empty():
                    self._cola.push(colaAux.pop())
                    
                
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
                           
    case 3:
        print(f"{bcolors.OKGREEN} Implementar la función recursiva `inversionRecursiva` que recibe por parámetro un string y retorna un nuevo string conteniendo el string de entrada invertido. {bcolors.ENDC}")
        def inversionRecursiva(string:str, stringInverso:list) -> str:
            if len(string) == 0:
                return "".join(stringInverso)
            stringInverso.append(string[len(string)-1])
            
            return inversionRecursiva(string[:len(string)-1], stringInverso)
        
        
        string = "Hola Mundo"
        print(f"{bcolors.OKCYAN}El string original es {string}{bcolors.ENDC}")
        print(f"{bcolors.OKCYAN}El string invertido es {inversionRecursiva(string, [])}{bcolors.ENDC}")
    
    case 4:
        print(f"{bcolors.OKGREEN} Crear el TDA `Receta`, que contiene una arreglo con los ingredientes de una receta.{bcolors.ENDC}")
        
        class Ingrediente:
            def __init__(self, nombre:str, cantidad:int, calorias:int):
                self._nombre = nombre
                self._cantidad = cantidad
                self._calorias = calorias
                
            def cantidad(self):
                return self._cantidad
            
            def calorias(self):
                return self._calorias
            
            def nombre(self):
                return self._nombre
            
            def __str__(self):
                return f"El ingrediente tiene de nombre {self._nombre}, de cantidad {self._cantidad} y de calorias {self._calorias}"
        
        class Receta:
            def __init__(self, tipoReceta:str, ingredientes:np.asarray = None):
                self._tipo_receta=tipoReceta
                self._ingredientes = ingredientes
                if self._ingredientes is None:
                    self._ingredientes = np.empty(20, dtype=Ingrediente)
                else:
                    if len(self._ingredientes) > 20:
                        raise ValueError("No deben de ser mas de 20 ingredientes")
                if self._tipo_receta not in ["omnivora", "vegetariana", "vegana"]:
                    raise ValueError("No se permiten recetas que no sean omnivoras, vegetarianas o veganas")
                
            def cantidad_ingredientes(self) -> int:
                cantidadIngredientes = 0
                for ingrediente in self._ingredientes:
                    if ingrediente != None:
                        cantidadIngredientes += ingrediente.cantidad()
                return cantidadIngredientes
            
            def registrar_ingrediente(self, ingredienteARegistrar:Ingrediente) -> None:
                if len(self._ingredientes) > 20:
                    raise ValueError("No se puede agregar mas de 20 ingredientes")
                for nroIngrediente in range(len(self._ingredientes)):
                    if self._ingredientes[nroIngrediente] == None:
                        self._ingredientes[nroIngrediente] = ingredienteARegistrar
                        break
            
            def total_calorias(self) -> int:
                caloriasTotales = 0
                for ingrediente in self._ingredientes:
                    if ingrediente != None:
                        caloriasTotales += ingrediente.calorias()
                return caloriasTotales
            
            def ingrediente_mas_calorico(self) -> Ingrediente:
                posicion = 0
                for nroIngrediente in range(len(self._ingredientes)):
                    if self._ingredientes[nroIngrediente] != None and self._ingredientes[nroIngrediente].calorias() > self._ingredientes[posicion].calorias():
                        posicion = nroIngrediente
                return self._ingredientes[posicion]
            
            def __str__(self) -> str:
                return f"Esta receta es de tipo {self._tipo_receta} y tiene los siguientes ingredientes: {self._ingredientes}"
            
            def ingredientes(self) -> np.asarray:
                return self._ingredientes

        
            
            
        receta = Receta("omnivora")
        ingrediente1 = Ingrediente("carne", 2, 500)
        ingrediente2 = Ingrediente("verdura", 1, 100)
        ingrediente3 = Ingrediente("fruta", 1, 200)
        receta.registrar_ingrediente(ingrediente1)
        receta.registrar_ingrediente(ingrediente2)
        receta.registrar_ingrediente(ingrediente3)
        print(f"{bcolors.OKCYAN}La receta es de tipo {receta._tipo_receta} y tiene los siguientes ingredientes: {bcolors.ENDC}")
        for ingrediente in receta.ingredientes():
            if ingrediente != None:
                print(f"{bcolors.OKCYAN}{ingrediente.__str__()}{bcolors.ENDC}")
        print(f"{bcolors.OKCYAN}La receta tiene un total de {receta.cantidad_ingredientes()} ingredientes{bcolors.ENDC}")
        print(f"{bcolors.OKCYAN}La receta tiene un total de {receta.total_calorias()} calorias{bcolors.ENDC}")
        print(f"{bcolors.OKCYAN}El ingrediente mas calorico es {receta.ingrediente_mas_calorico().__str__()}{bcolors.ENDC}")
            
    case 5:
        print(f"{bcolors.OKGREEN} Escribir la función recursiva `sonIguales` que recibe dos strings del mismo tamaño (no vacías) y retorna True si son iguales y False en caso contrario.{bcolors.ENDC}")
        def sonIguales(str1:str, str2:str) -> bool:
            if len(str1) != len(str2):
                raise ValueError("Los strings no son del mismo tamaño")
            if len(str1) == 0:
                return True
            if str1[0] != str2[0]:
                return False
            return sonIguales(str1[1:], str2[1:])
        
        
        str1 = "Hola Mundose"
        str2 = "Hola Mundoas"
        print(f"{bcolors.OKCYAN}El string 1 es {str1} y el string 2 es {str2}{bcolors.ENDC}")
        print(f"{bcolors.OKCYAN}Los strings son iguales: {sonIguales(str1, str2)}{bcolors.ENDC}")
        str4 = "asdasdasdasfasd"
        str5 = "asdasdasdasfast"
        print(f"{bcolors.OKCYAN}El string 1 es {str4} y el string 2 es {str5}{bcolors.ENDC}")
        print(f"{bcolors.OKCYAN}Los strings son iguales: {sonIguales(str4, str5)}{bcolors.ENDC}")
            
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
        
    case 7:
        print(f"{bcolors.OKGREEN}  implementar un algoritmo recursivo que cuente la cantidad de números pares y otro algoritmo recursivo para contar la cantidad de números mayores que 10 en un arreglo de números enteros. {bcolors.ENDC}")
        def cantidadNumerosPares(arreglo:np.asarray) -> int: # Prueba
            
            def contar(i:int, cantidad:int) -> int:
                if i == len(arreglo):
                    return cantidad
                if arreglo[i] % 2 == 0:
                    return contar(i+1, cantidad+1)
                return contar(i+1, cantidad)
            
            return contar(0, 0)
        
        def cantidadNumerosMayoresA10(arreglo:np.asarray) -> int:
            
            def contar(i:int, cantidad:int) -> int:
                if i == len(arreglo):
                    return cantidad
                if arreglo[i] > 10:
                    return contar(i+1, cantidad+1)
                return contar(i+1, cantidad)
            
            return contar(0, 0)
        
        def masParesQue10(arreglo:np.asarray) -> bool:
            return cantidadNumerosPares(arreglo) > cantidadNumerosMayoresA10(arreglo)
        
        arreglo = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11])
        print(f"{bcolors.OKCYAN}El arreglo es {arreglo}{bcolors.ENDC}")
        print(f"{bcolors.OKCYAN}La cantidad de numeros pares es {cantidadNumerosPares(arreglo)}{bcolors.ENDC}")
        print(f"{bcolors.OKCYAN}La cantidad de numeros mayores a 10 es {cantidadNumerosMayoresA10(arreglo)}{bcolors.ENDC}")
        print(f"{bcolors.OKCYAN}El arreglo tiene mas numeros pares que mayores a 10: {masParesQue10(arreglo)}{bcolors.ENDC}")
        
    case 8:
        print(f"{bcolors.OKGREEN} Implementar el TDA EstacionamientoUnaHur {bcolors.ENDC}")
        class Auto:
            def __init__(self, patente:int, horario:int) -> None:
                self._patente = patente
                self._horario = horario
            
            def horario(self) -> int:
                return self._horario
            
            def patente(self) -> int:
                return self._patente
            
            def __repr__(self) -> str:
                return "Auto"
            
        class EstacionamientoUnahur:
            def __init__(self,filas:int) -> None:
                self._estacionamiento = np.empty((filas,filas), dtype=Auto)
            
            def estacionar(self, patente:int, horaIngreso:int) -> list[int]:
                nuevoAuto = Auto(patente, horaIngreso)
                for i in range(len(self._estacionamiento)):
                    for j in range(len(self._estacionamiento[i])):
                        if type(self._estacionamiento[i,j]) is Auto:
                            continue
                        self._estacionamiento[i,j] = nuevoAuto
                        return [i,j]
                raise ValueError("No hay plazas disponibles")
            
            def salir(self, patente:int) -> int:
                for i in range(len(self._estacionamiento)):
                    for j in range(len(self._estacionamiento[i])):
                        if type(self._estacionamiento[i,j]) is Auto and self._estacionamiento[i,j].patente() == patente:
                            horarioEntrada = self._estacionamiento[i,j].horario()
                            self._estacionamiento[i,j] = None
                            return horarioEntrada
                return 0
            
            def esta_vacio(self) -> bool:
                for fila in self._estacionamiento:
                    for plaza in fila:
                        if type(plaza) is Auto:
                            return False
                return True
            
            def cantidad_autos__hora(self,hora:int) -> int:
                cantidad = 0
                for fila in self._estacionamiento:
                    for plaza in fila:
                        if type(plaza) is Auto and plaza.horario() == hora:
                            cantidad +=1
                return cantidad
            
            def __repr__(self):
                return str(self._estacionamiento)
        estacionamiento = EstacionamientoUnahur(5)
        print(f"{bcolors.OKCYAN}El estacionamiento tiene las siguientes plazas {estacionamiento.__repr__()}{bcolors.ENDC}")
        print(f"{bcolors.OKCYAN}El estacionamiento esta vacio: {estacionamiento.esta_vacio()}{bcolors.ENDC}")
        print(f"{bcolors.OKCYAN}El auto con patente 1234 fue estacionado en la plaza {estacionamiento.estacionar(1234, 10)}{bcolors.ENDC}")
        print(f"{bcolors.OKCYAN}El estacionamiento tiene las siguientes plazas {estacionamiento.__repr__()}{bcolors.ENDC}")
        print(f"{bcolors.OKCYAN}la cantidad de autos en la hora 10 es {estacionamiento.cantidad_autos__hora(10)}{bcolors.ENDC}")
        print(f"{bcolors.OKCYAN}El estacionamiento esta vacio: {estacionamiento.esta_vacio()}{bcolors.ENDC}")
        print(f"{bcolors.OKCYAN}El auto que salio con patente 1234, entro a las {estacionamiento.salir(1234)}{bcolors.ENDC}")
        print(f"{bcolors.OKCYAN}El estacionamiento tiene las siguientes plazas {estacionamiento.__repr__()}{bcolors.ENDC}")
                                    
            

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

    
