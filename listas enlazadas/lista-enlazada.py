class ListaEnlazada: 
    class Nodo:
        def __init__(self, valor = None):
            self.valor = valor
            self.siguiente = None
        
        def tiene_siguiente(self):
            return self.siguiente is not None
        
        def append(self, valor):
            if not self.tiene_siguiente():
                self.siguiente = ListaEnlazada.Nodo(valor)
                return self.siguiente
            return self.siguiente.append(valor)
                
        def __repr__(self):
            return str(self.valor) + " -> " + str(self.siguiente)
                
        def length(self, tamaño):
            if not self.tiene_siguiente():
                return tamaño
            return self.siguiente.length(tamaño + 1)
        
        def pop(self, pos:int) -> None:
            if pos != 0:
                return self.siguiente.pop(pos-1)
            if pos == 1 and not self.siguiente.tiene_siguiente():
                nodoBorrado = self.siguiente
                self.siguiente = None
                return nodoBorrado
            nodoBorrado = self
            self.valor = self.siguiente.valor
            self.siguiente = self.siguiente.siguiente
            return nodoBorrado
        
        def insertar(self, posicion, valor):
            if posicion != 1:
                return self.siguiente.insertar(valor, posicion-1)
            valor.siguiente = self.siguiente
            self.siguiente = valor
            
        def get(self, posicion):
            if posicion != 0:
                return self.siguiente.get(posicion-1)
            return self.valor
            
            
    
    def __init__(self):
        self.primero = None
        
    def __repr__(self):
        nodoAux = self.primero
        string = str(nodoAux.valor)
        while nodoAux.tiene_siguiente():
            nodoAux = nodoAux.siguiente
            string += " -> " + str(nodoAux.valor)
        string += " -> None"
        return string
    
    def __len__(self):
        tamaño = 0
        if self.primero is None:
            return tamaño
        return self.primero.length(tamaño)
    
    def is_empty(self):
        return self.primero is None
    
    def append_recursivo(self, valor):
        if self.primero is None:
            self.primero = self.Nodo(valor)
        else:
            self.primero.append(valor)
            
    def append_iterativo(self,valor):
        if self.primero is None:
            self.primero = self.Nodo(valor)
        else:
            nodoAux = self.primero
            while nodoAux.tiene_siguiente():
                nodoAux = nodoAux.siguiente
            nodoAux.siguiente = self.Nodo(valor)
            
    
    def pop_recursivo(self, pos:int) -> None:
        if pos < 0:
            raise IndexError("Índice negativo no permitido")
        if pos > len(self):
            raise IndexError("Índice fuera de rango")
        self.primero.pop(pos)
            
    def pop_iterativo(self,pos:int) -> None:
        if pos < 0:
            raise IndexError("indice negativo no permitido")
        if pos > len(self):
            raise IndexError("Indice fuera de rango")
        posicionActual = 0
        nodoAux = self.primero
        while posicionActual != pos - 1:
            nodoAux = nodoAux.siguiente
            posicionActual+=1
        if not nodoAux.siguiente.tiene_siguiente():
            nodoAux.siguiente = None
        nodoAux.siguiente.valor = nodoAux.siguiente.siguiente.valor
        nodoAux.siguiente.siguiente = nodoAux.siguiente.siguiente.siguiente
        return self

    def insertar_recursivo(self, pos, valor):
        nodoAInsertar = self.Nodo(valor)
        if pos < 0:
            raise IndexError("Indice negativo no permitido")
        if pos > len(self):
            raise IndexError("indice fuera de rango")
        if pos == 0 and self.primero is None:
            self.primero = nodoAInsertar
            return self.primero
        self.primero.insertar(pos, nodoAInsertar)
        
    def insertar_iterativo(self, pos, valor):
        nodoAInsertar = self.Nodo(valor)
        if pos < 0:
            raise IndexError("Indice negativo no permitido")
        if pos > len(self):
            raise IndexError("indice fuera de rango")
        indice = 0
        nodoAux = self.primero
        while indice != pos-1:
            nodoAux = nodoAux.siguiente
            indice += 1
        if not nodoAux.siguiente.tiene_siguiente():
            nodoAux.siguiente = nodoAInsertar
            return self.siguiente
        nodoAInsertar.siguiente(nodoAux.siguiente)
        nodoAux.siguiente = nodoAInsertar
        return nodoAux.siguiente
    
    def get_recursivo(self, pos):
        if pos < 0:
            raise IndexError("Indice negativo no permitido")
        if pos > len(self):
            raise IndexError("indice fuera de rango")
        if pos == 0:
            return self.primero
        return self.primero.get(pos)
    
    def get_iterativo(self, pos):
        if pos < 0:
            raise IndexError("Indice negativo no permitido")
        if pos > len(self):
            raise IndexError("indice fuera de rango")
        nodoAux = self.primero
        indice = 0
        while indice != pos:
            nodoAux = nodoAux.siguiente
            indice += 1
        return nodoAux.valor
    
    
    def clonar(self):
        listaAux = ListaEnlazada()
        nodoAux = self.primero
        if self.primero is None:
            return listaAux
        listaAux.append_iterativo(self.primero.valor)
        while nodoAux.tiene_siguiente():
            nodoAux = nodoAux.siguiente
            listaAux.append_iterativo(nodoAux.valor)
        return listaAux


lista = ListaEnlazada()
lista.append_iterativo(1)
lista.append_iterativo(2)
lista.append_iterativo(3)
lista.append_iterativo(4)
lista.append_recursivo(5)
print(len(lista))
print(lista)
print(lista.get_iterativo(4))
listAClonada = lista.clonar()
print(f"Lista clonada: {listAClonada}")
print(f"Lista original: {lista}")
print(f"La lista esta vacia?: {lista.is_empty()}")
print(lista.pop_iterativo(2))
print(lista.get_recursivo(2))
