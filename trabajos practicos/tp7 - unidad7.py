

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

class Nodo:
    def __init__(self, valor: any = None) -> None:
        self.valor = valor
        self.siguiente = None

    def tiene_siguiente(self) -> bool:
        return self.siguiente is not None
    
    def agregar_elemento_ordenado_recusivo(self, elemento:int) -> None:
        if self.siguiente is None:
            self.siguiente = Nodo(elemento)
        if self.siguiente.valor > elemento:
            nodoAux = self.siguiente
            self.siguiente = Nodo(elemento)
            self.siguiente.siguiente = nodoAux
        else:
            self.siguiente.agregar_elemento_ordenado_recusivo(elemento)

    def multiplicacion_de_menor_recursivo(self, elemento1, elemento2):
        if self.valor <= elemento1:
            self.valor = elemento2*self.valor
        if self.tiene_siguiente():
            self.siguiente.multiplicacion_de_menor_recursivo(elemento1, elemento2)
            
    def indices_elemento_recursivo(self, elemento:any, indice:int, listaIndices:list[int]) -> list[int]:
        if self.valor == elemento:
            listaIndices.append(indice)
        if self.tiene_siguiente():
            return self.siguiente.indices_elemento_recursivo(elemento, indice+1, listaIndices)
        return listaIndices
        

