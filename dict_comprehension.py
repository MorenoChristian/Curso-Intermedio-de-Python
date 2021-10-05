import math

def run() :
    # my_dict = {}

    # for i in range(0,101):
    #     if i%3 != 0:
    #         my_dict[i] = i**3 
    
    # print("Original Dict")
    # print(my_dict)

    # #aplicando dicts comprehension

    # my_dict = {i: i**3 for i in range(0,101) if i%3 != 0}

    # print("Comprehension Dict")
    # print(my_dict)

    #Desafio, primeros 1000 numeros naturales como llaves y sus valores seran sus raices cuadradas

    my_dict = {i:round(math.sqrt(i),2) for i in range(0,101)}
    
    print("Square root Dict: ")
    print(my_dict)


if __name__ == '__main__':
    run()