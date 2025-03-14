from funciones import calcular_y, graficar
import argparse
import matplotlib.pyplot as plt

def main(m,b):
    #X=[ x for x in range(1,11)]
    #Y=[calcular_y(x,m,b) for x in X]
    #print(f"Enteros:")
    #cordenadas_enteros= list(zip(X,Y))
    #print(cordenadas_enteros)
    XF = [x/10.0 for x in range(10,110,5)]
    YF =[calcular_y(x,m,b) for x in XF]
    coordenadas_flotantes = list(zip(XF,YF))
    print("Flotantes:")
    print(coordenadas_flotantes)
    
    graficar(XF,YF,m,b)
    

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-m", type=float, help='Pendiente De La Linea', default=2.0)
    parser.add_argument('-b', type=float, help='Ordenada al origen', default=3.0)
    args = parser.parse_args()
    main(args.m,args.b)