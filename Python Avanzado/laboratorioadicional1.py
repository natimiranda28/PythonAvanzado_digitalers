"""  Ejercicio 1: Sumatoria
 Crear un bucle que almacene en una variable la suma de todos los elementos numéricos de una lista, con excepción del último"""

lista_numeros = [10, 20, 30, 40, 50]
suma = 0        
for numero in lista_numeros[:-1]:  # Excluye el último elemento
    suma += numero  
print("La suma de los elementos, excluyendo el último, es:", suma)

