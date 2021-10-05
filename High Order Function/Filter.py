my_list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

#Si queremos obtener los numero impares de una lista, con list comprehension seria

odd = [i for i in my_list if i%2 != 0]
print(odd)

#resolviendo con filter sería, Filter como su nombre lo dice, filtra los elementos de un iterable, en este caso, una lista

odd = list(filter(lambda x: x%2 != 0, my_list))
# si la funcion lambda es True, agregamos el valor en odd

print(odd)
print("Se obtiene el mismo resultado con list comprehension y con filter")