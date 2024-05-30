"""Un programa donde se mostrará una palabra oculta usando tantos guiones como letras que contiene la palabra a adivinar (la palabra a adivinar será elegida por el programa usando
el módulo de Python random), la cantidad de vidas con las que cuenta el jugador y la cantidad de letras incorrectas que se va ingresando. 
Cuando el jugador ingresa una letra es necesario que se valide el dato (que sea una letra). Luego de validar la letra ingresada se corrobora si la letra ingresada pertenece a 
alguna de las letras de la palabra a adivinar. Cada vez que el jugador ingrese una letra que NO pertence a la palabra a adivinar se restará una vida.
El juego finaliza cuando el jugador se queda sin vidas o cuando adivina todas las letras de la palabra. 
Para todos los casos se debe mostrar un mensaje indicando si ganó la partida o si perdió."""  

palabras=["flor", "arbol", "manzana", "mano", "diente", "fuego", "sol", "agua", "conejo"]
vidas= 5

import random



def saludo():
    print("~°~°~°~°~°~°~°~°~°~°~°~°~°~°~°~°~°~°~°~°~°~°~°")
    print("°~ Bienvenido al juego de adivinar la palabra ~°")
    print("~°~°~°~°~°~°~°~°~°~°~°~°~°~°~°~°~°~°~°~°~°~°~°")


def elegir_palabra():
    return random.choice(palabras)
   



def mostrar_palabra(palabra, vidas):
    print("\n~°~°~°~°~°~°~°~°~°~°~°~°~°~°~°~°~°~°~°~°~°~°~°\n")
    print(f"La palabra a adivinar tiene {len(palabra)} letras")
    print(f"Tenés {vidas} vidas, ¡mucha suerte!\n")
    print("~°~°~°~°~°~°~°~°~°~°~°~°~°~°~°~°~°~°~°~°~°~°~°")


def adivinar_palabra(vidas, palabra):
    letras_adivinar = set(palabra)
    letras_adivinadas = set()
    letras_incorrectas = set()

 #cambio de método para mostrar guiones para la palabra oculta
    while vidas > 0:
        palabra_oculta = ''.join([letra if letra in letras_adivinadas else '-' for letra in palabra])
        print(f"Palabra: {palabra_oculta}")
        print(f"Te quedan {vidas} vidas")
        print(f"Letras adivinadas: {', '.join(sorted(letras_adivinadas))}")
        print(f"Letras incorrectas: {', '.join(sorted(letras_incorrectas))}")
        
        # Verificar si se adivinó toda la palabra
        if letras_adivinar == letras_adivinadas:
            return True

        letra_ingresada = input("\nPor favor ingresa una letra: ").lower()
        
        if not letra_ingresada.isalpha() or len(letra_ingresada) != 1:
            print("Debe ser una sola letra, por favor intenta de nuevo.")
            continue
        
        if letra_ingresada in letras_adivinadas or letra_ingresada in letras_incorrectas:
            print("Ya ingresaste esa letra, por favor intenta de nuevo.")
            continue

        if letra_ingresada in letras_adivinar:
            print(f"¡Bien! La letra {letra_ingresada} está en la palabra.")
            letras_adivinadas.add(letra_ingresada)
        else:
            print(f"La letra {letra_ingresada} no está en la palabra, intenta de nuevo.")
            letras_incorrectas.add(letra_ingresada)
            vidas -= 1
    
    return False
    
    



def fin_del_juego(ganaste, palabra):
    print("\n~°~°~°~°~°~°~°~°~°~°~°~°~°~°~°~°~°~°~°~°~°~°~°\n")
    if ganaste:
        print(f"¡Felicidades, ganaste! La palabra era {palabra}")
    else:
        print(f"Perdiste, la palabra era {palabra}")
    print("\n~°~°~°~°~°~°~°~°~°~°~°~°~°~°~°~°~°~°~°~°~°~°~°")

# Inicio del juego
saludo()
palabra= elegir_palabra()
mostrar_palabra(palabra, vidas)
#condición de ganar agragada para exportar a la otra función
ganaste = adivinar_palabra(vidas, palabra)
fin_del_juego(ganaste, palabra)
