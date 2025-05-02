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


actividad = int(input("Ingrese el número de actividad: "))

emptyStack = "La pila está vacía"

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
         if not self.is_empty():
            return self.items.pop()
         raise IndexError(emptyStack)

        def peek(self):
         if not self.is_empty():
           return self.items[-1]
         raise IndexError(emptyStack)

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
            def __init__(self, listaInicial=None):
                if listaInicial is not None:
                    self.items = listaInicial
                else:
                    self.items = []

            def is_empty(self):
                return len(self.items) == 0

            def enqueue(self, item):
                self.items.append(item)

            def dequeue(self):
                if not self.is_empty():
                    return self.items.pop(0)
                raise IndexError(emptyStack)

            def top(self):
                if not self.is_empty():
                    return self.items[0]
                raise IndexError(emptyStack)

            def size(self):
                return len(self.items)

            def clear(self):
                self.items = []

            def clone(self):
                new_queue = Cola()
                new_queue.items = self.items.copy()
                return new_queue

            def __repr__(self):
                return str(self.items) 

match actividad:
    case 1:
        print(f"{bcolors.OKGREEN}Implementar el TDA Pila (Stack), con las siguientes operaciones: Crear, Vaciar, Clonar, EstaVacia, Repr, obtener el tamaño, Apilar, Desapilar, obtener primer elemento (top) ${bcolors.ENDC}")
        class Stack:
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
                if not self.is_empty():
                    return self.items.pop()
                raise IndexError(emptyStack)

            def peek(self):
                if not self.is_empty():
                    return self.items[-1]
                raise IndexError(emptyStack)

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
    case 2:
        print(f"{bcolors.OKGREEN}Escribir un programa que declare una pila de enteros y le apile 4 elementos. Luego debe mostrar la pila y su tamaño, desapilar 2 elementos y volver a imprimirla junto con el nuevo tamaño.${bcolors.ENDC}")
        pila = Pila([1,2,3,4])
        print(f"{bcolors.OKBLUE}Se apilan los elementos 5, 6, 7, 8{bcolors.ENDC}")
        pila.push(5)
        pila.push(6)
        pila.push(7)
        pila.push(8)
        print(f"{bcolors.OKBLUE}Pila inicial: {pila} {bcolors.ENDC}")
        print(f"{bcolors.OKBLUE}Tamaño inicial: {pila.size()} {bcolors.ENDC}")
        print(f"{bcolors.OKBLUE}Desapilando elemento {pila.pop()} y {pila.pop()} {bcolors.ENDC}")
        print(f"{bcolors.OKBLUE}Pila después de desapilar: {pila} {bcolors.ENDC}")
        print(f"{bcolors.OKBLUE}Nuevo tamaño: {pila.size()} {bcolors.ENDC}")
    case 3:
        print(f"{bcolors.OKGREEN} Escribir una función que invierta el orden de una pila. No debe devolver una nueva pila invertida, sino invertir la pila que ingresa por parámetro. {bcolors.ENDC}")
        def invertirPila(pila:Pila) -> None:
                clonPila = pila.clone()
                pila.clear()
                while not clonPila.is_empty():
                    pila.push(clonPila.pop()) 
        pila = Pila([1,2,3,4])
        print(f"{bcolors.OKBLUE}Pila inicial: {pila} {bcolors.ENDC}")
        invertirPila(pila)
        print(f"{bcolors.OKBLUE}Pila invertida: {pila} {bcolors.ENDC}")
    case 4:
        print(f"{bcolors.OKGREEN}Escribir una función que tome el ultimo elemento de una pila(la base) y lo coloque en la cima de la misma. {bcolors.ENDC}")
        def convertirPrimerElementoAUltimo(pila:Pila) -> None:
            pilaAux = Pila()
            while pila.size() > 1:
                pilaAux.push(pila.pop())
            primerElemento = pila.pop()
            while not pilaAux.is_empty():
                pila.push(pilaAux.pop())
            pila.push(primerElemento)
        pila = Pila([1,2,3,4])
        print(f"{bcolors.OKBLUE}Pila inicial: {pila} {bcolors.ENDC}")
        convertirPrimerElementoAUltimo(pila)
        print(f"{bcolors.OKBLUE}Pila después de convertir el primer elemento en el último: {pila} {bcolors.ENDC}")
    case 5:
        print(f"{bcolors.OKGREEN} Escribir una función que coloque en el fondo de una pila un nuevo elemento. {bcolors.ENDC}")
        def colocarEnFondo(pila:Pila, elemento) -> None:
            pilaAux = Pila()
            while not pila.is_empty():
                pilaAux.push(pila.pop())
            pila.push(elemento)
            while not pilaAux.is_empty():
                pila.push(pilaAux.pop())
        pila = Pila([1,2,3,4])
        print(f"{bcolors.OKBLUE}Pila inicial: {pila} {bcolors.ENDC}")
        colocarEnFondo(pila, 5)
        print(f"{bcolors.OKBLUE}Pila después de colocar el elemento 5 en el fondo: {pila} {bcolors.ENDC}")
    case 6:
        print(f"{bcolors.OKGREEN} Escribir una función que elimine de una pila todas las ocurrencias de un elemento dado. Usar una pila auxiliar. {bcolors.ENDC}")
        def eliminarElemento(pila:Pila, elemento:any) -> None:
            pilaAux = Pila()
            while not pila.is_empty():
                if pila.peek() == elemento:
                    pila.pop()
                    continue
                pilaAux.push(pila.pop())
            while not pilaAux.is_empty():
                pila.push(pilaAux.pop())
        pila = Pila([1,2,3,4,5,1])
        print(f"{bcolors.OKBLUE}Pila inicial: {pila} {bcolors.ENDC}")
        eliminarElemento(pila, 1)
        print(f"{bcolors.OKBLUE}Pila después de eliminar el elemento 1: {pila} {bcolors.ENDC}")
    case 7:
        print(f"{bcolors.OKGREEN} Escribir un función que duplique el contenido de una pila. {bcolors.ENDC}")
        def duplicarPila(pila:Pila) -> None:
            pilaAux = Pila()
            pilaClon = pila.clone()
            while not pilaClon.is_empty():
                pilaAux.push(pilaClon.pop())
            while not pilaAux.is_empty():
                pila.push(pilaAux.pop())

        pila = Pila([1,2,3,4])
        print(f"{bcolors.OKBLUE}Pila inicial: {pila} {bcolors.ENDC}")
        duplicarPila(pila)
        print(f"{bcolors.OKBLUE}Pila después de duplicar: {pila} {bcolors.ENDC}")
    case 8:
        print(f"{bcolors.OKGREEN} Escribir una función que realiza el cálculo de la suma de dos números enteros de muchos dígitos, . La función recibe dos pilas por parámetro, las que almacenan los dígitos de los números a sumar. {bcolors.ENDC}")
        def pilaResultadoSuma(primeraPila:Pila, segundaPila:Pila) -> Pila:
            if primeraPila.size() != segundaPila.size():
                raise ValueError("Las pilas deben tener el mismo tamaño")
            primerNumero = ""
            segundoNumero = ""
            while not primeraPila.is_empty():
                if type(primeraPila.peek()) is not int:
                    raise ValueError("Los elementos de la primera pila deben ser dígitos")
                primerNumero += str(primeraPila.pop())
            while not segundaPila.is_empty():
                if type(segundaPila.peek()) is not int:
                    raise ValueError("Los elementos de la segunda pila deben ser dígitos")
                segundoNumero += str(segundaPila.pop())
            return Pila([int(primerNumero) + int(segundoNumero)])
        pila1 = Pila([1,2,3,4])
        pila2 = Pila([5,6,7,8])
        print(f"{bcolors.OKBLUE}Pila 1: {pila1} {bcolors.ENDC}")
        print(f"{bcolors.OKBLUE}Pila 2: {pila2} {bcolors.ENDC}")
        resultado = pilaResultadoSuma(pila1, pila2)
        print(f"{bcolors.OKBLUE}Resultado de la suma: {resultado} {bcolors.ENDC}")
    case 9:
        print(f"{bcolors.OKGREEN} Escribir la función “reemplazar”, que recibe como parámetro una pila de enteros y dos números enteros: “viejo” y “nuevo”. La función debe modificar la pila ingresada por parámetro, reemplazando cada ocurrencia del número “viejo” por el “nuevo”.{bcolors.ENDC}")
        def reemplazarOcurrencias(pila:Pila, elementoViejo:any, elementoNuevo:any) -> None:
            pilaAux = Pila()
            while not pila.is_empty():
                if pila.peek() == elementoViejo:
                    pilaAux.push(elementoNuevo)
                    pila.pop()
                    continue
                pilaAux.push(pila.pop())
            while not pilaAux.is_empty():
                pila.push(pilaAux.pop())
        pila = Pila([1,2,3,4,5,1])
        print(f"{bcolors.OKBLUE}Pila inicial: {pila} {bcolors.ENDC}")
        reemplazarOcurrencias(pila, 1, 5)
        print(f"{bcolors.OKBLUE}Pila después de reemplazar el elemento 1 por 5: {pila} {bcolors.ENDC}")
    case 10:
        print(f"{bcolors.OKGREEN} Escribir una función que recibe una pila de enteros y retorna dos pilas, una con solo los números pares y otra con solo los impares, provenientes de la pila de entrada. Al finalizar la función, la pila de entrada no debe estar modificada.{bcolors.ENDC}")
        def pilaParesEImpares(pilaATomarParesEImpares:Pila) -> list[Pila, Pila]:
            pilaClon = pilaATomarParesEImpares.clone()
            pilaPares = Pila()
            pilaImpares = Pila()
            while not pilaClon.is_empty():
                if pilaClon.peek() % 2 == 0:
                    pilaPares.push(pilaClon.pop())
                    continue
                pilaImpares.push(pilaClon.pop())
            return [pilaPares, pilaImpares]
        pila = Pila([1,2,3,4,5,6])
        print(f"{bcolors.OKBLUE}Pila inicial: {pila} {bcolors.ENDC}")
        pilas = pilaParesEImpares(pila)
        print(f"{bcolors.OKBLUE}Pila de pares: {pilas[0]} {bcolors.ENDC}")
        print(f"{bcolors.OKBLUE}Pila de impares: {pilas[1]} {bcolors.ENDC}")
    case 11:
        print(f"{bcolors.OKGREEN} Implementar el TDA Cola (Queue), con las siguientes operaciones: Crear, Vaciar, Clonar, Encolar, Desencolar, Obtener el primer elemento (top), obtener el tamaño, estaVacia, repr. {bcolors.ENDC}")
        class Cola:
            def __init__(self, listaInicial=None):
                if listaInicial is not None:
                    self.items = listaInicial
                else:
                    self.items = []

            def is_empty(self):
                return len(self.items) == 0

            def enqueue(self, item):
                self.items.append(item)

            def dequeue(self):
                if not self.is_empty():
                    return self.items.pop(0)
                raise IndexError(emptyStack)

            def top(self):
                if not self.is_empty():
                    return self.items[0]
                raise IndexError(emptyStack)

            def size(self):
                return len(self.items)

            def clear(self):
                self.items = []

            def clone(self):
                new_queue = Cola()
                new_queue.items = self.items.copy()
                return new_queue

            def __repr__(self):
                return str(self.items) 
            