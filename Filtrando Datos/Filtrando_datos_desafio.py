DATA = [
    {
        'name': 'Facundo',
        'age': 72,
        'organization': 'Platzi',
        'position': 'Technical Coach',
        'language': 'python',
    },
    {
        'name': 'Luisana',
        'age': 33,
        'organization': 'Globant',
        'position': 'UX Designer',
        'language': 'javascript',
    },
    {
        'name': 'Héctor',
        'age': 19,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'ruby',
    },
    {
        'name': 'Gabriel',
        'age': 20,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'javascript',
    },
    {
        'name': 'Isabella',
        'age': 30,
        'organization': 'Platzi',
        'position': 'QA Manager',
        'language': 'java',
    },
    {
        'name': 'Karo',
        'age': 23,
        'organization': 'Everis',
        'position': 'Backend Developer',
        'language': 'python',
    },
    {
        'name': 'Ariel',
        'age': 32,
        'organization': 'Rappi',
        'position': 'Support',
        'language': '',
    },
    {
        'name': 'Juan',
        'age': 17,
        'organization': '',
        'position': 'Student',
        'language': 'go',
    },
    {
        'name': 'Pablo',
        'age': 32,
        'organization': 'Master',
        'position': 'Human Resources Manager',
        'language': 'python',
    },
    {
        'name': 'Lorena',
        'age': 56,
        'organization': 'Python Organization',
        'position': 'Language Maker',
        'language': 'python',
    },
]

#DESAFIO, CREAR LAS LISTAS ALL_PYTHON_DEVS Y ALL_PLATZI_WORKER CON UNA COMBINACION DE FILTER Y MAP
# TMB CREAR LAS LISTA OLD_PEOPLE Y ADULTS CON LIST COMPREHENSION

def run():
    all_python_devs = [worker["name"] for worker in DATA if worker["language"] == "python"]

    #DESAFIO
    all_python_devs = list(filter(lambda worker: worker["language"] == "python" ,DATA))
    all_python_devs = list(map(lambda worker: worker["name"], all_python_devs))

    all_platzi_worker = [worker["name"] for worker in DATA if worker["organization"] == "Platzi"]

    #DESAFIO
    all_platzi_worker = list(filter(lambda worker: worker["organization"] == "Platzi", DATA))
    all_platzi_worker = list(map(lambda worker: worker["name"], all_platzi_worker))

    adults = list(filter(lambda worker: worker["age"] > 18 ,DATA))
    adults_map = list(map(lambda worker: worker["name"], adults))
    old_people = list(map(lambda worker: worker | {"old": worker["age"] > 70} , DATA)) #con | unimos diccionarios, funciona igual que el simbolo + para unir listas
    # unimos a los diccionarios worker, un diccionario nuevo llamado old que va a tener como resultado un booleano

    #DESAFIO
    adults = [worker["name"] for worker in DATA if worker["age"] > 18]
    old_people = [worker["name"] for worker in DATA if worker["age"] > 70]

    # for worker in all_python_devs:
    #     print(worker, end=" ")

    # print("")

    # for worker in all_platzi_worker:
    #     print(worker, end=" ")

    print("")

    for i in adults:
        print(i, end=" ")

    print("")

    for i in old_people:
        print(i, end=" ")


if __name__ == '__main__':
    run()
