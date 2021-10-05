def divisor(num):
    divisors = [i for i in range(1,num + 1) if num % i == 0]

    return divisors

def run():
    while True:
        try:
            num = int(input("Ingresa un numero: "))
            if num < 0:
                raise ValueError ("No se permiten numeros negativos")
            print(divisor(num))
            print("Terminó mi programa")
            break
        except ValueError as ve:
            print(ve)




if __name__ == '__main__':
    run()