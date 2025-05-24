conj1 = set()

conj1.add(1)

conj1.add(2)

conj2 = {1, 2, 3}


print(conj1)

print(conj2)
print(type(conj1))
print(type(conj2))
print(conj1 == conj2)
print(conj1 | conj2) # union
print(conj1 & conj2) # interseccion
print(conj1 - conj2) # diferencia+
print(conj1.issubset(conj2)) # es subconjunto
print(conj1.issuperset(conj2)) # es superconjunto
print(conj1.isdisjoint(conj2)) # no tienen elementos en comun
print(conj1.pop()) # elimina el primer elemento


tupla = (1, 2, 3, 4, 5) # es inmutable

print(tupla)
print(type(tupla))
print(tupla[0])
print(tupla[1:3])

class TuplaDic:
    def __init__(self, clave, valor):
        self.data = (clave, valor)
    
    def __repr__(self):
        return str(self.data)
    
    def __eq__(self, datoAComparar):
        if isinstance(datoAComparar, TuplaDic):
            return self.data[0] == datoAComparar.data[0]
        return self.data[0] == datoAComparar
    
    def __hash__(self):
        return hash(self.data[0]) # Indexacion hashing
    
    def get_key(self):
        return self.data[0]
    
    def get_value(self):
        return self.data[1]

tuplaDic = TuplaDic(1, 2)
print(tuplaDic)
print(tuplaDic.get_key())
print(tuplaDic.get_value())

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
                return tupla.getValue()
        
    def keys(self):
        return [tupla.get_key() for tupla in self._diccionario]
        
    def values(self):
        return [tupla.get_value() for tupla in self._diccionario]
 
    def __contains__(self, clave):
        for tupla in self._diccionario:
            if tupla.get_key() == clave:
                return True
        return False
    
diccionario = Diccionario()
diccionario.insert(1, 2)
diccionario.insert(2, 3)
diccionario.insert(3, 4)
print(diccionario.__repr__())
print(diccionario[1])
diccionario[1] = 5
print(diccionario[1])
print(diccionario.keys())
print(diccionario.values())
print(1 in diccionario)
print(4 in diccionario)