class ListaEnlazada:
    def __init__(self) -> None:
        self.primero = None

    def append(self, valor: any) -> Nodo:
        if self.primero is None:
            self.primero = Nodo(valor)
            return self.primero
        nodoAux: Nodo = self.primero
        while nodoAux.tiene_siguiente():
            nodoAux: Nodo = nodoAux.siguiente
        nodoAux.siguiente = Nodo(valor)
        return self.primero

    def vaciar(self) -> None:
        self.primero = None

    def __len__(self) -> int:
        longitud = 0
        nodoAux = self.primero
        while nodoAux.tiene_siguiente():
            nodoAux = nodoAux.siguiente
            longitud += 1
        return longitud

    def insert(self, valor: any, posicion: int) -> Nodo:
        if posicion < 0:
            raise IndexError("No se puede insertar el elemento en una posicion negativa")
        if posicion > len(self):
            raise IndexError("Indice fuera de rango")
        if posicion == 0:
            nodo = Nodo(valor)
            nodo.siguiente = self.primero
            self.primero = nodo
            return self.primero
        indice = 0
        nodoAux = self.primero
        while indice != posicion - 1:
            nodoAux = nodoAux.siguiente
            indice += 1
        nodo = Nodo(valor)
        nodo.siguiente = nodoAux.siguiente
        nodoAux.siguiente = nodo
        return nodoAux.siguiente

    def __repr__(self):
        if self.primero is None:
            return "None"
        string = str(self.primero.valor)
        nodoAux = self.primero
        while nodoAux.tiene_siguiente():
            string += " -> " + str(nodoAux.siguiente.valor)
            nodoAux: Nodo = nodoAux.siguiente
        string += " -> None"
        return string

    def is_empty(self):
        return self.primero is None

    def get(self, posicion: int) -> any:
        if posicion < 0:
            raise IndexError("No se puede recibir el elemento en una posicion negativa")
        if posicion > len(self):
            raise IndexError("Indice fuera de rango")
        posicionActual = 0
        nodoAux = self.primero
        while posicionActual != posicion:
            posicionActual += 1
            nodoAux = nodoAux.siguiente
        return nodoAux.valor

    def pop(self, posicion: int = None) -> Nodo:
        if posicion is None:
            nodoAux = self.primero
            while nodoAux.siguiente.tiene_siguiente():
                nodoAux = nodoAux.siguiente
            nodoBorrado = nodoAux.siguiente
            nodoAux.siguiente = None
            return nodoBorrado
        if posicion < 0:
            raise IndexError("No se puede recibir el elemento en una posicion negativa")
        if posicion > len(self):
            raise IndexError("Indice fuera de rango")
        if posicion == 0:
            nodoAux = self.primero
            if nodoAux.tiene_siguiente():
                self.primero = nodoAux.siguiente
            else:
                self.primero = None
            return nodoAux
        indice = 0
        nodoAux = self.primero
        while indice != posicion - 1:
            indice += 1
            nodoAux = nodoAux.siguiente
        nodoBorrado = nodoAux.siguiente
        if nodoAux.siguiente.tiene_siguiente():
            nodoAux.siguiente = nodoAux.siguiente.siguiente
        else:
            nodoAux.siguiente = None
        return nodoBorrado

    def clone(self):
        copiaLista = ListaEnlazada()
        nodoAux = self.primero
        while nodoAux is not None:
            copiaLista.append(nodoAux.valor)
            nodoAux = nodoAux.siguiente
        return copiaLista

    def __contains__(self, valor: any) -> bool:
        nodoAux = self.primero
        while nodoAux is not None:
            if nodoAux.valor == valor:
                return True
            nodoAux = nodoAux.siguiente
        return False

    def __setitem__(self, posicion: int, valor: any) -> None:
        if posicion < 0:
            raise IndexError("No se puede asignar un valor en una posicion negativa")
        if posicion > len(self):
            raise IndexError("Indice fuera de rango")
        nodoAux = self.primero
        indice = 0
        while indice != posicion:
            nodoAux = nodoAux.siguiente
            indice += 1
        nodoAux.valor = valor

    def __getitem__(self, posicion: int) -> any:
        if posicion < 0:
            raise IndexError("No se puede recibir el elemento en una posicion negativa")
        if posicion > len(self):
            raise IndexError("Indice fuera de rango")
        nodoAux = self.primero
        indice = 0
        while indice != posicion:
            nodoAux = nodoAux.siguiente
            indice += 1
        return nodoAux.valor

    def intercambiar_primeros(self):
        if self.primero is None or not self.primero.tiene_siguiente():
            raise ValueError("No se pueden intercambiar primeros si no hay dos elementos")
        nodoAux = self.primero
        self.primero = self.primero.siguiente
        nodoAux.siguiente = self.primero.siguiente
        self.primero.siguiente = nodoAux
        
    def indices_elemento(self, elemento:any) -> list[int]:
        listaIndices = []
        if self.primero is None:
            return listaIndices
        nodoAux = self.primero
        indice = 0
        while nodoAux is not None:
            if nodoAux.valor == elemento:
                listaIndices.append(indice)
            indice += 1
            nodoAux = nodoAux.siguiente
        return listaIndices
    
    def indices_elemento_recursivo(self, elemento:any) -> list[int] | list[None]:
        if self.primero is None:
            return []
        return self.primero.indices_elemento_recursivo(elemento, 0,[])
        
        
    
    def eliminar_ocurrencias(self, elemento:any) -> None:
        nodoAux = self.primero
        while nodoAux.valor == elemento: # Si los primeros elementos son iguales al elemento a eliminar, los borra
            self.primero = nodoAux.siguiente
            nodoAux = self.primero
        while nodoAux.tiene_siguiente():
            if nodoAux.siguiente.valor == elemento: # Si el siguiente elemento es igual al elemento a eliminar, lo borra
                nodoAux.siguiente = nodoAux.siguiente.siguiente
                continue
            nodoAux = nodoAux.siguiente
    
    def primer_nodo_al_final(self) -> None:
        if self.is_empty():
            raise IndexError("No se puede pasar el primer nodo al final si la lista esta vacia")
        primerNodo = self.pop(0) # Duplica, no mueve
        self.append(primerNodo.valor)
    
    
    def ultimo_nodo_al_principio(self) -> None:
        if self.is_empty():
            raise IndexError("No se puede pasar el ultimo nodo al principio si la lista esta vacia")
        primerNodo = self.primero
        if not primerNodo.tiene_siguiente():
            raise IndexError("Este metodo solo puede aplicarse si hay mas de un nodo")
        self.primero = self.pop()
        self.primero.siguiente = primerNodo
        
    def reemplazar_ocurrencias(self, elemento_a_reemplazar:any, elemento_reemplazo:any) -> None:
        if self.is_empty():
            raise IndexError("No se puede reemplazar ocurrencias si la lista esta vacia")
        nodoAux = self.primero
        if self.primero.valor == elemento_a_reemplazar:
            self.primero.valor = elemento_reemplazo
        while nodoAux.tiene_siguiente():
            nodoAux = nodoAux.siguiente
            if nodoAux.valor == elemento_a_reemplazar:
                nodoAux.valor = elemento_reemplazo
                
    def duplicar(self) -> None:
        if self.is_empty():
            raise IndexError("No se puede duplicar una lista vacia")
        listaDuplicada = self.clone()
        nodoAux = listaDuplicada.primero
        while nodoAux is not None:
            self.append(nodoAux.valor)
            nodoAux = nodoAux.siguiente
    
    def recorrido_salteado(self) -> list[any]:
        lista = []
        if self.is_empty():
            return lista
        nodoAux = self.primero
        lista.append(nodoAux.valor)
        if not self.primero.tiene_siguiente():
            return lista
        while nodoAux.tiene_siguiente() and nodoAux.siguiente.tiene_siguiente():
            nodoAux = nodoAux.siguiente.siguiente
            lista.append(nodoAux.valor)
        return lista
    
    def recorrido_salteado_si_impar(self) -> list[int]:
        lista = []
        if self.is_empty():
            return lista
        nodoAux = self.primero
        lista.append(nodoAux.valor)
        while nodoAux.tiene_siguiente():
            if nodoAux.valor % 2 == 0:
                nodoAux = nodoAux.siguiente
                lista.append(nodoAux.valor)
                continue
            if nodoAux.siguiente.tiene_siguiente():
                nodoAux = nodoAux.siguiente.siguiente
                lista.append(nodoAux.valor)
        return lista
    
    def multiplicacion_de_menor(self, numero1: int, numero2: int) -> None:
        if self.is_empty():
            raise IndexError("No se puede recorrer una lista vacia")
        nodoAux = self.primero
        if nodoAux.valor <= numero1:
            nodoAux.valor = numero2 * nodoAux.valor
        while nodoAux.tiene_siguiente():
            nodoAux = nodoAux.siguiente
            if nodoAux.valor <= numero1:
                nodoAux.valor = numero2 * nodoAux.valor

    def multiplicacion_de_menor_recursivo(self, numero1:int, numero2:int) -> None:
        if self.is_empty():
            raise IndexError("No se puede recorrer una lista vacia")
        self.primero.multiplicacion_de_menor_recursivo(numero1, numero2)

    
    def reemplazar_por_nuevo(self, posicion: int, nuevo_valor: any) -> None:
        if self.is_empty():
            raise IndexError("No se puede recorrer una lista vacia")
        if posicion < 0:
            raise IndexError("No se puede reemplazar un valor en una posicion negativa")
        if posicion >= len(self):
            raise IndexError("Indice fuera de rango")
        nodoAux = self.primero
        indice = 0
        while indice != posicion:
            nodoAux = nodoAux.siguiente
            indice += 1
        nodoAux.valor = nuevo_valor
        
    def agregar_elemento_ordenado(self, elemento:int) -> None:
        nodoAAgregar = Nodo(elemento)
        nodoAux = self.primero
        if self.is_empty():
            self.primero = nodoAAgregar
            return
        if nodoAux.valor > elemento:
            nodoAAgregar.siguiente = self.primero
            self.primero = nodoAAgregar 
        while nodoAux.tiene_siguiente() and nodoAux.siguiente.valor < elemento:
            nodoAux = nodoAux.siguiente
        nodoAAgregar.siguiente = nodoAux.siguiente
        nodoAux.siguiente = nodoAAgregar

