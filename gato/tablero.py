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
        x= random.choice(list(simbolos.keys()))
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
    
    def juego(simbolos:dict):
        lista_combinaciones=[
            ['1','2','3'],
            ['4','5','6'],
            ['7','8','9'],
            ['1','4','7'],
            ['2','5','8'],
            ['3','6','9'],
            ['1','5','9'],
            ['3','5','7']
        ]
        
    def checa_winner(simbolos:dict, combinaciones:list):
        for c in combinaciones:
            if simbolos[c[0]] == simbolos [c[1]] == simbolos [c[2]]:
                return simbolos[0]
        return None

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

