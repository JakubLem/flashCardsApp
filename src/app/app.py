import random
from os import system, name

# define our clear function 
def clear(): 
    if name == 'nt': 
        _ = system('cls') 
    else: 
        _ = system('clear') 


def app(flashcards):
    while True:
        clear()
        print("FlashCardsApp", "\n")
        num = random.randint(0,len(flashcards)-1)
        print("Polish:", "\n", flashcards[num].pw, "\n", flashcards[num].ps)
        x = input()
        print("English:", "\n", flashcards[num].ew, "\n", flashcards[num].es)
        x = input()
        if x == "end":
            break