match actividad:
    case 1:
        print(f"{bcolors.HEADER}Implementar el TDA Lista enlazada simple, con las siguientes operaciones: constructor, vaciar, append, insert, get, pop, len, is_empty, clone, repr {bcolors.ENDC}")
        Lista = ListaEnlazada()
        Lista.append(1)
        Lista.append(2)
        Lista.append(3)
        print(f"{bcolors.OKGREEN}Lista enlazada creada: {Lista}{bcolors.ENDC}")
        print(len(Lista))
        Lista.insert(4, 1)
        print(f"{bcolors.OKGREEN}Lista enlazada luego de insertar 4 en la posicion 1: {Lista}{bcolors.ENDC}")
        Lista.pop(1)
        print(f"{bcolors.OKGREEN}Lista enlazada luego de eliminar el elemento en la posicion 1: {Lista}{bcolors.ENDC}")
        Lista.get(1)
        print(f"{bcolors.OKGREEN}Elemento en la posicion 1: {Lista.get(1)}{bcolors.ENDC}")
        listaClonada = Lista.clone()
        print(f"{bcolors.OKGREEN}Lista clonada: {listaClonada}{bcolors.ENDC}")
        Lista.vaciar()
        print(f"{bcolors.OKGREEN}Lista enlazada vaciada: {Lista}{bcolors.ENDC}")
        print(f"{bcolors.OKGREEN}En la lista clonada, el elemento 2 esta presente: {2 in listaClonada}{bcolors.ENDC}")
        listaClonada[1] = 5
        print(f"{bcolors.OKGREEN}Lista clonada luego de cambiar el elemento en la posicion 1 por 5: {listaClonada}{bcolors.ENDC}")
    case 2:
        print(f"{bcolors.HEADER}Implementar el metodo intercambiar para intercambiar dos primeros elementos de la lista enlazada simple{bcolors.ENDC}")
        lista = ListaEnlazada()
        lista.append(1)
        lista.append(2)
        print(f"{bcolors.OKGREEN}Lista enlazada creada: {lista}{bcolors.ENDC}")
        lista.intercambiar_primeros()
        print(f"{bcolors.OKGREEN}Lista enlazada luego de intercambiar los dos primeros elementos: {lista}{bcolors.ENDC}")
    case 3:
        print(f"{bcolors.HEADER} Escribir la operación del TDA Lista indicesElemento() que busque un elemento que recibe por parámetro. La operación debe retornar una lista con los indices del elemento en la lista de entrada.")
        lista = ListaEnlazada()
        lista.append(1)
        lista.append(2)
        lista.append(3)
        lista.append(1)
        lista.append(4)
        lista.append(1)
        print(f"{bcolors.OKGREEN}Lista enlazada creada: {lista}{bcolors.ENDC}")
        indices = lista.indices_elemento(1)
        indicesRecursivos = lista.indices_elemento_recursivo(1)
        print(f"{bcolors.OKGREEN}Indices del elemento 1 en la lista: {indices}{bcolors.ENDC}")
        print(f"{bcolors.OKGREEN}Indices del elemento 1 en la lista (recursivo): {indicesRecursivos}{bcolors.ENDC}")
    case 4:
        print(f"{bcolors.HEADER}Escribir una operacion del TDA Lista que elimine todas las ocurrencias de un elemento que recibe por parametro. {bcolors.ENDC}")
        lista = ListaEnlazada()
        lista.append(1)
        lista.append(1)
        lista.append(1)
        lista.append(2)
        lista.append(3)
        lista.append(1)
        lista.append(4)
        lista.append(1)
        
        print(f"{bcolors.OKGREEN}Lista enlazada creada: {lista}{bcolors.ENDC}")
        lista.eliminar_ocurrencias(1)
        print(f"{bcolors.OKGREEN}Lista enlazada luego de eliminar las ocurrencias del elemento 1: {lista}{bcolors.ENDC}")
    case 5:
        print(f"{bcolors.HEADER}Escribir una operación del TDA Lista que saque el nodo que esta al inicio de la lista (posición cero) y lo ponga en el final. Hacer otra que haga lo contrario, saque el nodo del final y lo ponga al inicio.{bcolors.ENDC}")
        lista = ListaEnlazada()
        lista.append(1)
        lista.append(2)
        lista.append(3)
        lista.append(4)
        print(f"{bcolors.OKGREEN}Lista enlazada creada: {lista}{bcolors.ENDC}")
        lista.primer_nodo_al_final()
        print(f"{bcolors.OKGREEN}Lista enlazada luego de pasar el primer nodo al final: {lista}{bcolors.ENDC}")
        lista.ultimo_nodo_al_principio()
        print(f"{bcolors.OKGREEN}Lista enlazada luego de pasar el ultimo nodo al principio: {lista}{bcolors.ENDC}")
    case 6:
        print(f"{bcolors.HEADER}Escribir una operación del TDA Lista que reemplace todas las ocurrencias de un numero por otro. Ambos números los recibe por parámetro.{bcolors.ENDC}")
        lista = ListaEnlazada()
        lista.append(1)
        lista.append(2)
        lista.append(1)
        lista.append(3)
        lista.append(1)
        print(f"{bcolors.OKGREEN}Lista enlazada creada: {lista}{bcolors.ENDC}")
        lista.reemplazar_ocurrencias(1, 5)
        print(f"{bcolors.OKGREEN}Lista enlazada luego de reemplazar las ocurrencias del elemento 1 por 5: {lista}{bcolors.ENDC}")
    case 7:
        print(f"{bcolors.HEADER} Escribir la operación duplicar() del TDA Lista que duplica el contenido de una lista. {bcolors.ENDC}")
        lista = ListaEnlazada()
        lista.append(1)
        lista.append(2)
        lista.append(3)
        print(f"{bcolors.OKGREEN}Lista enlazada creada: {lista}{bcolors.ENDC}")
        lista.duplicar()
        print(f"{bcolors.OKGREEN}Lista enlazada luego de duplicar su contenido: {lista}{bcolors.ENDC}")
    case 8:
        print(f"{bcolors.HEADER}Escribir una operación del TDA Lista que recorra la lista salteandose de a un nodo y mostrando por pantalla los elementos de los nodos visitados.{bcolors.ENDC}")
        lista = ListaEnlazada()
        lista.append(1)
        lista.append(2)
        lista.append(3)
        lista.append(4)
        lista.append(5)
        print(f"{bcolors.OKGREEN}Lista enlazada creada: {lista}{bcolors.ENDC}")
        recorrido = lista.recorrido_salteado()
        print(f"{bcolors.OKGREEN}Recorrido salteado de la lista: {recorrido}{bcolors.ENDC}")
    case 9:
        print(f"{bcolors.HEADER}Escribir una operación del TDA Lista la cual realize un recorrido de la lista, si el elemento es par entonces sigue con el siguiente, si es impar entonces sigue con el siguiente del siguiente. Retornar una lista con los elementos visitados.{bcolors.ENDC}")
        lista = ListaEnlazada()
        lista.append(1)
        lista.append(2)
        lista.append(3)
        lista.append(4)
        lista.append(4)
        lista.append(5)
        print(f"{bcolors.OKGREEN}Lista enlazada creada: {lista}{bcolors.ENDC}")
        recorrido = lista.recorrido_salteado_si_impar()
        print(f"{bcolors.OKGREEN}Recorrido salteado de la lista si el elemento es impar: {recorrido}{bcolors.ENDC}")
    case 10:
        print(f"{bcolors.HEADER}Escribir una operación del TDA Lista que recibe dos números por parámetro. La operación recorre la lista, si el elemento del nodo es menor que el primer parámetro se deja igual, si es mayor o igual, se reemplaza por el mismo número multiplicado por el otro parámetro.{bcolors.ENDC}")
        lista = ListaEnlazada()
        lista.append(1)
        lista.append(2)
        lista.append(3)
        lista.append(4)
        lista.append(5)
        print(f"{bcolors.OKGREEN}Lista enlazada creada: {lista}{bcolors.ENDC}")
        lista.multiplicacion_de_menor(3, 2)
        print(f"{bcolors.OKGREEN}Lista enlazada luego de multiplicar los elementos menores a 3 por 2: {lista}{bcolors.ENDC}")
        lista.vaciar()
        lista.append(1)
        lista.append(2)
        lista.append(3)
        lista.append(4)
        lista.append(5)
        lista.multiplicacion_de_menor_recursivo(3, 2)
        print(f"{bcolors.OKGREEN}Lista enlazada luego de multiplicar los elementos menores a 3 por 2 de manera recursiva: {lista}{bcolors.ENDC}")
    case 11:
        print(f"{bcolors.HEADER}Escribir una operación del TDA Lista que recibe dos números por parámetro: una posición y un número nuevo. Recorre la lista hasta la posición y reemplaza el número de la lista por el nuevo.{bcolors.ENDC}")
        lista = ListaEnlazada()
        lista.append(1)
        lista.append(2)
        lista.append(3)
        lista.append(4)
        lista.append(5)
        print(f"{bcolors.OKGREEN}Lista enlazada creada: {lista}{bcolors.ENDC}")
        lista.reemplazar_por_nuevo(2, 10)
        print(f"{bcolors.OKGREEN}Lista enlazada luego de reemplazar el elemento en la posicion 2 por 10: {lista}{bcolors.ENDC}")
    case 12:
        print(f"{bcolors.HEADER}Escribir la operación insertarOrdenado() del TDA Lista, que se llama desde una lista ordenada e inserta un número que recibe por parámetro en el lugar correcto (manteniendo el orden de menor a mayor).{bcolors.ENDC}")
        lista = ListaEnlazada()
        lista.append(1)
        lista.append(2)
        lista.append(4)
        lista.append(5)
        print(f"{bcolors.OKGREEN}Lista enlazada creada: {lista}{bcolors.ENDC}")
        lista.agregar_elemento_ordenado(3)
        print(f"{bcolors.OKGREEN}Lista enlazada luego de agregar el elemento 3 en el lugar correcto: {lista}{bcolors.ENDC}")
        lista.pop(2)
        lista.agregar_elemento_ordenado_recursivo(3)
        print(f"{bcolors.OKGREEN}Lista enlazada luego de agregar el elemento 3 en el lugar correcto de manera recursiva: {lista}{bcolors.ENDC}")