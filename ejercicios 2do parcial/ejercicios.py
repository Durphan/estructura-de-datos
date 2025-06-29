actividad = int(input("Seleccione la actividad"))


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
        
    def agregar_elemento_no_repetido(self, elemento) -> None:
        nodoAAgregar = Nodo(elemento)
        def agregarNoRepetido(nodoAAgregar, nodoActual):
            if nodoAAgregar.valor == nodoActual.valor:
                print("Esta repetido, no se hara nada")
                return
            if nodoActual.siguiente is None:
                nodoActual.siguiente = nodoAAgregar
            else:
                agregarNoRepetido(nodoAAgregar, nodoActual.siguiente)
        agregarNoRepetido(nodoAAgregar, self.primero)

    def eliminar_impares(self):
        def eliminarImpar(nodoActual: 'Nodo'):
            if nodoActual is None:
                return
            if nodoActual.tiene_siguiente():
                if nodoActual.siguiente.valor % 2 == 1:
                    if nodoActual.siguiente.tiene_siguiente():
                        nodoActual.siguiente = nodoActual.siguiente.siguiente
                    else:
                        nodoActual.siguiente = None
                    eliminarImpar(nodoActual)
                eliminarImpar(nodoActual.siguiente)
        eliminarImpar(self.primero)
            
                    
    def insertar_lista_en_posicion(self, lista: list[any], posicion:int) -> None:
        if posicion == 0:
            nodoNuevo = Nodo(lista)
            nodoNuevo.siguiente = self.primero
            self.primero = nodoNuevo
        def insertarListaEnPosicion(nodoActual:'Nodo', posicionActual:int) -> None:
            if nodoActual.tiene_siguiente() and posicionActual+1 < posicion:
                insertarListaEnPosicion(nodoActual.siguiente, posicionActual+1)
                return
            if not nodoActual.tiene_siguiente():
                nodoActual.siguiente = Nodo(lista)
                return
            nodoACambiar = nodoActual.siguiente
            nodoActual.siguiente = Nodo(lista)
            nodoActual.siguiente.siguiente = nodoACambiar
        insertarListaEnPosicion(self.primero, 0)
        
    def insertar_ceros(self) -> None:
        if self.is_empty():
            return
        def insertarCero(nodo:Nodo):
            if nodo.tiene_siguiente():
                if nodo.valor != 0 and nodo.valor % 2 == 0 and nodo.siguiente.valor % 2 == 0:
                    nuevoNodo = Nodo(0)
                    nuevoNodo.siguiente = nodo.siguiente
                    nodo.siguiente = nuevoNodo
                insertarCero(nodo.siguiente)
        insertarCero(self.primero)
    
    
class TuplaDic:
            def __init__(self, clave = None, valor = None):
                self.data = (clave, valor)
            
            def __repr__(self):
                return str(self.data)
            
            def __eq__(self, value):
                if isinstance(value, TuplaDic):
                    return self.data[0] == value.data[0]
                return self.data[0] == value
            
            def __hash__(self):
                return hash(self.data[0])
            
            def get_key(self):
                return self.data[0]
            
            def get_value(self):
                return self.data[1]

class Diccionario:
            def __init__(self, clave = None, valor = None):
                self._diccionario = set()
                if clave is not None and valor is not None:
                    self._diccionario.add(TuplaDic(clave, valor))
            
            def __repr__(self):
                return str(self._diccionario)
                
            def __setitem__(self, clave, valor):
                for tupla in self._diccionario:
                    if tupla.get_key() == clave:
                        self._diccionario.remove(tupla)
                        break
                self._diccionario.add(TuplaDic(clave, valor))
                
            def __getitem__(self, clave):
                for tupla in self._diccionario:
                    if tupla.get_key() == clave:
                        return tupla.get_value()
            
            def insert(self, clave, valor):
                self._diccionario.add(TuplaDic(clave, valor))
            
            def get(self, key):
                for tupla in self._diccionario:
                    if tupla.get_key() == key:
                        return tupla.get_value()
            
            def keys(self):
                return [tupla.get_key() for tupla in self._diccionario]
                
            def values(self):
                return [tupla.get_value() for tupla in self._diccionario]
            
            def __contains__(self, clave):
                for tupla in self._diccionario:
                    if tupla.get_key() == clave:
                        return True
                return False
            
            def remove(self, clave):
                for tupla in self._diccionario:
                    if tupla.get_key() == clave:
                        self._diccionario.remove(tupla)
                        break
            
            def clone(self):
                nuevo_diccionario = Diccionario()
                nuevo_diccionario._diccionario = set(self._diccionario)
                return nuevo_diccionario
            
            def clear(self):
                self._diccionario.clear()
            

