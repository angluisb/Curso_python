

#Calculo de coordenadas de lineas.
def calcular_y(x,m,b):
    return m*x +b

def main():
    m=2
    b=3
    x=5
    y=calcular_y(x,m,b)
    print(f"Para x = {x}, y = {y}")
    

if __name__ == '__main__':
    main()