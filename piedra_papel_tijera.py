from operator import truediv
import random


def jugar():
    usuario = input("Ingrese una opción: 'pi' para piedra, 'pa' para papel, 'ti' para tijera. \n").lower()
    #\n representa el fin de la linea actual y el comienzo de la linea nueva
    #.lower, lo que hace es convertir todos los carecteres en minusculas

    computadora = random.choice(['pi', 'pa', 'ti'])

    if usuario == computadora:
        return 'Empate!!'

    if gano_el_jugador(usuario, computadora):
        return 'Ganaste!!'

    return 'Perdiste!!'


def gano_el_jugador(jugador, oponente):
    #retornar valor true si gana el jugador
    #piedra gana a tijera(pi > ti)
    #tijera gana a papel(ti > pa)
    #papel gana a piedra(pa > pi)

    if ((jugador == 'pi' and oponente == 'ti')
        or (jugador == 'ti' and oponente == 'pa')
        or (jugador == 'pa' and oponente == 'pi')):
        return True

    else:
        return False


print(jugar())
