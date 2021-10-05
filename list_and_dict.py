def run():
    my_list = [1, "Hello", True, 4.5]
    my_dict = {"firstname": "Christian",
                "lastname": "Moreno"}
    
    super_list = [
        {"firstname": "Christian","lastname": "Moreno"},
        {"firstname": "Juan","lastname": "Garcia"},
        {"firstname": "Susana","lastname": "Martinez"},
        {"firstname": "Vanesa","lastname": "Osuna"},
        {"firstname": "Gonzalo","lastname": "Perez"},
        {"firstname": "Mario","lastname": "Jusepe"}
    ]

    for i in super_list:
        for key,value in i.items():
            print(value, end=" ")
        print("")

    super_dict = {
        "natural_nums": [1,2,3,4,5],
        "integer_nums": [-1,-2,0,1,2],
        "floating_nums": [1.2, 4.5, 6.43]
    }

    for key, value in super_dict.items():
        print(key, "-", value)

if __name__ == '__main__':
    run()