# -*- coding: cp1252 -*-
"""

Tarea 3 Ayudantia Computación Paralela Segundo Semestre 2014.

Integrantes: Jonathan León S. (johnnysavior)
             Juan Cortez G. ()
             Christopher Salvatierra L. ()
             Felipe Alvarez R. ()
"""

"""
1.- Obtener una solución serial al algoritmo
"""
# En primer lugar debemos de abrir el fichero que vamos a leer.
# Se debe incluir el archivo adjunto matriz.txt para la correcta
# Ejecuccion de este codigo.

archivo = open('matriz.txt', 'r')
#leemos linea por linea y guardamos en una lista
matriz=archivo.readlines()
#eliminamos el "\n" de cada fila
for indice in range(len(matriz)):
    matriz[indice]=matriz[indice][:-1]
#separamos cada fila en los numeros  que trae separados por espacios
for indice in range(len(matriz)):
    matriz[indice]=matriz[indice].split(" ")    
#ahora hay que transformar cada valor en un int, pues la matriz que obtenemos
#es todo string de strings
for indice_i in range(len(matriz)):
    for indice_j in range(len(matriz[indice_i])):
        matriz[indice_i][indice_j]=int(matriz[indice_i][indice_j])

#definimos algunas cuantas variables necesarias para multiplicar
mayor=-999999999
producto=int()

#definimos variables donde guardaremos los 4 numeros que generan la multiplicacion mas grande
a=int()
b=int()
c=int()
d=int()
#buscando la mayor multiplicacion de 4 numeros adjacentes de forma horizontal
for i in range(len(matriz)):
    for j in range(len(matriz[i])-3):
        producto=matriz[i][j]*matriz[i][j+1]*matriz[i][j+2]*matriz[i][j+3]
        if producto>mayor:
            mayor=producto
            a=matriz[i][j]
            b=matriz[i][j+1]
            c=matriz[i][j+2]
            d=matriz[i][j+3]

print "producto mayor (horizontal) : %d" % (mayor)            
print "factores : %d * %d * %d * %d" % (a,b,c,d)

mayor=-999999999
mayor_final=-999999999
#ahora se repite el procedimiento de multiplicacion anterior pero ahora lo hacemos de arriba
#hacia abajo con cada columna.          
for i in range(len(matriz)-3):
    for j in range(len(matriz[i])):
        producto=matriz[i][j]*matriz[i+1][j]*matriz[i+2][j]*matriz[i+3][j]
        if producto>mayor:
            mayor=producto
            a=matriz[i][j]
            b=matriz[i+1][j]
            c=matriz[i+2][j]
            d=matriz[i+3][j]

if mayor>mayor_final:
    mayor_final=mayor           
            
print "producto mayor (vertical)   : %d" % (mayor)
print "factores : %d * %d * %d * %d" % (a,b,c,d)

#ahora se repite el procedimiento de multiplicacion anterior pero ahora lo hacemos en forma
#diagonal de derecha a izquierda.


j=3
contador=0
mayor=-999999999
for i in range(len(matriz)-3):
    for j in range(len(matriz)-3):
        producto=matriz[i][j]*matriz[i+1][j-1]*matriz[i+2][j-2]*matriz[i+3][j-3]
        contador+=1
        if producto>mayor:
            mayor=producto            
            a=matriz[i][j]
            b=matriz[i+1][j-1]
            c=matriz[i+2][j-2]
            d=matriz[i+3][j-3]
            
if mayor>mayor_final:
    mayor_final=mayor
        
print "producto mayor (diagonal1)   : %d" % (mayor)
print "factores : %d * %d * %d * %d" % (a,b,c,d)


#ahora se repite el procedimiento de multiplicacion anterior pero ahora lo hacemos en forma
#diagonal de izquierda a derecha y damos vuelta la matriz para facilitar el calculo

matriz.reverse()
j=3
mayor=-999999999
for i in range(len(matriz)-3):
    for j in range(len(matriz)-3):
        producto=matriz[i][j]*matriz[i+1][j-1]*matriz[i+2][j-2]*matriz[i+3][j-3]
        if producto>mayor:
            mayor=producto
            a=matriz[i][j]
            b=matriz[i+1][j-1]
            c=matriz[i+2][j-2]
            d=matriz[i+3][j-3]

if mayor>mayor_final:
    mayor_final=mayor            
        
print "producto mayor (diagonal2)   : %d" % (mayor)
print "factores : %d * %d * %d * %d" % (a,b,c,d)
print "\nProducto mayor en la matriz: %d" %(mayor_final)
        
# Cerramos el fichero.
archivo.close()

"""
2.- Describa como puede dividir el problema para cuando tiene p procesadores

R: Una solución sería dividir de acuerdo al método de busqueda de los factores que den mayor
resuldado en la matriz. Para este caso, podriamos usar 4 procesadores, donde cada uno ejecutaria
la busqueda de forma vertical, otro de forma horizontal, otro de forma diagonal derecha-izquierda
y el ultimo procesador buscara de  izquierda-derecha.Finalmente comparar los resultados que obtuvo
cada procesador y quedarse con el mayor de todos.

"""






