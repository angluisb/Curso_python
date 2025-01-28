#Archivo con todas las funciones necesarias para la aplcacion linea 
import matplotlib.pyplot as plt


def calcular_y(x:float,m:float,b:float)->float:
    return m*x +b

def test_lineas():
    assert calcular_y(0,2,3) == 3
    
    
    
def graficar(XF:list, YF:list, m:float, b:float):
    plt.plot(XF,YF)
    plt.title(f'Linea con pendiente{m} y ordenada al origen {b}')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.show()
    
    

if __name__ == '__main__':
    if test_lineas()== 3.0:
        print('Todo bien')
    else:
        print("Algo Quinix")
