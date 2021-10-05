import random
import os

def run():
    words = []
    with open("C:/Users/Christian/Desktop/Informatorio/2da Etapa/Programación Web/Python/Platzi/Intermedio Python/Project/File/data.txt", "r", encoding="utf-8") as f:
        for line in f:
            words.append(line)
    word = random.choice(words)
    letra = None   
    os.system("cls")

    while True:
        if letra == None:
            print("Hangman")
            print(word)
            clue = ["_ "]*(len(word)-1)
            for i in clue:
                print(i, end="")
        else:
            os.system("cls")
            print("Hangman")
            print(word)
            for i in clue:
                print(i, end="")

        try:
            letra = input("\nSeleccione una letra: ")
            if letra.isalpha() == False:
                raise TypeError("No se permiten numeros, solo letras")
                
            for i,l in enumerate(word):
                if l == letra:
                    clue[i] = l
            
            cont = 0
            for i in clue:
                if i != "_ ":
                    cont = cont + 1
            if cont == len(clue):
                os.system("cls")
                print("¡La palabra era ",word)
                break

        except TypeError as ty:
            print(ty)
        

    


if __name__=='__main__':
    run()