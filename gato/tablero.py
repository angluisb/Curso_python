"""
tablero.py: Dibuja el tablero del juego de el gato
"""
import random

def dibuja_tablero(simbolos):
    print(f"""
        {simbolos['1']} | {simbolos['2']} | {simbolos['3']}
        ---------
        {simbolos['4']} | {simbolos['5']} | {simbolos['6']}
        ---------
        {simbolos['7']} | {simbolos['8']} | {simbolos['9']}
        """)
    
    

def ia(simbolos:dict):
    ocupado = True
    while ocupado is True:
        x= random.choice(list(simbolos.keys(1,10)))
        if simbolos[x] not in ['X','O']:
            simbolos[x]='O'
            ocupado==False
    

def user(simbolos: dict):
    ocupado = True
    nums = [str(i) for i in range(1,10)]
    while ocupado is True:
        x = input('Ingresa la Casilla')
        if (x in numeros):
            if simbolos[x] not in ['X','O']:
                simbolos[x] ='X'
                ocupado = False
            else:
                print('Casilla Ocupada')
        else:
            print('Numero Incorrecto')
    

if __name__ == '__main__':
    numeros=[str(x) for x in range(1,10)]
    simbolos = {x:x for x in numeros}
    x = random.choice(numeros)
    numeros.remove(x)
    simbolos[x] = 'X'
    dibuja_tablero(simbolos)
    ia(simbolos)
    dibuja_tablero(simbolos)
    user(simbolos)
    dibuja_tablero(simbolos)

