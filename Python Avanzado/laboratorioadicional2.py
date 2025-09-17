""" Ejercicio 1: Mostrar y eliminar
Utilizando un bucle “while”, elaborar un código que imprima en pantalla cada uno de los elementos de una lista y simultáneamente los elimine, hasta quedar vacía """

lista_elementos = ['manzana', 'banana', 'cereza', 'durazno']
while lista_elementos:  
    elemento = lista_elementos.pop(0)  
    print("Elemento eliminado:", elemento)  
print("Lista final:", lista_elementos)  
