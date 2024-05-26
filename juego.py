"""Un programa donde se mostrará una palabra oculta usando tantos guiones como letras que contiene la palabra a adivinar (la palabra a adivinar será elegida por el programa usando
el módulo de Python random), la cantidad de vidas con las que cuenta el jugador y la cantidad de letras incorrectas que se va ingresando. 
Cuando el jugador ingresa una letra es necesario que se valide el dato (que sea una letra). Luego de validar la letra ingresada se corrobora si la letra ingresada pertenece a 
alguna de las letras de la palabra a adivinar. Cada vez que el jugador ingrese una letra que NO pertence a la palabra a adivinar se restará una vida.
El juego finaliza cuando el jugador se queda sin vidas o cuando adivina todas las letras de la palabra. 
Para todos los casos se debe mostrar un mensaje indicando si ganó la partida o si perdió."""  

palabras=["flor", "arbol", "manzana", "mano", "diente", "fuego", "sol", "agua", "conejo"]
vidas= 5

import random

letras_adivinadas= []

def saludo():
    print("~°~°~°~°~°~°~°~°~°~°~°~°~°~°~°~°~°~°~°~°~°~°~°")
    print("°~ Bienvenido al juego de adivinar la palabra~°")
    print("~°~°~°~°~°~°~°~°~°~°~°~°~°~°~°~°~°~°~°~°~°~°~°")


def elegir_palabra():
    return random.choice(palabras)

palabra = elegir_palabra()

def mostrar_palabra(palabra):
    print(" ")
    print("~°~°~°~°~°~°~°~°~°~°~°~°~°~°~°~°~°~°~°~°~°~°~°")
    print(" ")
    print(f"La palabra a adivinar tiene {len(palabra)} letras")
    for letra in palabra:
        print("-", end=" ")
        """if letra in palabra and letras_adivinadas:
         print(letra, end=" ")
        else:
            print("-", end=" ")"""
    print(f"Tenés {vidas} vidas")
    print("")
    print("~°~°~°~°~°~°~°~°~°~°~°~°~°~°~°~°~°~°~°~°~°~°~°")



def adivinar_palabra(vidas, palabra):
 while vidas > 0:
    letra_ingresada = str(input("\n Por favor ingresá una letra: "))

    if letra_ingresada.lower in palabra:
        print(f"Bien! La letra {letra_ingresada} está en la palabra.")
        letras_adivinadas.append(letra_ingresada.lower())
    else:
        print(f"La letra {letra_ingresada} no está en la palabra.")
        vidas -= 1 

    if not letra_ingresada.isalpha():
        print("debe ser una letra, por favor intentá de nuevo")
        continue

    mostrar_palabra(palabra)
    print(f"Te quedan {vidas} vidas")

saludo()
mostrar_palabra(palabra)
adivinar_palabra(vidas, palabra)