import tablero


def main():
    numeros = [str(x) for x in range(1,10) ]
    simbolos = {x:x for x in numeros}
    g = tablero.juego(simbolos=simbolos)
    
    if g is not None:
        print(f'El ganador es {g}')
    else:
        print('Empate')