class ArbolBinario:
    class NodoArbol:
        def __init__(self, valor) -> None:
            self.valor = valor
            self.hijo_derecho = None
            self.hijo_izquierdo = None
        
        def tiene_hijo_derecho(self) -> bool:
            return self.hijo_derecho is not None
        
        def tiene_hijo_izquierdo(self) -> bool:
            return self.hijo_izquierdo is not None
        
        def grado(self) -> int:
            if self.tiene_hijo_derecho() and self.tiene_hijo_izquierdo():
                return 2
            if self.tiene_hijo_derecho() or self.tiene_hijo_izquierdo():
                return 1
            return 0
        
        def es_hoja(self) -> bool:
            return not self.tiene_hijo_derecho() and not self.tiene_hijo_izquierdo()
        
        def altura(self) -> int: # La altura de un nodo es la cantidad de nodos desde él hasta la hoja más lejana | Profundidad es la cantidad de nodos desde la raíz hasta el nodo
            def contarAltura(nodo):
                if nodo is None:
                    return 0
                alturaDerecha = contarAltura(nodo.hijo_derecho)
                alturaIzquierda = contarAltura(nodo.hijo_izquierdo)
                return 1 + max(alturaDerecha, alturaIzquierda)
            return contarAltura(self)
        
        def es_balanceado(self) -> bool:
                altura_izq = self.hijo_izquierdo.altura() if self.tiene_hijo_izquierdo() else 0
                altura_der = self.hijo_derecho.altura() if self.tiene_hijo_derecho() else 0
                return abs(altura_izq - altura_der) <= 1
        
        
        def predecesor(self) -> 'ArbolBinario.NodoArbol': # El predecesor es el nodo con el valor más grande en el subárbol izquierdo
            if not self.tiene_hijo_izquierdo():
                raise ValueError("No se puede obtener el predecesor de un nodo que no tiene hijo izquierdo")
            return self.hijo_izquierdo.maximo()
        
        def maximo(self) -> 'ArbolBinario.NodoArbol': # El máximo es el nodo con el valor más grande en el subárbol (el que está más a la derecha)
            if not self.tiene_hijo_derecho():
                return self
            return self.hijo_derecho.maximo()
        
        def sucesor(self) -> 'ArbolBinario.NodoArbol': # El sucesor es el nodo con el valor más pequeño en el subárbol derecho
            if not self.tiene_hijo_derecho():
                raise ValueError("No se puede obtener el sucesor de un nodo que no tiene hijo derecho")
            return self.hijo_derecho.minimo()
            
        def minimo(self) -> 'ArbolBinario.NodoArbol': # El minimo es el nodo con el valor más pequeño en el subárbol (el que está más a la izquierda)
            if not self.tiene_hijo_izquierdo():
                return self
            return self.hijo_izquierdo.minimo()
       
    def __init__(self):
        self.raiz = None
    
    def vaciar(self) -> None:
        self.raiz = None
    
    def esta_vacio(self) -> bool:
        return self.raiz is None
    
    def recorrido_preorden(self) -> str:  # Primero el valor, luego los hijos izquierdo y derecho
        def preorden(nodo):
            if self.esta_vacio():
                return ""
            return f"{nodo.valor} " + preorden(nodo.hijo_izquierdo) + preorden(nodo.hijo_derecho)
        
        return preorden(self.raiz).strip()
    
    def recorrido_inorden(self) -> str: # Primero uno de los lados, luego el valor, y finalmente el otro lado
        def inorden(nodo):
            if self.esta_vacio():
                return ""
            if nodo is None:
                return ""
            return inorden(nodo.hijo_izquierdo) + f"{nodo.valor} " + inorden(nodo.hijo_derecho)
        
        return inorden(self.raiz).strip()
    
    def recorrido_postorden(self) -> str: # Primero los hijos izquierdo y derecho, luego el valor
        def postorden(nodo):
            if self.esta_vacio():
                return ""
            return postorden(nodo.hijo_izquierdo) + postorden(nodo.hijo_derecho) + f"{nodo.valor} "
        return postorden(self.raiz).strip() # Elimina los espacios al final
        
    def insertar(self, elemento) -> 'ArbolBinario.NodoArbol':
        nodoAColocar = self.NodoArbol(elemento)
        if self.esta_vacio():
            self.raiz = nodoAColocar
            return self.raiz
        def insertarEnArbol(elemento, nodo):
            if nodo.valor > elemento:
                if not nodo.tiene_hijo_izquierdo():
                    nodo.hijo_izquierdo = nodoAColocar
                    return nodoAColocar
                return insertarEnArbol(elemento, nodo.hijo_izquierdo)
            if nodo.valor < elemento:
                if not nodo.tiene_hijo_derecho():
                    nodo.hijo_derecho = nodoAColocar
                    return nodoAColocar
                return insertarEnArbol(elemento, nodo.hijo_derecho)
            raise ValueError("El elemento que se quiere ingresar ya esta en el nodo")
        return insertarEnArbol(elemento, self.raiz)
                
    def __contains__(self, valor) -> bool:
        if self.esta_vacio():
            return False
        def buscarValorEnArbol(valor, nodo):
            if nodo.valor == valor:
                return True
            if nodo.valor > valor and nodo.tiene_hijo_izquierdo():
                return buscarValorEnArbol(valor, nodo.hijo_izquierdo)
            if nodo.valor < valor and nodo.tiene_hijo_derecho():
                return buscarValorEnArbol(valor, nodo.hijo_derecho)
            return False
        return buscarValorEnArbol(valor, self.raiz)
    
    def eliminar(self, valor) -> None:
        if self.esta_vacio():
            raise ValueError("No se puede eliminar un nodo en un arbol vacio")
        arbolAux = ArbolBinario()
        def eliminarDelArbol(valor, nodo, arbolAux):
            if nodo.valor == valor:
                if nodo.tiene_hijo_derecho():
                    eliminarDelArbol(valor, nodo.hijo_derecho(), arbolAux)
                if nodo.tiene_hijo_izquierdo():
                    eliminarDelArbol(valor, nodo.hijo_izquierdo(), arbolAux)
            arbolAux.insertar(nodo.valor)
        eliminarDelArbol(valor, self.raiz, arbolAux)
        self.raiz = arbolAux.raiz
        
    def eliminar_sin_auxiliar(self, valor) -> None:
        if self.esta_vacio():
            raise ValueError("No se puede eliminar un nodo en un arbol vacio")
        def eliminarDelArbol(nodo, valor):
            if not nodo:
                raise ValueError("Valor no encontrado en el árbol")
            if valor < nodo.valor:
                nodo.hijo_izquierdo = eliminarDelArbol(nodo.hijo_izquierdo, valor)
            elif valor > nodo.valor:
                nodo.hijo_derecho = eliminarDelArbol(nodo.hijo_derecho, valor)
            else:
                if not nodo.tiene_hijo_izquierdo():
                    return nodo.hijo_derecho
                elif not nodo.tiene_hijo_derecho():
                    return nodo.hijo_izquierdo
                elif not nodo.tiene_hijo_izquierdo() and not nodo.tiene_hijo_derecho():
                    return None
                else:
                    sucesor = nodo.hijo_derecho.minimo()
                    nodo.valor = sucesor.valor
                    nodo.hijo_derecho = eliminarDelArbol(nodo.hijo_derecho, sucesor.valor)
            return nodo
        self.raiz = eliminarDelArbol(self.raiz, valor)
        
    def clonar(self) -> 'ArbolBinario':
        arbolClonado = ArbolBinario()
        def clonarArbol(arbolClonado, nodo):
            if nodo is not None:
                arbolClonado.insertar(nodo.valor)
                clonarArbol(arbolClonado, nodo.hijo_derecho)
                clonarArbol(arbolClonado, nodo.hijo_izquierdo)
        clonarArbol(arbolClonado, self.raiz)
        return arbolClonado
    
    def peso(self) -> int:
        def pesoArbol(nodo) -> int:
            if nodo is not None:
                return 1 + pesoArbol(nodo.hijo_izquierdo) + pesoArbol(nodo.hijo_derecho)
        return pesoArbol(self.raiz)
    
    def maximo(self) -> NodoArbol:
        return self.raiz.maximo()
    
    def minimo(self) -> NodoArbol:
        return self.raiz.minimo()
    
    def profundidad(self) -> int:
        def profundidadArbol(nodo):
            if nodo is not None:
                return 1 + max(profundidadArbol(nodo.hijo_derecho), profundidadArbol(nodo.hijo_izquierdo))
            return 0
        return profundidadArbol(self.raiz)
            
    def profundidad_elemento(self, elemento) -> int:
        def medirProfundidadDeElemento(nodo, elemento, nivelProfundidad):
            if nodo is None:
                return None
            if nodo.elemento == elemento:
                return nivelProfundidad
            izquierda = medirProfundidadDeElemento(nodo.hijo_izquierdo, elemento, nivelProfundidad+1)
            if izquierda is not None:
                return izquierda
            return medirProfundidadDeElemento(nodo.hijo_derecho, elemento, nivelProfundidad+1)
        return medirProfundidadDeElemento(self.raiz, elemento, 0)
    
    def cantidad_hojas(self) -> int:
        def contarHojas(nodo):
            if nodo is None:
                return 0
            if nodo.es_hoja():
                return 1
            return contarHojas(nodo.hijo_izquierdo) + contarHojas(nodo.hijo_derecho)
        return contarHojas(self.raiz)
    
    def nodos_en_nivel(self, nivel) -> str | ValueError:
        def mostrarNodosDeNivel(nodo:'ArbolBinario.NodoArbol', nivelAMostrar, nivelActual) -> None:
            if nodo is None:
                raise ValueError("No existe el nivel indicado dentro del arbol")
            if nivelActual < nivelAMostrar:
                mostrarNodosDeNivel(nodo.hijo_derecho, nivelAMostrar, nivelActual+1)
                mostrarNodosDeNivel(nodo.hijo_izquierdo, nivelAMostrar, nivelActual+1)
            else:
                print(nodo.valor)
        mostrarNodosDeNivel(self.raiz, nivel, 0)
    
    def frontera(self):
        def contenidoHojas(nodo) -> str:
            if nodo is None:
                return ""
            if nodo.es_hoja():
                return str(nodo.valor) + " "
            return contenidoHojas(nodo.hijo_izquierdo) + contenidoHojas(nodo.hijo_derecho)
        return contenidoHojas(self.raiz)
    
    def rotar(self) -> None:
        def realizarRotacion(nodo:'ArbolBinario.NodoArbol') -> None:
            if nodo is None:
                return
            hijoACopiar = nodo.hijo_izquierdo
            nodo.hijo_izquierdo = nodo.hijo_derecho
            nodo.hijo_derecho = hijoACopiar
            realizarRotacion(nodo.hijo_izquierdo)
            realizarRotacion(nodo.hijo_derecho)
        return realizarRotacion(self.raiz)

    def cantidad_nodos_en_nivel(self, nivel: int) -> int:
        def contarCantidadDeNivel(nodo:'ArbolBinario.NodoArbol', nivel: int, nivelActual: int) -> int:
            if nodo is None:
                return 0
            if nivelActual == nivel:
                return 1
            return contarCantidadDeNivel(nodo.hijo_izquierdo, nivel, nivelActual + 1) + contarCantidadDeNivel(nodo.hijo_derecho, nivel, nivelActual + 1)
        return contarCantidadDeNivel(self.raiz, nivel, 0)
    
    def es_balanceado(self) -> bool:
        if self.raiz is None:
            raise ValueError("El arbol a saber si es balanceado no tiene raiz")
        def recorrerArbol(nodo: 'ArbolBinario.NodoArbol'):
            if nodo.es_hoja():
                return True
            return nodo.es_balanceado() and recorrerArbol(nodo.hijo_derecho) and recorrerArbol(nodo.hijo_izquierdo)
        return recorrerArbol(self.raiz)
    
    def es_completo(self) -> bool:
        if self.raiz is None and self.profundidad() == 0:
            return True
        def sonAlteultimosNodosCompletos(nodo:'ArbolBinario.NodoArbol', nivelActual:int):
            if nodo is None:
                return True
            if nivelActual < self.profundidad() - 1:
                if not nodo.tiene_hijo_derecho() or not nodo.tiene_hijo_izquierdo():
                    return False
            if not nodo.tiene_hijo_derecho() and nodo.tiene_hijo_izquierdo():
                return False
            return sonAlteultimosNodosCompletos(nodo.hijo_derecho, nivelActual+1) and sonAlteultimosNodosCompletos(nodo.hijo_izquierdo, nivelActual+1)
        return sonAlteultimosNodosCompletos(self.raiz, 0)
    
    def promedio_hojas(self) -> int:
        def recorrer_arbol(nodo:'ArbolBinario.NodoArbol', totalValorHojas: int) -> int:
            if nodo is None:
                return totalValorHojas
            if nodo.es_hoja():
                return totalValorHojas + nodo.valor
            totalValorHojas = recorrer_arbol(nodo.hijo_izquierdo, totalValorHojas)
            totalValorHojas = recorrer_arbol(nodo.hijo_derecho, totalValorHojas)
            return totalValorHojas
        return int(recorrer_arbol(self.raiz, 0) / self.cantidad_hojas()) if self.cantidad_hojas() > 0 else 0
    
    def sumar_hasta_nivel(self, nivel:int) -> int:
        def sumaHastaNivel(nodo:'ArbolBinario.NodoArbol', nivelActual:int) -> int:
            if nodo is None or nivelActual >= nivel:
                    return 0
            return (nodo.valor + sumaHastaNivel(nodo.hijo_izquierdo, nivelActual + 1) + sumaHastaNivel(nodo.hijo_derecho, nivelActual + 1))
        return sumaHastaNivel(self.raiz, 0)
    
    def sum_mayores(self, numeroAComparar:int) -> int:
        if self.esta_vacio():
            return 0
        def totalDeMayores(nodo: 'ArbolBinario.NodoArbol', total:int):
            if nodo is None:
                return 0
            if nodo.valor < numeroAComparar:
                 total += nodo.valor
            return total + totalDeMayores(nodo.hijo_derecho,total) + totalDeMayores(nodo.hijo_izquierdo, total)
        return totalDeMayores(self.raiz, 0)
                
            
        
                
            
    
