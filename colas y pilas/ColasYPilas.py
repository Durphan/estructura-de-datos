print("Declaracion de listas dinamicas en Python")

lista = [1,2,3,4,5]
print("Lista ", lista)
lista.pop(0)
print("Elimina el elemento en la posicion 0: ", lista)
lista.pop()
print("Elimina el ultimo elemento: ", lista)
lista.insert(0,2)
print("Agrega el elemento 1 en la posicion 0: ", lista)
lista.append(5)
print("Agrega el elemento 5 al final: ", lista)

print("El acceso por indices es igual que en arreglos",  {lista[0]})

print("Pilas y colas")

class Pila:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            raise IndexError("La pila está vacía")
        
    def peek(self):
        if not self.is_empty():
            return self.items[len(self.items) - 1]
        else:
            raise IndexError("La pila está vacía")
    
    def is_empty(self):
        return len(self.items) == 0
    
    def size(self):
        return len(self.items)
    
class Cola:
    def __init__(self):
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
    