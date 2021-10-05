def read():
    numbers = []

    with open("./Files Management/Files/numbers.txt", "r", encoding="utf-8") as f:
        for line in f:
            numbers.append(int(line))
    print(numbers)

def write():
    names = ["Facundo", "Christian", "Pepe", "Miguel", "Pin", "Rocío"]

    with open("./Files Management/Files/names.txt", "w") as f:
        for name in names:
            f.write(name)
            f.write("\n")


def run():
    write()


if __name__ == '__main__':
    run()
