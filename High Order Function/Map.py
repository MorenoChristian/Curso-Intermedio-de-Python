my_list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

#si queremos obtener los cuadrados de los elementos de la lista, con comprehension hacemos

square = [i**2 for i in my_list]
print(square)

#resolviendo con Map sería, Map modifica los elementos de un iterable, en este caso una lista

square = list(map(lambda x: x**2, my_list))
print(square)

print("Se obtiene los mismos resultados con comprehension y con map")