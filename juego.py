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
    print("°~ Bienvenido al juego de adivinar la palabra ~°")
    print("~°~°~°~°~°~°~°~°~°~°~°~°~°~°~°~°~°~°~°~°~°~°~°")


def elegir_palabra():
    global palabra
    global palabra_oculta
    palabra= random.choce(palabras)
    palabra_oculta =["_" for _ in palabra] 


def mostrar_palabra(palabra):
    print(" ")
    print("~°~°~°~°~°~°~°~°~°~°~°~°~°~°~°~°~°~°~°~°~°~°~°")
    print(" ")
    print(f"La palabra a adivinar tiene {len(palabra)} letras")
    print(f"Tenés {vidas} vidas, mucha suerte!")
    print("")
    print("~°~°~°~°~°~°~°~°~°~°~°~°~°~°~°~°~°~°~°~°~°~°~°")

letras_adivinar = set(palabra)


def adivinar_palabra(vidas, letras_adivinar):
 while vidas > 0:
    for letra in palabra:
        if letra in letras_adivinadas:
            print(letra, end=" ")
        else:
            print("-", end=" ")
    print(f"Te quedan {vidas} vidas")
           
    letra_ingresada = str(input("\n Por favor ingresá una letra: ").lower())

    if letra_ingresada in letras_adivinar:
        print(f"Bien! La letra {letra_ingresada} está en la palabra.")
        letras_adivinadas.append(letra_ingresada)
    else:
        print(f"la letra {letra_ingresada} no está en la palabra, intentá de nuevo!")
        vidas -= 1 
        
    if not letra_ingresada.isalpha():
        print("debe ser una letra, por favor intentá de nuevo")
        continue

    if letra_ingresada in letras_adivinadas and palabra:
        print(f"Ya ingresaste la letra {letra_ingresada}, por favor intentá de nuevo")
        continue

   


saludo()
elegir_palabra()
mostrar_palabra(palabra)
adivinar_palabra(vidas, palabra)

