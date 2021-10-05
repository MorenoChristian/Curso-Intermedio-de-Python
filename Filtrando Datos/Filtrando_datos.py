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


def run():
    all_python_devs = [worker["name"] for worker in DATA if worker["language"] == "python"]
    all_platzi_worker = [worker["name"] for worker in DATA if worker["organization"] == "Platzi"]
    adults = list(filter(lambda worker: worker["age"] > 18 ,DATA))
    adults_map = list(map(lambda worker: worker["name"], adults))
    old_people = list(map(lambda worker: worker | {"old": worker["age"] > 70} , DATA)) #con | unimos diccionarios, funciona igual que el simbolo + para unir listas
    # unimos a los diccionarios worker, un diccionario nuevo llamado old que va a tener como resultado un booleano
    
    for worker in all_python_devs:
        print(worker, end=" ")
    
    print("")

    for worker in all_platzi_worker:
        print(worker, end=" ")

    print("")

    #print(adults)
    for worker in adults_map:
        print(worker, end= " ")

    print("")

    for worker in old_people:
        print(worker, end=" ")


if __name__ == '__main__':
    run()
