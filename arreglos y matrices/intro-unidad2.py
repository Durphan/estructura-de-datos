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
print("Hay dos formas de recorrer un arreglo o matriz, por elementos y por indices")
print("for i in [nombre-arreglo] para recorrer los elementos del arreglo")
for i in arrayPrueba:
    print(i)
print("Otra forma es con for i in np.nditer(arrayPrueba)")
for i in np.nditer(arrayPrueba):
    print(i)
print("for i in range([indice], len(arrayPrueba) para recorrer los elementos desde cierto indice")
for i in range(0, len(arrayPrueba)):
    print(arrayPrueba[i])
print("for i in matriz prueba para recorrer por filas la matriz, mostrando tambien los []")
for i in matrizPrueba:
    print(i)
print("Para recorrer elemento por elemento una matriz se hace un for anidado for i in range(0, len(matrizPrueba) y for j in range(0, len(matrizPrueba[i]))")
for i in range(0, len(matrizPrueba)):
    for j in range(0, len(matrizPrueba[i])):
        print(matrizPrueba[i,j])