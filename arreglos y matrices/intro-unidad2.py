# Se debe de descargar la libreria numpy creando un nuevo entorno aislado

import numpy as np


print("Pruebe la declaracion, modificacion y accesos usando indices")
arrayPrueba = np.array([1,2,3,4])
print(f"Se crea un array llamado ArrayPrueba con {arrayPrueba}")
print(f"Dado que el indice empieza desde 0, si coloco arrayPrueba[1] me mostrara {arrayPrueba[1]}") 
print("Si deseo modificar el 2 deberia de escribir arrayPrueba[1] = 3")
arrayPrueba[1] = 3
print(arrayPrueba)
matrizPrueba = np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12]])
print(f"Se crea una matriz llamada matrizprueba que contiene {matrizPrueba}")
print(f"Si deseo acceder al 4 deberia de colocar entonces matrizPrueba[0,3] {matrizPrueba[0,3]}")
print("Si deseo modificar el 4 deberia de escribir matrizPrueba[0,3] = 3")
matrizPrueba[0,3] = 3
print(matrizPrueba)
