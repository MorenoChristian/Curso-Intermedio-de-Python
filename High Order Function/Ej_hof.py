#Las high order function son funciones que tienen por parametros otras funciones

def saludo(function):
    function()

def hola():
    print("hola!")

def despedida():
    print("Adios!")

print(saludo(hola))
print(saludo(despedida))