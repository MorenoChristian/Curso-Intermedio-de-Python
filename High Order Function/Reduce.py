#Para usar Reduce, necesitamos importar una libreria
from functools import reduce

my_list = [2,2,2,2,2]

#si queremos obtener la multiplicacion de todos los elementos de la lista, con un ciclo for sería

all_multiplied = 1

for i in my_list:
    all_multiplied = all_multiplied*i
print(all_multiplied)


#resolviendo con Reduce, primero importamos la libreria

all_multiplied = reduce(lambda a,b: a*b, my_list)
print(all_multiplied)
print("Obtenemos el mismo resultado con el bucle for y con Reduce")