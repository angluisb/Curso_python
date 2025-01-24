#Archivo con todas las funciones necesarias para la aplcacion linea 

def calcular_y(x,m,b):
    return m*x +b

def test_lineas():
    assert calcular_y(0,2,3) == 3
    
if __name__ == '__main__':
    if test_lineas():
        print('Todo bien')
    else:
        print("Algo Quinix")
    