match actividad:
    case 1:
        print(f"{bcolors.OKGREEN}Actividad 1: Escribir una funcion que calcule la interseccion de dos diccionarios.{bcolors.ENDC}")
        def interseccion(diccionarioA:Diccionario, diccionarioB:Diccionario) -> Diccionario:
            diccionarioAux = Diccionario()
            for clave in diccionarioA.keys():
                if clave in diccionarioB:
                    diccionarioAux.insert(clave, [diccionarioA[clave], diccionarioB[clave]])
            return diccionarioAux
        diccionario1 = Diccionario("a", 1)
        diccionario1.insert("b", 2)
        diccionario1.insert("c", 3)
        diccionario2 = Diccionario("a", 4)
        diccionario2.insert("b", 5)
        diccionario2.insert("d", 6)
        print(f"Diccionario 1: {diccionario1}")
        print(f"Diccionario 2: {diccionario2}")
        resultado = interseccion(diccionario1, diccionario2)
        print(f"Interseccion: {resultado}")
    case 2:
        print(f"{bcolors.OKGREEN}Actividad 2: Escribir una operación del TDA ABB, que calcule el promedio de los valores acumulados en el árbol.{bcolors.ENDC}")
        arbol = ArbolBinario()
        arbol.insertar(10)
        arbol.insertar(5)
        arbol.insertar(15)
        arbol.insertar(3)
        arbol.insertar(7)
        arbol.insertar(12)
        arbol.insertar(18)
        print(f"Arbol: {arbol.recorrido_inorden()}")
        resultado = arbol.promedio_hojas()
        print(f"Promedio de hojas: {resultado}")
    case 3:
        print(f"{bcolors.OKGREEN}Actividad 3: Escribir una operación del TDA Lista que inserte un dato de modo similar al insertar básico, al final de la lista (append). Pero ahora, no se debe permitir insertar datos repetidos.{bcolors.ENDC}")
        lista = ListaEnlazada()
        lista.append(1)
        lista.append(2)
        lista.append(3)
        print(f"Lista original: {lista}")
        lista.agregar_elemento_no_repetido(4)
        print(f"Lista luego de agregar 4: {lista}")
        lista.agregar_elemento_no_repetido(2)  # No se debe agregar
        print(f"Lista luego de intentar agregar 2: {lista}")
    case 4:
        print(f"{bcolors.OKGREEN}Actividad 4: Escribir la función maximoPorNumero que recibe una lista de pares (x,y) que indica que el número x está asociado al valor y. {bcolors.ENDC}")
        lista = [(1,5), (2,3), (3,8), (4,2), (5,6), (1,7), (2,4)]
        def maximoPorNumero(lista) -> Diccionario:
            diccionario = Diccionario()
            for dupla in lista:
                if dupla[0] not in diccionario:
                    diccionario.insert(dupla[0],dupla[1])
                    continue
                if diccionario[dupla[0]] < dupla[1]:
                    diccionario[dupla[0]] = dupla[1]
            return diccionario
        resultado = maximoPorNumero(lista)
        print(f"Lista original: {lista}")
        print(f"Resultado: {resultado}")
    case 5:
        print(f"{bcolors.OKGREEN}Actividad 5: Escribir una operación del TDA Lista (enteros) que tome una lista y elimine todos los elementos impares, la operación NO debe retornar una nueva lista, sino modificar la lista con la cual se llama a la función. Definir la estructura de datos del tipo Lista y del NodoLista utilizados.{bcolors.ENDC}")
        lista = ListaEnlazada()
        lista.append(2)
        lista.append(3)
        lista.append(4)
        lista.append(5)
        lista.append(6)
        print(f"Lista original: {lista}")
        lista.eliminar_impares()
        print(f"Lista luego de eliminar impares: {lista}")
    case 6:
        print(f"{bcolors.OKGREEN}Actividad 6: Escribir la operación sumaHastaNivel del TDA ABB que recibe un nivel N por parámetro y retorna la suma de todos los números en el ABB en nodos que estén a nivel menor o igual a N. La operación puede hacer uso de las operaciones del TDA ABB: estaVacio y del TDA NodoArbol: tieneIzquierdo y tieneDerecho.{bcolors.ENDC}")
        arbol = ArbolBinario()
        arbol.insertar(10)
        arbol.insertar(5)
        arbol.insertar(15)
        arbol.insertar(3)
        arbol.insertar(7)
        arbol.insertar(12)
        arbol.insertar(18)
        print(f"Arbol: {arbol.recorrido_inorden()}")
        nivel = 1
        resultado = arbol.sumar_hasta_nivel(nivel)
        print(f"Suma de nodos hasta el nivel {nivel}: {resultado}") # Deberia de ser 30 (10 + 5 + 15)
    case 7:
        print(f"{bcolors.OKGREEN}Actividad 7: Escribir la operación insertarEnPosI del TDA Lista que inserte una lista completa dentro de otra en una posición determinada. La función debe recibir como parámetro la lista que debe ser insertada y la posición de inserción. Si la posición es más grande que el tamaño de la lista original, la nueva lista se inserta al final.{bcolors.ENDC}")
        lista = ListaEnlazada()
        lista.append(1)
        lista.append(2)
        lista.append(3)
        print(f"Lista original: {lista}")
        lista_a_insertar = [4, 5, 6]
        posicion = 1
        lista.insertar_lista_en_posicion(lista_a_insertar, posicion)
        print(f"Lista luego de insertar {lista_a_insertar} en la posicion {posicion}: {lista}")
        posicion = 10  # Posición mayor que el tamaño de la lista original
        lista.insertar_lista_en_posicion(lista_a_insertar, posicion)
        print(f"Lista luego de intentar insertar {lista_a_insertar} en la posicion {posicion}: {lista}")  # Deberia de agregar al final
    case 8:
        print(f"{bcolors.OKGREEN}Actividad 8: Escribir la función palabrasPorTamaño que recibe una lista de palabras (strings) y retorna un diccionario que posee como clave el tamaño de palabra y como significado una lista con las palabras de ese tamaño que forman parte de la lista de entrada.{bcolors.ENDC}")
        def palabraPorTamanio(listaPalabras: list[str]) -> Diccionario:
            diccionario = Diccionario()
            for palabra in listaPalabras:
                if len(palabra) not in diccionario:
                    diccionario.insert(len(palabra), [palabra])
                    continue
                diccionario[len(palabra)].append(palabra)
            return diccionario
        listaPalabras = ["hola", "mundo", "python", "programacion", "lista", "arbol"]
        resultado = palabraPorTamanio(listaPalabras)
        print(f"Lista de palabras: {listaPalabras}")
        print(f"Resultado: {resultado}")  # Deberia de ser un diccionario
    case 9:
        print(f"Actividad 9: Escribir la operación sumaInternosMenores del TDA ABB que devuelva la suma de los elementos de los nodos internos del árbol que son menores a un valor N que se recibe por parámetro. Definir la estructura del TDA ABB utilizado.{bcolors.ENDC}")
        arbol = ArbolBinario()
        arbol.insertar(10)
        arbol.insertar(5)
        arbol.insertar(15)
        arbol.insertar(3) 
        arbol.insertar(7)
        arbol.insertar(12)
        arbol.insertar(18)
        print(f"Arbol: {arbol.recorrido_inorden()}")
        numeroAComparar = 10
        resultado = arbol.sum_mayores(numeroAComparar)
        print(f"Suma de nodos internos menores a {numeroAComparar}: {resultado}")  # Deberia de ser 25 (5 + 3 + 7 + 12)
    case 10:
        print(f"{bcolors.OKGREEN}Actividad 10: Crear la operación insertarCeros del TDA Lista, que inserte un 0 (cero) entre 2 números pares consecutivos. La función no debe crear una nueva lista, debe modificar la lista con la cual se llama a la operación. Definir la estructura de datos del TDA Lista utilizada.{bcolors.ENDC}")
        lista = ListaEnlazada()
        lista.append(2)
        lista.append(4)
        lista.append(6)
        lista.append(8)
        print(f"Lista original: {lista}")
        lista.insertar_ceros()
        print(f"Lista luego de insertar ceros entre pares: {lista}")  # Deberia de ser 2, 0, 4, 0, 6, 0, 8