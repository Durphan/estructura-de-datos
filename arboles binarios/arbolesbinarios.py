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
            
    def profundidad_nivel(self, nivel):
        def medirProfundidadDeNivel(nodo, nivelActual, nivelAMedir):
            if nodo is not None:
                if nivelActual < nivelAMedir:
                    return(
                    medirProfundidadDeNivel(nodo.hijo_derecho, nivelActual+1, nivelAMedir),
                    medirProfundidadDeNivel(nodo.hijo_izquierdo, nivelActual+1, nivelAMedir)    
                    )
                else:
                    return 1 + max(medirProfundidadDeNivel(nodo.hijo_derecho, nivelActual, nivelAMedir), medirProfundidadDeNivel(nodo.hijo_izquierdo, nivelActual, nivelAMedir))
            raise ValueError("El arbol no tiene el nivel seleccionado")
        return medirProfundidadDeNivel(self.raiz, 0, nivel)
            
            
                
        

                        
                    
            

            
                