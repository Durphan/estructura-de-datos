import numpy as np

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

actividad = int(input("Ingrese el número de actividad: "))

match actividad:
    case 1:
        print(f"{bcolors.OKGREEN}Implementar el TDA Diccionario (Map), con las siguientes operaciones: crear, repr, insertar, setitem, get, getitem, len, getkeys, getvalues, contains, remove, clone, clear{bcolors.ENDC}")
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
            
            def insert(self, clave, valor = None):
                self._diccionario.add(TuplaDic(clave, valor))
            
            def get(self, key):
                for tupla in self._diccionario:
                    if tupla.get_key() == key:
                        return tupla.get_value()
                raise KeyError("Clave no encontrada")
            
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
    
    case 2:
        print(f"{bcolors.OKGREEN} Escribir un programa que declare un Diccionario de <entero , entero> (clave entero y significado entero) y le agrege 4 pares. {bcolors.ENDC}")
        diccionario = Diccionario()
        diccionario.insert(1, 2)
        diccionario.insert(2, 3)
        diccionario.insert(3, 4)
        diccionario.insert(4, 5)
        print(diccionario.__repr__())
        print("Redefiniendo el valor de la clave 1")
        diccionario[1] = 5
        print(diccionario[1])
        print(diccionario.__repr__())
    case 3:
        print(f"{bcolors.OKGREEN} Escribir un diccionario con sinónimos. Luego intentar insertar dos pares <clave , significado> con claves repetidas con la operacion insert y ver que sucede. {bcolors.ENDC}")
        diccionario = Diccionario()
        diccionario.insert("feliz", "contento")
        diccionario.insert("triste", "deprimido")
        diccionario.insert("feliz", "contento")
        diccionario.insert("feliz", "contento")
        diccionario.insert("feliz", "contento")
        diccionario.insert("feliz", "alegre")
        print(diccionario.__repr__())
        print(diccionario["feliz"])
    case 4:
        print(f"{bcolors.OKGREEN} Escribir una función que dado una lista de enteros me devuelve otra(no necesariamente en el mismo orden) sin los numeros repetidos.{bcolors.ENDC}")
        def eliminar_repetidos(lista):
            diccionario = Diccionario()
            for elemento in lista:
                diccionario.insert(elemento, None)
            return diccionario.keys()
        lista = [1, 2, 3, 4, 5, 1, 2, 3]
        print(f"Lista original: {lista}")
        lista_sin_repetidos = eliminar_repetidos(lista)
        print(f"Lista sin repetidos: {lista_sin_repetidos}")
    case 5:
        print(f"{bcolors.OKGREEN} Rehacer le ejercicio 4 pero retornando un diccionario en lugar de una lista.{bcolors.ENDC}")
        def eliminar_repetidos(lista):
            diccionario = Diccionario()
            for elemento in lista:
                diccionario.insert(elemento, None)
            return diccionario.clone()
        lista = [1, 2, 3, 4, 5, 1, 2, 3]
        print(f"Lista original: {lista}")
        diccionario_sin_repetidos = eliminar_repetidos(lista)
        print(f"Diccionario sin repetidos: {diccionario_sin_repetidos}")
    case 6:
        print(f"{bcolors.OKGREEN} Escribir una función que recibe una lista de números como parámetro y devuelve un diccionario con los números de la lista como claves y la cantidad de apariciones de cada uno como su significado.{bcolors.ENDC}")
        def cantidadRepetidosEnLista(numero:int, lista:list):
            def contar(numero:int, lista:list, cantidad:int, i:int):
                if i == len(lista):
                    return cantidad
                if lista[i] == numero:
                    return contar(numero, lista, cantidad+1, i+1)
                return contar(numero, lista, cantidad, i+1)
            return contar(numero, lista, 0, 0)
        
        def diccionarioCantidadRepetidos(lista:list) -> Diccionario:
            diccionario = Diccionario()
            for elemento in lista:
                diccionario.insert(elemento, cantidadRepetidosEnLista(elemento, lista))
            return diccionario.__repr__()
        lista = [1, 2, 3, 4, 5, 1, 2, 3]
        print(f"Lista original: {lista}")
        diccionario = diccionarioCantidadRepetidos(lista)
        print(f"Diccionario con cantidad de repetidos: {diccionario}")
    
    case 7:
        print(f"{bcolors.OKGREEN} Escribir una función que recibe dos diccionarios y devuelve otro con la mezcla de los dos, para las claves repetidas, se queda con los significados de primer diccionario.{bcolors.ENDC}")
        def mezclarDiccionarios(diccionario1:Diccionario, diccionario2:Diccionario) -> Diccionario:
            diccionario = Diccionario()
            for clave in diccionario1.keys():
                diccionario.insert(clave, diccionario1[clave])
            for clave in diccionario2.keys():
                if clave in diccionario1:
                    print(f"la clave {clave} esta en el diccionario1")
                    continue
                diccionario.insert(clave, diccionario2[clave])
            return diccionario
        diccionario1 = Diccionario()
        diccionario1.insert(1, 2)
        diccionario1.insert(2, 3)
        diccionario1.insert(3, 4)
        diccionario1.insert(4, 5)
        diccionario2 = Diccionario()
        diccionario2.insert(1, 5)
        diccionario2.insert(2, 6)
        diccionario2.insert(3, 7)
        diccionario2.insert(4, 8)
        diccionario2.insert(5, 9)
        print(diccionario1.__repr__())
        print(diccionario2.__repr__())
        diccionario = mezclarDiccionarios(diccionario1, diccionario2)
        print(diccionario.__repr__())
    case 8:
        print(f"{bcolors.OKGREEN} Escribir una función que modele el problema de administrar las materias que cursa un alumno. Es decir que reciba un diccionario, un alumno y una materia y agregue esa materia a las materias que cursa.{bcolors.ENDC}")
        def agregarMateria(diccionario:Diccionario, alumno:str, materia:str):
            if alumno in diccionario:
                if materia in diccionario[alumno]:
                    raise ValueError("El alumno ya tiene esa materia")
                diccionario[alumno].append(materia)
            else:
                diccionario.insert(alumno, [materia])
            
        diccionario = Diccionario()
        agregarMateria(diccionario, "Juan", "Matematica")
        agregarMateria(diccionario, "Juan", "Fisica")
        agregarMateria(diccionario, "Juan", "Quimica")
        agregarMateria(diccionario, "Pedro", "Matematica")
        agregarMateria(diccionario, "Pedro", "Fisica")
        agregarMateria(diccionario, "Pedro", "Quimica")
        agregarMateria(diccionario, "Pedro", "Matematica")
        print(diccionario.__repr__())
    case 9:
        print(f"{bcolors.OKGREEN} Escribir una función listaToDic que recibe una lista con chirimbolos y devuelve un diccionario con cada chirimbolo como clave y como significado una matriz de nxn donde n es la cantidad de veces que aparece el chirimbolo en la lista. La matriz se debe llenar con el chirimbolo de la clave. {bcolors.ENDC}")
        def cantidadRepetidosEnLista(numero:int, lista:list):
            def contar(numero:int, lista:list, cantidad:int, i:int):
                if i == len(lista):
                    return cantidad
                if lista[i] == numero:
                    return contar(numero, lista, cantidad+1, i+1)
                return contar(numero, lista, cantidad, i+1)
            return contar(numero, lista, 0, 0)
        
        def listaToDic(listaChirimbolos):
            diccionario = Diccionario()
            for chirimbolo in listaChirimbolos:
                diccionario.insert(chirimbolo, np.full((cantidadRepetidosEnLista(chirimbolo, listaChirimbolos), cantidadRepetidosEnLista(chirimbolo, listaChirimbolos)),chirimbolo))
            return diccionario.__repr__()
        lista = [1, 2, 3, 4, 5, 1, 2, 3]
        print(f"Lista original: {lista}")
        diccionario = listaToDic(lista)
        print(f"Diccionario con chirimbolos: {diccionario}")
    case 10:
        print(f"{bcolors.OKGREEN} Escribir la función promedios que recibe una lista de materias (strings) y una lista de notas (enteros) del mismo tamaño. Retorna un diccionario que posee como clave cada materia y como significado su nota promedio.{bcolors.ENDC}")
        def promedios(materias:list[str], notas:list[int]):
            if len(materias) != len(notas):
                raise ValueError("La lista de materias y notas deben de tener la misma longitud")
            diccionario = Diccionario()
            for i in range(len(materias)):
                if materias[i] in diccionario:
                    listaNotas = diccionario[materias[i]]
                    listaNotas.append(notas[i])
                    diccionario[materias[i]] = listaNotas
                    continue
                diccionario.insert(materias[i], [notas[i]])
            for materia in diccionario.keys():
                diccionario[materia] = int(sum(diccionario[materia])/len(diccionario[materia]))
            return diccionario
        materias = ["Matematica", "Fisica", "Quimica", "Matematica", "Fisica", "Quimica"]
        notas = [1, 2, 3, 4, 5, 6]
        print(f"Lista de materias: {materias}")
        print(f"Lista de notas: {notas}")
        diccionario = promedios(materias, notas)
        print(f"Diccionario con promedios: {diccionario}")
    case 11:
        print(f"{bcolors.OKGREEN} Tenemos un diccionario del tipo <Entero , Lista de enteros>, escribir una funcion que devuelva una lista en formato de dupla de productos cartesianos entre la clave y los enteros de la lista. {bcolors.ENDC}")
        def productoCartesianoParcial(diccionario:Diccionario) -> list[tuple[int]]:
            lista = []
            for numeroClave in diccionario.keys():
                for numero in diccionario[numeroClave]:
                    lista.append(TuplaDic(numeroClave, numero))
            return lista
        diccionario = Diccionario()
        diccionario.insert(1, [1, 2, 3])
        diccionario.insert(2, [4, 5, 6])
        diccionario.insert(3, [7, 8, 9])
        print(diccionario.__repr__())
        lista = productoCartesianoParcial(diccionario)
        print(f"Lista de productos cartesianos: {lista}")
    case 12:
        print(f"{bcolors.OKGREEN} Escribir una función que haga lo inverso del Ejercicio 11.{bcolors.ENDC}")
        def productoCartesianoInverso(lista:list[TuplaDic]) -> Diccionario:
            diccionario = Diccionario()
            for tupla in lista:
                if tupla.get_key() in diccionario:
                    listaEnteros = diccionario[tupla.get_key()]
                    listaEnteros.append(tupla.get_value())
                    diccionario[tupla.get_key()] = listaEnteros
                    continue
                diccionario.insert(tupla.get_key(), [tupla.get_value()])
            return diccionario
        lista = [TuplaDic(1, 1), TuplaDic(1, 2), TuplaDic(1, 3), TuplaDic(2, 4), TuplaDic(2, 5), TuplaDic(2, 6), TuplaDic(3, 7), TuplaDic(3, 8), TuplaDic(3, 9)]
        print(f"Lista de productos cartesianos: {lista}")
        diccionario = productoCartesianoInverso(lista)
        print(f"Diccionario: {diccionario.__repr__()}")
    case 13:
        print(f"{bcolors.OKGREEN} Escribir el TDA MatrizDePixels, que modele una matriz de pixels (imagen) de N x M usando el tipo array del paquete numpy, donde cada pixel tiene un color representado por un número entero entre 0 y 255.{bcolors.ENDC}")
        class MatrizDePixels:
            def __init__(self, n:int, m:int ):
                self.matriz = np.zeros((n,m), dtype=int)
                
            def __repr__(self):
                return str(self.matriz)
            
            def __getitem__(self, indices:list[int]) -> int:
                return self.matriz[indices]

            def __setitem__(self, indices:list[int], valor:int):
                self.matriz[indices] = valor
        print(f"{bcolors.OKGREEN} Crear una MatrizDePixels de 100 x 100 y agregarle valores a dos pixels. {bcolors.ENDC}")
        matriz1 = MatrizDePixels(100, 100)
        matriz1[0,0] = 2
        matriz1[0,2] = 230
        matriz1[0,3] = 255
        matriz1[0,4] = 255
        matriz1[0,5] = 255
        matriz1[0,6] = 255
        matriz1[0,7] = 255
        print(matriz1.__repr__())
        print(f"{bcolors.OKGREEN}  Crear una MatrizDePixels de 100000 x 50000 y agregarle valores a dos pixels. {bcolors.ENDC}")
        # matriz2 = MatrizDePixels(100000, 50000)  Da array memory error
        print(f"{bcolors.OKGREEN} Ahora escribir el TDA MatrizDePixelsDict, que modele una matriz de pixels (imagen) de N x M usando un diccionario de <(fila,columna) , pixel>, donde cada pixel tiene un color representado por un número entero entre 0 y 255 y el par (fila,columna) indica la posición del pixel en la matriz.{bcolors.ENDC}")
        class MatrizDePixelDict:
            def __init__(self,n:int, m:int):
                self.matriz = set()
                for primerNumero in range(n):
                    for segundoNumero in range(m):
                        self.matriz.add(TuplaDic((primerNumero, segundoNumero), 0))
            
            def __repr__(self):
                return str(self.matriz)
        
            def __setitem__(self, indices,valor):
                for tupla in self.matriz:
                    if tupla.get_key() == indices:
                        self.matriz.remove(tupla)
                        break
                self.matriz.add(TuplaDic(indices, valor))
                        
                
            def __getitem__(self, indices):
                for tupla in self.matriz:
                    if tupla.get_key() == indices:
                        return tupla.get_value()
                raise KeyError("El pixel no existe")
            
        print(f"{bcolors.OKGREEN} Crear una MatrizDePixelsDict de 100 x 100 y agregarle valores a dos pixels. {bcolors.ENDC}")
        matriz1 = MatrizDePixelDict(100, 100)
        matriz1[0,0] = 2
        matriz1[0,2] = 230
        print(matriz1[0,0])
        print(matriz1[0,2])
        print(f"{bcolors.OKGREEN} Crear una MatrizDePixelsDict de 100000 x 50000 y agregarle valores a dos pixels. {bcolors.ENDC}")
        # matriz2 = MatrizDePixelDict(100000, 50000)  Produce un error
    case 14:
        print(f"{bcolors.OKGREEN} Implementar la suma matrices como operación en el TDA MatrizDePixelsDict implementado en el Ejercicio 13.{bcolors.ENDC}")
        class MatrizDePixelDict:
            def __init__(self,n:int, m:int):
                self.matriz = set()
                for primerNumero in range(n):
                    for segundoNumero in range(m):
                        self.matriz.add(TuplaDic((primerNumero, segundoNumero), 0))
            
            def __repr__(self):
                return str(self.matriz)
        
            def __setitem__(self, indices,valor):
                for tupla in self.matriz:
                    if tupla.get_key() == indices:
                        self.matriz.remove(tupla)
                        break
                self.matriz.add(TuplaDic(indices, valor))
                        
                
            def __getitem__(self, indices):
                for tupla in self.matriz:
                    if tupla.get_key() == indices:
                        return tupla.get_value()
                raise KeyError("El pixel no existe")
            
            def sumar(self, matriz2):
                for tupla in matriz2.keys():
                    if tupla in self:
                        self[tupla] += matriz2[tupla]
                    else:
                        self[tupla] = matriz2[tupla]
                    
            
            def __contains__(self, indices):
                for tupla in self.matriz:
                    if tupla.get_key() == indices:
                        return True
                return False
            
            def keys(self):
                return [tupla.get_key() for tupla in self.matriz]
        matriz1 = MatrizDePixelDict(5, 5)
        matriz2 = MatrizDePixelDict(5, 5)
        matriz1[0,0] = 2
        matriz1[0,2] = 230
        matriz2[0,0] = 2
        matriz2[0,2] = 230
        matriz1.sumar(matriz2)
        print(matriz1[0,0])
        print(matriz1[0,2])
                
            
        
        
        
            
                