
def run():

    #list = []

    # for i in range(1,101):
    #     square = i**2
    #     if square % 3 != 0:
    #         list.append(square)

    #Usamos list comprehension para resumir las 4 lineas de codigo solo en 1

    list = [i**2 for i in range(1,101) if i%3 != 0]
    #para cada i en un rango del 1 al 100, agregar a la lista los i elevados al cuadrado si i no es divisible por 3

    print(list)
    print(len(list))

    # DESAFIO, numeros naturales multiplos de 4 que a su vez son multiplos de 6 y 9, hasta el 100000

    square = [i for i in range(1,1001) if i%4 == 0 and i%6 == 0 and i%9 == 0]
    print(square)

    square = [i for i in range(1,1001) if i % 36 == 0]
    print(square)

if __name__ == "__main__":
    run()