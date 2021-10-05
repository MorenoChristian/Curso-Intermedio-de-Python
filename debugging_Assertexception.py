def divisor(num):
    divisors = [i for i in range(1,num + 1) if num % i == 0]

    return divisors

def run():
    while True:
        try:
            num = int(input("Ingresa un numero: "))
            assert num>0
            print(divisor(num))
            print("Terminó mi programa")
            break
        except AssertionError:
            print("No se permiten numero negativos")




if __name__ == '__main__':
    run()