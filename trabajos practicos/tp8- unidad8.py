

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
    
    


actividad = int(input("Ingrese el número de actividad:"))


class ListaOrdenada:
    class Nodo:
        def __init__(self, valor):
            self.valor = valor
            self.siguiente = None
            
        def tiene_siguiente(self):
            return self.siguiente is not None
    def __init__(self):
        self.primero = None
    
    def insertar(self, valor):
        if self.primero is None:
            self.primero = self.Nodo(valor)
            return self.primero
        def insertarValor(valor, nodo: 'ListaOrdenada.Nodo'):
            if not nodo.tiene_siguiente():
                nodo.siguiente = self.Nodo(valor)
                return nodo.siguiente
            return insertarValor(valor, nodo.siguiente)
        
    def insertar_menor_a_mayor(self, valor):
        if self.primero is None:
            self.primero = self.Nodo(valor)
            return self.primero
        if self.primero.valor > valor:
            nodoAColocar = self.Nodo(valor)
            nodoAColocar.siguiente = self.primero
            self.primero = nodoAColocar
            return self.primero
        if self.primero.valor == valor:
            raise ValueError("El valor ya existe en la lista")
        def insertarValor(valor, nodo: 'ListaOrdenada.Nodo') -> 'ListaOrdenada.Nodo':
            if nodo.tiene_siguiente():
                if nodo.siguiente.valor == valor:
                    raise ValueError("El valor ya existe en la lista")
                if nodo.siguiente.valor > valor:
                    nodoAColocar = self.Nodo(valor)
                    nodoAColocar.siguiente = nodo.siguiente
                    nodo.siguiente = nodoAColocar
                    return nodoAColocar
            nodo.siguiente = self.Nodo(valor)
            return nodo.siguiente
        return insertarValor(valor, self.primero)
    
    def insertar_menor_a_mayor_pares(self, valor):
        if valor % 2 != 0:
            return
        if self.primero is None:
            self.primero = self.Nodo(valor)
            return
        if self.primero.valor == valor:
            raise ValueError("El valor que se desea agregar ya se encuentra en la lista")
        def insertarValor(valor, nodo:'ListaOrdenada.Nodo'):
            if nodo.tiene_siguiente():
                if valor < nodo.siguiente.valor:
                    nodoNuevo = self.Nodo(valor)
                    nodoNuevo.siguiente = nodo.siguiente
                    nodo.siguiente = nodoNuevo
                    return
                if nodo.siguiente.valor == valor:
                    raise ValueError("El valor que se desea agregar ya se encuentra en la lista")
                return insertarValor(valor, nodo.siguiente)
            nodo.siguiente = self.Nodo(valor)
        return insertarValor(valor, self.primero)
            
    def __repr__(self):
        valores = []
        nodo = self.primero
        while nodo is not None:
            valores.append(str(nodo.valor))
            nodo = nodo.siguiente
        return " -> ".join(valores) if valores else "Lista vacía"
            
            


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
        
        
        
        def predecesor(self): # El predecesor es el nodo con el valor más grande en el subárbol izquierdo
            if not self.tiene_hijo_izquierdo():
                raise ValueError("No se puede obtener el predecesor de un nodo que no tiene hijo izquierdo")
            return self.hijo_izquierdo.maximo()
        
        def maximo(self): # El máximo es el nodo con el valor más grande en el subárbol (el que está más a la derecha)
            if not self.tiene_hijo_derecho():
                return self
            return self.hijo_derecho.maximo()
        
        def sucesor(self): # El sucesor es el nodo con el valor más pequeño en el subárbol derecho
            if not self.tiene_hijo_derecho():
                raise ValueError("No se puede obtener el sucesor de un nodo que no tiene hijo derecho")
            return self.hijo_derecho.minimo()
            
        def minimo(self): # El minimo es el nodo con el valor más pequeño en el subárbol (el que está más a la izquierda)
            if not self.tiene_hijo_izquierdo():
                return self
            return self.hijo_izquierdo.minimo()
       
    def __init__(self):
        self.raiz = None
    
    def vaciar(self):
        self.raiz = None
    
    def esta_vacio(self):
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
        
    def insertar(self, elemento):
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
                
    def __contains__(self, valor):
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
    
    def eliminar(self, valor):
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
        
    def eliminar_sin_auxiliar(self, valor):
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
        
    def clonar(self):
        arbolClonado = ArbolBinario()
        def clonarArbol(arbolClonado, nodo):
            if nodo is not None:
                arbolClonado.insertar(nodo.valor)
                clonarArbol(arbolClonado, nodo.hijo_derecho)
                clonarArbol(arbolClonado, nodo.hijo_izquierdo)
        clonarArbol(arbolClonado, self.raiz)
        return arbolClonado
    
    def peso(self) -> int:
        def pesoArbol(nodo):
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
            
    def profundidad_elemento(self, elemento):
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
    
    def nodos_en_nivel(self, nivel):
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
        def contenidoHojas(nodo):
            if nodo is None:
                return ""
            if nodo.es_hoja():
                return str(nodo.valor) + " "
            return contenidoHojas(nodo.hijo_izquierdo) + contenidoHojas(nodo.hijo_derecho)
        return contenidoHojas(self.raiz)
            
    def lista_ordenada(self):
        lista = ListaOrdenada()
        if self.raiz is None:
            return lista
        def insertarNodo(nodo:ArbolBinario.NodoArbol, lista:ListaOrdenada) -> ListaOrdenada:
            if nodo is not None:
                insertarNodo(nodo.hijo_izquierdo, lista)
                lista.insertar_menor_a_mayor_pares(nodo.valor)
                insertarNodo(nodo.hijo_derecho, lista)
        insertarNodo(self.raiz, lista)
        return lista

    
    def rotar(self):
        def realizarRotacion(nodo:'ArbolBinario.NodoArbol') -> None:
            if nodo is None:
                return
            hijoACopiar = nodo.hijo_izquierdo
            nodo.hijo_izquierdo = nodo.hijo_derecho
            nodo.hijo_derecho = hijoACopiar
            realizarRotacion(nodo.hijo_izquierdo)
            realizarRotacion(nodo.hijo_derecho)
        return realizarRotacion(self.raiz)

    def cantidad_nodos_en_nivel(self, nivel):
        def contarCantidadDeNivel(nodo, nivel, nivelActual):
            if nodo is None:
                return 0
            if nivelActual == nivel:
                return 1
            return contarCantidadDeNivel(nodo.hijo_izquierdo, nivel, nivelActual + 1) + contarCantidadDeNivel(nodo.hijo_derecho, nivel, nivelActual + 1)
            
        return contarCantidadDeNivel(self.raiz, nivel, 0)
    

            
                
    

match actividad:
    case 1: 
        print(f"{bcolors.OKGREEN}Actividad 1: implementar el TDA Árbol binario de búsqueda{bcolors.ENDC}")
        arbol = ArbolBinario()
        arbol.insertar(10)
        arbol.insertar(5)
        arbol.insertar(15)
        arbol.insertar(3)
        arbol.insertar(7)
        arbol.insertar(12)
        arbol.insertar(18)
        print(f"{bcolors.OKBLUE}Árbol binario de búsqueda creado con los valores: {arbol.recorrido_inorden()}{bcolors.ENDC}")
    case 2:
        print(f"{bcolors.OKGREEN}Escribir una operación del TDA ABB que calcule la cantidad de hojas de un árbol.{bcolors.ENDC}")
        arbol = ArbolBinario()
        arbol.insertar(10)
        arbol.insertar(5)
        arbol.insertar(15)
        arbol.insertar(3)
        arbol.insertar(7)
        arbol.insertar(12)
        arbol.insertar(18)
        print(f"{bcolors.OKBLUE}Árbol binario de búsqueda creado con los valores: {arbol.recorrido_inorden()}{bcolors.ENDC}")
        cantidad_hojas = arbol.cantidad_hojas()
        print(f"{bcolors.OKBLUE}Cantidad de hojas en el árbol: {cantidad_hojas}{bcolors.ENDC}")
    case 3:
        print(f"{bcolors.OKGREEN}Escribir una operación del TDA ABB que muestre los elementos que estan en el nivel N de un ABB, el nivel se recibe por parámetro.{bcolors.ENDC}")
        arbol = ArbolBinario()
        arbol.insertar(10)
        arbol.insertar(5)
        arbol.insertar(15)
        arbol.insertar(3)
        arbol.insertar(7)
        arbol.insertar(12)
        arbol.insertar(18)
        print(f"{bcolors.OKBLUE}Árbol binario de búsqueda creado con los valores: {arbol.recorrido_inorden()}{bcolors.ENDC}")
        nivel = int(input("Ingrese el nivel a consultar: "))
        arbol.nodos_en_nivel(nivel)
        
    case 4:
        print(f"{bcolors.OKGREEN} Se define por frontera de un árbol, la secuencia formada por los elementos almacenados en las hojas de un árbol, tomados de izquierda a derecha. Escribir una operación del TDA ABB, que imprima por pantalla la frontera del árbol.{bcolors.ENDC}")
        arbol = ArbolBinario()
        arbol.insertar(10)
        arbol.insertar(5)
        arbol.insertar(15)
        arbol.insertar(3)
        arbol.insertar(7)
        arbol.insertar(12)
        arbol.insertar(18)
        print(f"{bcolors.OKBLUE}Árbol binario de búsqueda creado con los valores: {arbol.recorrido_inorden()}{bcolors.ENDC}")
        frontera = arbol.frontera()
        print(f"{bcolors.OKBLUE}Frontera del árbol: {frontera}{bcolors.ENDC}")
    
    case 5:
        print(f"{bcolors.OKGREEN}Escribir una operación del TDA ABB que retorne una lista ordenada (de menor a mayor) con todos los números pares que forman parte del árbol.{bcolors.ENDC}")
        arbol = ArbolBinario()
        arbol.insertar(10)
        arbol.insertar(5)
        arbol.insertar(15)
        arbol.insertar(3)
        arbol.insertar(7)
        arbol.insertar(12)
        arbol.insertar(18)
        print(f"{bcolors.OKBLUE}Árbol binario de búsqueda creado con los valores: {arbol.recorrido_inorden()}{bcolors.ENDC}")
        lista_ordenada = arbol.lista_ordenada()
        print(f"{bcolors.OKBLUE}Lista ordenada de los elementos del árbol: {lista_ordenada}{bcolors.ENDC}")
    case 6:
        print(f"{bcolors.OKGREEN} Escribir una operación del TDA ABB, que rote el árbol completo es decir, los elementos del subárbol izquierdo deben ser mayores a la raíz y los del subárbol derecho menores{bcolors.ENDC}")
        arbol = ArbolBinario()
        arbol.insertar(10)
        arbol.insertar(5)
        arbol.insertar(15)
        arbol.insertar(3)
        arbol.insertar(7)
        arbol.insertar(12)
        arbol.insertar(18)
        print(f"{bcolors.OKBLUE}Árbol binario de búsqueda creado con los valores: {arbol.recorrido_inorden()}{bcolors.ENDC}")
        print(f"{bcolors.OKBLUE}Árbol antes de rotar: {arbol.recorrido_inorden()}{bcolors.ENDC}")
        arbol.rotar()
        print(f"{bcolors.OKBLUE}Árbol después de rotar: {arbol.recorrido_inorden()}{bcolors.ENDC}")
    case 7:
        print(f"{bcolors.OKGREEN}Escribir una operación del TDA ABB llamada cantidadNodosEnNivel que retorna la cantidad de nodos del arbol en un nivel determinado.{bcolors.ENDC}")
        arbol = ArbolBinario()
        arbol.insertar(10)
        arbol.insertar(5)
        arbol.insertar(15)
        arbol.insertar(3)
        arbol.insertar(7)  
        arbol.insertar(12)
        arbol.insertar(18)
        print(f"{bcolors.OKBLUE}Árbol binario de búsqueda creado con los valores: {arbol.recorrido_inorden()}{bcolors.ENDC}")
        nivel = int(input("Ingrese el nivel a consultar: "))
        cantidad_nodos = arbol.cantidad_nodos_en_nivel(nivel)
        print(f"{bcolors.OKBLUE}Cantidad de nodos en el nivel {nivel}: {cantidad_nodos}{bcolors.ENDC}")
